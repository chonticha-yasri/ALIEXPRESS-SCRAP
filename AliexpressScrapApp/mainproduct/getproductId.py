import requests
import json
import re
import time
import os


def request(link,page):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    url = f"{link}?page={page}"

    r = requests.get(url, headers = header )
    match = re.findall(r'window.runParams = ({.*})', r.text)
    data = json.loads(match[1])
    return data

def file_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    new_path = os.path.join(dir, *split_path)
    return new_path

def get_productID(maincategory,subcategory,link):
    productId = []
    condition = True
    # maincategory,subcategory,link = call_json_data( maincategory = "Luggage & Bags",subcategory = "Women's Bags")
    page = 1
    while condition:
        print(f"page{page}")
        if page == 1:
            data = request(link,page)
            data_category = {
                "maincategory" : maincategory,
                "categoryName" : subcategory}

        try:
            len_data = []
            data = request(link,page)
            for item in data["mods"]["itemList"]["content"]:
                productId.append(item["productId"])
                len_data.append(item["productId"])
            print("product Sum",len(len_data))
        except:
            condition = False
        page+=1

    data_category["productId"] = productId

    # with open(f'{subcategory}.json','w') as f:
    #     json.dump(data_category, f, indent=4)

    # return productId

    with open(file_path(f'productData/{data_category["categoryName"]}_new.json'),'w') as f:
        json.dump(data_category, f, indent=4)

    return file_path(f'productData/{data_category["categoryName"]}_new.json')


# get_productID()