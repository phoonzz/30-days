# DELIBERATELY INSECURE: BOLA (Broken Object Level Authorization) demo.
# No authentication, and the caller picks whose orders to see via ?user_id=N.
# Never deploy this. The secure version is server.py.
from fastapi import FastAPI

from server import ORDERS

app = FastAPI()


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/orders")
def list_orders(user_id: int):
    return [o for o in ORDERS if o["user_id"] == user_id]
