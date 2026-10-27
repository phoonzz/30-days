import secrets

from fastapi import Depends, FastAPI, Header, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])

USERS = [
    {"id": 1, "name": "alice", "password_hash": "$2b$12$Ir5Eu3Xc30u8A78qNOVd2u/qTQkjpsZLDjhDFlYnbwHOLl5HMXGMa"},
    {"id": 2, "name": "bob", "password_hash": "$2b$12$5CJHoa4URV5VFxIujCTkGO9Va6c4U4bKdj8oJz.YCr2YUl9N4Oaiq"},
    {"id": 3, "name": "carol", "password_hash": "$2b$12$zoww/roH14PZkYrVp16Ez.hQWtGleBT6/Y/v5W/KtB.m4CeS9z8vu"},
]

ORDERS = [
    {"id": 1, "user_id": 1, "item": "keyboard", "amount": 49.99},
    {"id": 2, "user_id": 1, "item": "mouse", "amount": 19.50},
    {"id": 3, "user_id": 1, "item": "monitor", "amount": 189.00},
    {"id": 4, "user_id": 2, "item": "laptop stand", "amount": 34.25},
    {"id": 5, "user_id": 2, "item": "webcam", "amount": 59.90},
    {"id": 6, "user_id": 2, "item": "headset", "amount": 79.00},
    {"id": 7, "user_id": 3, "item": "usb hub", "amount": 24.75},
    {"id": 8, "user_id": 3, "item": "desk lamp", "amount": 39.00},
    {"id": 9, "user_id": 3, "item": "notebook", "amount": 8.40},
]

TOKENS = {}

# Verified against when the username is unknown, so both failures cost the same.
DUMMY_HASH = pwd_context.hash(secrets.token_urlsafe(16))


class LoginRequest(BaseModel):
    username: str
    password: str


def current_user_id(authorization: str | None = Header(default=None)) -> int:
    scheme, _, token = (authorization or "").partition(" ")
    user_id = TOKENS.get(token) if scheme.lower() == "bearer" else None
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Missing or invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_id


@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.post("/login")
def login(body: LoginRequest):
    user = next((u for u in USERS if u["name"] == body.username), None)
    ok = pwd_context.verify(body.password, user["password_hash"] if user else DUMMY_HASH)
    if user is None or not ok:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = secrets.token_urlsafe(32)
    TOKENS[token] = user["id"]
    return {"access_token": token, "token_type": "bearer"}


@app.get("/orders")
def list_orders(user_id: int = Depends(current_user_id)):
    return [o for o in ORDERS if o["user_id"] == user_id]


@app.get("/orders/{order_id}")
def get_order(order_id: int, user_id: int = Depends(current_user_id)):
    for o in ORDERS:
        if o["id"] == order_id and o["user_id"] == user_id:
            return o
    raise HTTPException(status_code=404, detail="Order not found")
