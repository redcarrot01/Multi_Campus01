from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
from urllib.request import urlopen

url_head = "https://www.samsung.com/sec/support/model/"
url_tail = "/#downloads"


# 파일 읽어와서 딕셔너리 만들기
product_code_dic = {}
with open('product_code_dic.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split(': ')
        product_code_dic[int(key)] = value
# print(product_code_dic)


product_detail_page_link_dict = {}
for i in range(1, len(product_code_dic)+1):
    product_detail_page_link_dict[i] = url_head + product_code_dic[i]+url_tail
    
#print(product_detail_page_link_dict)



final_list = []

for key, product_code in product_code_dic.items():
    response = requests.get(product_detail_page_link_dict[key])
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
#     print(soup)
    product_dic= {}
    if len(soup.select('p.name'))==0:
        product_name = 0
        print(product_name)
        continue
    product_name = soup.select('p.name')[0].text
    print(product_name)    
#     if not soup.select('p.name') or soup.select('p.model'):
#         product_name = 0
#         product_code = 0
#     else:
#         product_name = soup.select('p.name')[0].text
#         product_code = soup.select('p.model')[0].text

        #     if soup.select('p.name') and soup.select('p.model'):
        #         product_name = soup.select('p.name')[0].text
        #         product_code = soup.select('p.model')[0].text
        #     else :
        #         product_name = '0'
        #         product_code = '0'
#     product_dic['product_detail_page_link'] = product_code_dic.values()
#     #     product_dic['product_manual_link'] = product_manual_link
#     product_dic['product_name'] = product_name
#     product_dic['product_code'] = product_code
    #     product_dic['product_image'] = product_image
    #     product_dic['category'] = 'printer'
#     final_list.append(product_dic)
# print(final_list[:5])
