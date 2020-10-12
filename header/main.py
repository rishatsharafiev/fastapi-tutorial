from typing import List, Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    x_token: Optional[List[str]] = Header(None),
):
    return {"User-Agent": user_agent, "X-Token values": x_token}
