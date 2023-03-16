import json

todo_types = ["roomitemtypes", "wallitemtypes"]

# Load the JSON data from the file
with open("../assets/gamedata/FurnitureData.json", encoding='utf-8') as f:
    data = json.load(f)

with open("catalog_items.sql", "w", encoding='utf-8') as f:
    for todo_type in todo_types:
        for furni in data[todo_type]["furnitype"]:
            furni_id = furni["id"]
            if furni["name"]:
                furni_name = furni["name"].replace("'", "''").strip()[:55]
                f.write(f"UPDATE catalog_items SET catalog_name = '{furni_name}' WHERE item_ids = '{furni_id}';\n")
                #f.write(f"UPDATE items_base SET public_name = '{furni_name}' WHERE id = '{furni_id}';\n")
