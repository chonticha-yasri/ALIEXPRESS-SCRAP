## maincatagory
from spider import spider
import json

data_list = []
main_list = ["Apparel Accessories","Cellphones & Telecommunications","Consumer Electronics","Computer & Office",
"Education & Office Supplies","Home Appliances","Luggage & Bags","Toys & Hobbies","Sports & Entertainment"]

soup = spider("https://www.aliexpress.com/all-wholesale-products.html")
for catagory in soup.find_all('div',class_="item util-clearfix"):
	data = {}
	sub_name = []
	link_sub  = []
    ## scrap name catagory, name subcatagory and link subcatagory##
	if catagory.a.text in main_list:
		data['maincatagory'] = catagory.a.text
		for subcatagory in catagory.find_all('li'):
			sub_name.append(subcatagory.a.get_text(strip=True))
			link_sub.append("https:"+subcatagory.a['href'])
	data['subcatagory'] = sub_name
	data['link_subcatagory'] = link_sub
	if data['subcatagory'] != []:
		data_list.append(data)


with open('maincatagory.json','w') as f:
	json.dump(data_list, f, indent=4)