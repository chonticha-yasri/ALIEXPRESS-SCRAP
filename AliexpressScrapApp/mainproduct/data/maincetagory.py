## maincategory
import sys
sys.path.insert(1, './AliexpressScrapApp')
from spider import spider
import json

data_list = []
main_list = ["Apparel Accessories","Cellphones & Telecommunications","Consumer Electronics","Computer & Office",
"Education & Office Supplies","Home Appliances","Luggage & Bags","Toys & Hobbies","Sports & Entertainment"]

soup = spider("https://www.aliexpress.com/all-wholesale-products.html")
for category in soup.find_all('div',class_="item util-clearfix"):
	data = {}
	sub_name = []
	link_sub  = []
    ## scrap name category, name subcategory and link subcategory##
	if category.a.text in main_list:
		data['maincategory'] = category.a.text
		for subcategory in category.find_all('li'):
			sub_name.append(subcategory.a.get_text(strip=True))
			link_sub.append("https:"+subcategory.a['href'])
	data['subcategory'] = sub_name
	data['link_subcategory'] = link_sub
	if data['subcategory'] != []:
		data_list.append(data)


with open('maincategory.json','w') as f:
	json.dump(data_list, f, indent=4)