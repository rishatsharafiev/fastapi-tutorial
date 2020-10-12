from enum import Enum
from fastapi import FastAPI

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


model_mapping = {
    ModelName.alexnet: {"message": "Deep Learning FTW!"},
    ModelName.resnet: {"message": "LeCNN all the images"},
    ModelName.lenet: {"message": "Have some residuals"},
}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    return model_mapping.get(model_name, {})


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
