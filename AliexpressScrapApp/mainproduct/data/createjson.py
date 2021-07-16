import json
import os

def file_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    new_path = os.path.join(dir, *split_path)
    return new_path

f = open(file_path('maincategory.json'),)
productId_list = json.load(f)
for item in productId_list:
    for sub in item["subcategory"]:
        data = {
            "maincatagory": item['maincategory'],
            "categoryName": sub,
            "productId": []
        }
        filename = data["categoryName"].replace('/'," ")
        with open(file_path(f'{filename}.json'),'w') as f:
            json.dump(data, f, indent=4)



