import requests
import json
import datetime
import re
import pandas as pd
import os
import time
import sys
sys.path.insert(1, './AliexpressScrapApp')
from spider import spider
from create_excel import *


class Aliexpress:
    def __init__(self,_productId,workbook_file):
        self.productId = _productId
        self.slash = "\\"
        self.workbook_file = workbook_file



    def request(self,productId):
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        url = f"https://th.aliexpress.com/item/{productId}.html"
        data = None
        try:
            r = requests.get(url, headers = header,timeout=10)
            match = re.search(r'data: ({.+})', r.text).group(1)
            data = json.loads(match)
        except:
            try:
                r = requests.get(url, headers = header,timeout=10)
                match = re.search(r'data: ({.+})', r.text).group(1)
                data = json.loads(match)
            except:
                pass
        return data

    def Mainfolder(self):
        path = os.getcwd()
        folder = "AliexpressImage"
        directory = path+self.slash+folder
        if(os.path.isdir(directory)):
            print("directory exists: "+folder)
        else:
            os.mkdir(directory)
            print("created: "+folder)
        return path+self.slash+folder

    def CreateFolder(self,directoryName,foldername):
        directory = directoryName+foldername
        if(os.path.isdir(directory)):
            print("directory exists: "+foldername)
        else:
            os.makedirs(directory)
            print("created: "+foldername)
        return directory


    def download_image(self,im_url, path_complete, file_name):
        try:
            r = requests.get(im_url,timeout=10)
            r.encoding = "utf-8"
            completeName = os.path.join(path_complete, file_name)
            open(completeName , 'wb').write(r.content)
            print("[*] Downloaded Image: %s" % file_name)
        except:
            print("[~] Error Occured with %s" % file_name)
            pass
        return



    def descrpition(self, data, list_im):
        soup = spider(data["descriptionModule"]["descriptionUrl"])
        for imageDes in soup.find_all("img"):
            list_im.append(imageDes["src"])
        return soup.get_text()

    def productDetail(self,data,path_complete,count,path_complete_excel):
        productdetail = []
        directoryImage = []

        list_im = []
        dataDetail = {
        "categoryName" : self.productId["categoryName"],
        "productID" : data["pageModule"]["itemDetailUrl"].split("/")[-1].split(".")[0],
        "title" : data["titleModule"]["subject"],
        "productUrl" : data["pageModule"]["itemDetailUrl"],
        "max_price" : data["priceModule"]["formatedPrice"],
        "brand" : " "
        }

        try:
            dataDetail["ActivityPrice"] = data["priceModule"]["formatedActivityPrice"]
        except:
            dataDetail["ActivityPrice"] = data["priceModule"]["formatedPrice"]


        for image in data["imageModule"]["imagePathList"]:
            list_im.append(image)
        try:
            for brand in data["specsModule"]['props']:
                if brand['attrName'] == "ชื่อยี่ห้อ":
                    dataDetail["brand"] = brand["attrValue"]
        except:
            dataDetail["brand"] = " "


        propertyName = []
        propertyValueDisplayName = []
        try:
            for Property in data["skuModule"]["productSKUPropertyList"]:
                propertyName.append(Property["skuPropertyName"]) # name property
                for value in Property["skuPropertyValues"]:
                    propertyValueDisplayName.append(value["propertyValueDisplayName"]) # value property
                    try:
                        list_im.append(value["skuPropertyImagePath"]) # image property
                    except:
                        pass
        except:
            pass


        dataDetail["name_product_property"] = propertyName
        dataDetail["product_property_value"] = propertyValueDisplayName

        dataDetail["description"] = self.descrpition(data,list_im)

        productdetail.append(dataDetail)

        i = 1
        image_name = []
        for link_im in list_im:
            try:
                if dataDetail["brand"] != " ":
                    name_im = f'{dataDetail["brand"]}_{dataDetail["productID"]}_{i:03}.jpg'
                    self.download_image(link_im, path_complete, name_im)
                    image_name.append(name_im)
                else:
                    name_im = f'TP_{dataDetail["productID"]}_{i:03}.jpg'
                    self.download_image(link_im, path_complete, name_im)
                    image_name.append(name_im)

            except:
                name_im = f'TP_{dataDetail["productID"]}_{i:03}.jpg'
                self.download_image(link_im, path_complete, name_im)
                image_name.append(name_im)
            i+=1

        pathIm = {
        "productID" : dataDetail["productID"],
        "directory" : path_complete_excel,
        "ImageName" : image_name
        }

        directoryImage.append(pathIm)
        df1 = pd.DataFrame(productdetail)
        df2 = pd.DataFrame(directoryImage)
        if count == 0:
            append_df_to_excel(self.workbook_file, df1, sheet_name='product', index=False,startrow=None)
            append_df_to_excel(self.workbook_file, df2, sheet_name='directoryImage', index=False,startrow=None)
        else:
            append_df_to_excel(self.workbook_file, df1, sheet_name='product',header=None, index=False,startrow=None)
            append_df_to_excel(self.workbook_file, df2, sheet_name='directoryImage',header=None, index=False,startrow=None)

        return



    def RUN(self, productdetail):
        directory = self.Mainfolder()
        # create sub category
        self.CreateFolder(directory, self.slash + self.productId["categoryName"])
        count = 0
        for productID in self.productId["productId"]:
            path_complete = directory, self.slash + self.productId["categoryName"]+ self.slash + str(productID)
            path_complete = ''.join(path_complete)

            path_complete_excel = self.productId["categoryName"]+ self.slash + str(productID)
            path_complete_excel = ''.join(path_complete_excel)

            self.CreateFolder(path_complete,"")
            print(path_complete)

            data = self.request(productID)
            if data is not None:
                self.productDetail(data,path_complete,count,path_complete_excel)
                count+=1
            else:
                pass


