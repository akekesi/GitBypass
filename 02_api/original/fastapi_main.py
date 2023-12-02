from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException


CONTENT = {}


class Item(BaseModel):
    name: str = Field(description="name of the item")
    flag: bool = Field(description="flag of item")
    path: str = Field(description="path of its directory on the server")


app = FastAPI(
    title="Bypass Server",
    version="0.0.1"
)


@app.get("/")
def get_content() -> dict[str, dict[str, Item]]:
    return {"content": CONTENT}


@app.get("/{name}")
def get_item(name: str) -> dict[str, Item]:
    if name not in CONTENT:
        raise HTTPException(
            status_code=404,
            detail=f"{name} does not exist",
        )
    return {name: CONTENT[name]}


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.name in CONTENT:
        raise HTTPException(
            status_code=400,
            detail=f"{item.name} already exists",
        )
    CONTENT[item.name] = item
    return {"added": item}


@app.put("/{name}")
def change_flag_path_of_item(
    name: str,
    flag: bool | None = None,
    path: str | None = None
) -> dict[str, Item]:
    if name not in CONTENT:
        raise HTTPException(
            status_code=404,
            detail=f"{name} does not exist",
        )
    if flag != None:
        CONTENT[name].flag = flag
    if path != None:
        CONTENT[name].path = path
    return {"changed": CONTENT[name]}


@app.delete("/delete/{name}")
def delete_item(name: str) -> dict[str, Item]:
    if name not in CONTENT:
        raise HTTPException(
            status_code=404,
            detail=f"{name} does not exist",
        )
    tmp = CONTENT.pop(name)
    return {"deleted": tmp}
