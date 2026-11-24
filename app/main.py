import os

import psycopg
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://app:app@localhost:5432/app")

app = FastAPI(title="DevOps API")
Instrumentator().instrument(app).expose(app)


class ItemIn(BaseModel):
    name: str


def get_conn() -> psycopg.Connection:
    conn = psycopg.connect(DATABASE_URL, connect_timeout=3)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT NOT NULL)"
    )
    return conn


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    with get_conn() as conn:
        rows = conn.execute("SELECT id, name FROM items ORDER BY id").fetchall()
    return [{"id": r[0], "name": r[1]} for r in rows]


@app.post("/items", status_code=201)
def create_item(item: ItemIn):
    with get_conn() as conn:
        row = conn.execute(
            "INSERT INTO items (name) VALUES (%s) RETURNING id", (item.name,)
        ).fetchone()
    return {"id": row[0], "name": item.name}