import requests
import json
import re
import os


def request(searchText,page):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    SearchText = searchText
    url = f"https://th.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={SearchText}&ltype=wholesale&SortType=default&page={page}"

    r = requests.get(url, headers = header )
    match = re.findall(r'window.runParams = ({.*})', r.text)
    data = json.loads(match[1])
    return data

def file_path(relative_path):
    dir = os.path.dirname(os.path.abspath(__file__))
    split_path = relative_path.split("/")
    new_path = os.path.join(dir, *split_path)
    return new_path

def get_productID(searchtext):
    productId = []
    condition = True
    page = 1
    while condition:
        print(f"page{page}")
        if page == 1:
            data = request(f"{searchtext}",page)
            data_category = {
                "categoryName" : data["exposureParams"]['keyword'],
                "ENcategoryName" : data["exposureParams"]['enKeyword']}

        try:
            len_data = []
            data = request(f"{searchtext}",page)
            for item in data["mods"]["itemList"]["content"]:
                productId.append(item["productId"])
                len_data.append(item["productId"])
            print("number of products : ",len(len_data))
        except:
            condition = False
        page+=1

    data_category["productId"] = productId
    
    with open(file_path(f'productData/{data_category["ENcategoryName"]}_new.json'),'w') as f:
        json.dump(data_category, f, indent=4)

    return file_path(f'productData/{data_category["ENcategoryName"]}_new.json')


# get_productData("ร่ม")