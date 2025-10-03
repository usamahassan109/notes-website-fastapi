from configuration.db import db, collection  # 🎯 MongoDB collection
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bson.objectid import ObjectId  # 🔑 for MongoDB _id

note = APIRouter()
templates = Jinja2Templates(directory="templates")

# ✅ READ NOTES
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    try:
        newDoc = []
        if collection is not None:
            docs = collection.find()
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
        if collection is not None:
            new_note = {"title": title, "desc": desc, "important": important}
            result = collection.insert_one(new_note)
            print(f"✅ Data saved with ID: {result.inserted_id}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")
    return RedirectResponse(url="/", status_code=303)

# ✅ DELETE NOTE
@note.get("/delete/{note_id}", response_class=RedirectResponse)
async def delete_note(note_id: str):
    try:
        if collection is not None:
            result = collection.delete_one({"_id": ObjectId(note_id)})
            if result.deleted_count:
                print(f"✅ Note with ID {note_id} deleted")
    except Exception as e:
        print(f"❌ Error deleting note: {e}")
    return RedirectResponse(url="/", status_code=303)

# ✅ UPDATE NOTE
@note.post("/update/{note_id}", response_class=RedirectResponse)
async def update_note(
    request: Request,
    note_id: str,
    title: str = Form(...),
    desc: str = Form(...),
    important: bool = Form(False)
):
    try:
        if collection is not None:
            result = collection.update_one(
                {"_id": ObjectId(note_id)},
                {"$set": {"title": title, "desc": desc, "important": important}}
            )
            if result.modified_count:
                print(f"✅ Note with ID {note_id} updated")
    except Exception as e:
        print(f"❌ Error updating note: {e}")
    return RedirectResponse(url="/", status_code=303)
