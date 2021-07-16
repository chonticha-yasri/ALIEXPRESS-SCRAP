import json
import os


def file_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    new_path = os.path.join(dir, *split_path)
    return new_path


f = open(file_path('data\maincategory.json'),)
productId_list = json.load(f)

def call_json_data(maincategory,subcategory):
    for item in productId_list:
        if item['maincategory'] == maincategory:
            for sub,link in zip(item['subcategory'],item['link_subcategory']):
                if sub == subcategory:
                    maincategory = item['maincategory']
                    subcategory = sub
                    link = link
    return maincategory,subcategory,link

# maincategory,subcategory,link = call_json_data( maincategory = "Luggage & Bags",subcategory = "Women's Bags")