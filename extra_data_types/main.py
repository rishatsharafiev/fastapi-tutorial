from datetime import datetime, time, timedelta
from typing import Optional, Union
from uuid import UUID

from fastapi import Body, FastAPI, Path

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID = Path(..., example=UUID("ddd92b88-54b1-4385-85bd-a533b1cf96e3")),
    start_datetime: Optional[datetime] = Body(None, example="2020-10-12T09:31:46.330Z"),
    end_datetime: Optional[datetime] = Body(None, example="2020-10-12T19:31:46.330Z"),
    repeat_at: Optional[time] = Body(None, example="00:00:00"),
    process_after: Optional[timedelta] = Body(None),
):
    start_process: Optional[datetime] = None
    duration: Optional[timedelta] = None
    if start_datetime and process_after:
        start_process = start_datetime + process_after
    if end_datetime and start_process:
        duration = end_datetime - start_process

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
