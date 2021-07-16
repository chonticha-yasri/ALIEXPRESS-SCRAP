## https://github.com/python/mypy/blob/master/README.md
Aliexpress scraping Typing for Python
=======================================

fastwork scraping
----------------------------------

หมวดหมู่สินค้าที่ต้องการมีดังนี้
1. [เครื่องประดับ เสื้อผ้า](https://www.aliexpress.com/category/205776616/apparel-accessories.html)
2. [โทรศัพท์มือถือ & telecommunications](https://www.aliexpress.com/category/509/cellphones-telecommunications.html)
3. [อุปกรณ์อิเล็กทรอนิกส์](https://www.aliexpress.com/category/44/consumer-electronics.html)
4. [คอมพิวเตอร์และออฟฟิศ](https://www.aliexpress.com/category/7/computer-office.html)
5. [อุปกรณ์ออฟฟิศและการเรียน](https://www.aliexpress.com/category/21/education-office-supplies.html)
6. [เครื่องใช้ในบ้าน](https://www.aliexpress.com/category/6/home-appliances.html)
7. [สัมภาระและกระเป๋า](https://www.aliexpress.com/category/1524/luggage-bags.html)
8. [ของเล่นและงานอดิเรก](https://www.aliexpress.com/category/26/toys-hobbies.html)
9. [กีฬาและนันทนาการ](https://www.aliexpress.com/category/18/sports-entertainment.html)

Requirements
------------

You need Python 3.x . [Install](https://www.python.org/downloads/)

firt you must install requirements.txt

    $ pip install - r requirements.txt

Here is example to scraping (Python 3):

```python
#list name main catagory in https://th.aliexpress.com
main_list = ["Apparel Accessories","Cellphones & Telecommunications","Consumer Electronics","Computer & Office",
"Education & Office Supplies","Home Appliances","Luggage & Bags","Toys & Hobbies","Sports & Entertainment"]
```
you cam see name main catagory in `maincatagory.json`

```python
def is_palindrome(s):
    # type: (str) -> bool
    return s == s[::-1]
```

- [ร่ม](https://th.aliexpress.com/wholesale?SearchText=ร่ม)
- [แก้วน้ำ](https://th.aliexpress.com/wholesale?SearchText=แก้วน้ำ)
- [แก้วน้ำ/กระบอกน้ำสแตนเลส](https://th.aliexpress.com/wholesale?SearchText=แก้วน้ำ%2Fกระบอกน้ำสแตนเลส)
- [พัดลมมือถือ](https://th.aliexpress.com/wholesale?SearchText=พัดลมมือถือ)
- [แฟลชไดร์ฟ](https://th.aliexpress.com/wholesale?SearchText=แฟลชไดร์ฟ)
- [แบตสำรอง](https://th.aliexpress.com/wholesale?SearchText=แบตสำรอง)

```python
import sys
sys.path.insert(1, './AliexpressScrap/searchproduct')
from app import *

AliexpressSearch(searchtext='แบตสำรอง')
```

```bash

application
├── AliexpressImage
│   └── Power bank
│
└── excel
|   └── power bank.xlsx
│
└── runcode here (exampleScrap.py)

```
Quick start
-----------





