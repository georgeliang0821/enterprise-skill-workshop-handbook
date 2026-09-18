"""
mock_jira_server.py
────────────────────
一個極簡化的假 Jira 伺服器,只支援課堂 Lab 需要的兩個行為:
  1. GET  /rest/api/2/search?jql=...        依 summary 關鍵字模擬查詢是否已有相同票
  2. POST /rest/api/2/issue                 建立一張新票,回傳票號

這不是真的 Jira,目的是讓學員在沒有企業 Jira 帳號的情況下,
也能練習「Skill 呼叫外部系統 API、並且要處理『避免重複建票』」這個真實場景。

啟動方式:
    pip install -r requirements.txt
    python -m uvicorn mock_jira_server:app --reload --port 9000
"""
from fastapi import FastAPI, Query, Header, HTTPException
from pydantic import BaseModel
import itertools

app = FastAPI(title="Mock Jira Server (課堂練習用)")

_issue_seq = itertools.count(101)
_issues = []  # 每筆: {"key": "MIP-101", "summary": "...", "assignee": "...", "duedate": "...", "priority": "..."}

FAKE_VALID_TOKEN = "mock-jira-token-classroom-only"


def verify_token(authorization: str = Header(None)):
    """課堂用的最基本假 token 驗證:token 不符就回 401,讓「認證失敗」情境可以被實際觸發與測試。"""
    if authorization != f"Bearer {FAKE_VALID_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized: missing or invalid token")


class CreateIssueRequest(BaseModel):
    project_key: str
    summary: str
    assignee: str | None = None
    duedate: str | None = None
    priority: str | None = None


@app.get("/rest/api/2/search")
def search_issues(jql: str = Query(..., description="極簡化 JQL,課堂練習只支援 summary ~ \"關鍵字\" 這種寫法"), authorization: str = Header(None)):
    """
    真實 Jira 的 JQL 語法複雜得多,這裡只做課堂需要的簡化比對:
    從 jql 字串裡抓出雙引號包住的關鍵字,對 summary 做包含比對。
    """
    verify_token(authorization)
    keyword = jql.split('"')[1] if '"' in jql else ""
    matches = [i for i in _issues if keyword and keyword in i["summary"]]
    return {"total": len(matches), "issues": matches}


@app.post("/rest/api/2/issue")
def create_issue(req: CreateIssueRequest, authorization: str = Header(None)):
    verify_token(authorization)
    key = f"{req.project_key}-{next(_issue_seq)}"
    issue = {
        "key": key,
        "summary": req.summary,
        "assignee": req.assignee,
        "duedate": req.duedate,
        "priority": req.priority,
    }
    _issues.append(issue)
    return {"key": key}


@app.get("/debug/issues")
def list_all_issues():
    """課堂除錯用:列出目前所有已建立的假票。"""
    return _issues


@app.post("/debug/reset")
def reset_all_issues():
    """課堂除錯用:清空所有假票。撞牆輪(naive 版)結束後、硬化輪開始前呼叫,
    讓兩輪的驗證結果不互相污染。不需要 token——這是課堂工具,不是被模擬的 Jira API。"""
    count = len(_issues)
    _issues.clear()
    return {"cleared": count}
