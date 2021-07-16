from call_json import *
from getproductId import *
from update import *
from scrap import *

def AliexpressScrap(maincategory, subcategory):
    maincategory,subcategory,link = call_json_data(maincategory = maincategory,subcategory = subcategory)
    filepath = get_productID(maincategory,subcategory,link)
    # print(filepath)
    update_data(file_path(filepath.split('_')[0]+".json"), file_path(filepath))

    ## scraping
    f = open(filepath,)
    productId_list = json.load(f)
    print(f"[TIME: {datetime.datetime.now()}] - [URL: https://th.aliexpress.com/] - start scraping")
    workbook_file = file_path(f"{os.getcwd()}/excel/{productId_list['categoryName']}.xlsx")
    running = True
    App = Aliexpress(productId_list,workbook_file)
    App.RUN(productId_list)

    ## update data in file json and remove new json file


    data = open(file_path(filepath.split('_')[0]+".json"),"r")
    update_data_json = json.load(data)
    for new in productId_list["productId"]:
        update_data_json["productId"].append(new)

    data_up = open(file_path(filepath.split('_')[0]+".json"),"w")
    json.dump(update_data_json, data_up)
    data_up.close()
    f.close()
    os.remove(filepath)
    print(f"[TIME: {datetime.datetime.now()}] - [URL: https://th.aliexpress.com/] - finish scraping")
    return


# AliexpressScrap(maincategory = "Luggage & Bags",subcategory = "Women's Bags")
