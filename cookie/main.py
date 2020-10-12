from typing import Optional

from fastapi import Cookie, FastAPI, Response

app = FastAPI()


@app.get("/items/")
async def read_items(response: Response, ads_id: str = Cookie(None)):
    response.set_cookie(key="ads_id", value=str(ads_id), path="/")
    return {"ads_id": ads_id}
