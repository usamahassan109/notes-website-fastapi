# def noteEntity(item) -> dict:
#     return {
#         "id": str(item["_id"]),
#         "title": item.get("title", ""),
#         "desc": item.get("desc", ""),
#         "important": item.get("important", False)
#     }

# def notesEntity(items) -> list:
#     return [noteEntity(item) for item in items]

def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title", ""),
        "desc": item.get("desc", ""),
        "important": item.get("important", False)
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]
