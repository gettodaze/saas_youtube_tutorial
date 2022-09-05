from __future__ import annotations

from fastapi import FastAPI
from mangum import Mangum

from app.openai_backend import get_cat_nicknames

app = FastAPI()
handler = Mangum(app)


@app.get("/cat_nicknames")
def read_root(prompt: str):
    return {"message": prompt}
    return {"message": get_cat_nicknames(prompt)}
