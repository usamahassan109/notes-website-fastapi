# from fastapi import FastAPI
# from routes.note import note
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# app.include_router(note)

# app.mount("/static", StaticFiles(directory="static"), name="static")

from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(note, tags=["Notes"])  # ✅ Added tag

app.mount("/static", StaticFiles(directory="static"), name="static")

