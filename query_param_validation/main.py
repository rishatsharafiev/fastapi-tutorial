from typing import Optional, List, Any, Dict

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: str = Query(..., min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_2/")
async def read_items_2(
    q: Optional[List[str]] = Query(
        ["foo", "bar"],
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=2,
        alias="item-query",
        deprecated=True,
    )
):
    query_items = {"q": q}
    return query_items
