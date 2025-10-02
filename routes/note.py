# from fastapi import APIRouter, Request, Form
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from model.note import Note
# from configuration.db import conn
# from schemas.note import noteEntity, notesEntity 

# note = APIRouter()
# templates = Jinja2Templates(directory="templates")
# @note.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs = conn.notes.notes.find()  # ✅ find_one → find
#     newDoc = []
#     for doc in docs:
#         newDoc.append({
#             "id": str(doc["_id"]),
#             "title": doc["title"],
#             "desc": doc["desc"],
#             "important": doc.get("important", False)
#         })
#     return templates.TemplateResponse("index.html", {"request": request, "newDoc": newDoc})
# @note.post("/")
# async def create_note(
#     title: str = Form(...),
#     desc: str = Form(...),
#     important: bool = Form(False)
# ):
#     new_note = {"title": title, "desc": desc, "important": important}
#     inserted_note = conn.notes.notes.insert_one(new_note)
#     return {"id": str(inserted_note.inserted_id)}



# # @note.post("/")
# # async def create_note(
# #     title: str = Form(...),
# #     description: str = Form(...)
# # ):
# #     # ✅ create a dictionary from form fields
# #     new_note = {"title": title, "description": description}
# #     inserted_note = conn.notes.notes.insert_one(new_note)
# #     return {"id": str(inserted_note.inserted_id)}
from configuration.db import db, collection  # 🎯 Import collection
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# ✅ READ NOTES
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        if collection is not None:
            docs = collection.find()
            newDoc = []
            for doc in docs:
                newDoc.append({
                    "id": str(doc["_id"]),
                    "title": doc.get("title", ""),
                    "desc": doc.get("desc", ""),
                    "important": doc.get("important", False)
                })
            return templates.TemplateResponse("index.html", {"request": request, "newDoc": newDoc})
    except Exception as e:
        print(f"❌ Error reading data: {e}")
    
    return templates.TemplateResponse("index.html", {"request": request, "newDoc": []})


# ✅ CREATE NOTE
@note.post("/", response_class=HTMLResponse)
async def create_note(
    request: Request,
    title: str = Form(...),
    desc: str = Form(...),
    important: bool = Form(False)
):
    try:
        # 🔍 Debug print: Check MongoDB collection reference
        print(f"🧠 Collection reference: {collection}")

        if collection is not None:
            new_note = {"title": title, "desc": desc, "important": important}
            result = collection.insert_one(new_note)
            print(f"✅ Data saved to MongoDB with ID: {result.inserted_id}")
        else:
            print(f"⚠️ Collection is None — data not saved")

    except Exception as e:
        print(f"❌ Error saving data: {e}")

    # 🔁 Redirect back to homepage
    return RedirectResponse(url="/", status_code=303)
