import json
from ProductID import file_path

def update_data(olddata, newdata):
    f1 = open(olddata,'r',encoding='utf-8')
    productId_list1 = json.load(f1)
    f1.close()

    f2 = open(newdata,'r',encoding='utf-8')
    productId_list2 = json.load(f2)
    f2.close()
    set1 = set(productId_list1["productId"])
    set2 = set(productId_list2["productId"])

    productId_list2["productId"] = list(set2.difference(set1))
    print(f"found {len(list(set2.difference(set1)))} new product")
    ## change new data
    a_file = open(newdata, "w")
    json.dump(productId_list2, a_file)
    a_file.close()

    return
# update_data(file_path('productID/Umbrella.json'), file_path('productID/Umbrella_new.json'))