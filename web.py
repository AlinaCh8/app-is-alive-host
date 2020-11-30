from fastapi import FastAPI
from app.is_alive_host import is_alive_host
from typing import Optional

app = FastAPI()


@app.get("/")
def the_сheck():
    return {
        'The_сheck':
        'Enter hostname or page address: /healthz?hostname=<please write it here>'
    }


@app.get("/healthz")
def read_item(hostname: Optional[str]):
    result = is_alive_host(hostname)
    return {'status': 'up' if result else 'down'}