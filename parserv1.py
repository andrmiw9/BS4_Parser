import requests
from bs4 import BeautifulSoup as bs
import re

# print('hello ')

TARGET = 'h3'
URL_TEMPLATE = "https://pythonexamples.org/python-basic-examples/"
r = requests.get(URL_TEMPLATE)
# print(r.encoding)
r.encoding = 'utf-8'
# print(r.encoding)
print('Status code:', r.status_code)
# print(r.text)
soup = bs(r.text, "html.parser")
print(soup.original_encoding)
# print(soup)
# vacancies_names = soup.find_all('a', string=re.compile('.*Python'))
result = soup.find_all(TARGET)
graph = []

print('Result:', result)

for entry in result:
    print('Entry:', entry)

    pass

# for entry in result:
#     deep = 1
#     listpars = []
#
#     print(entry)
#     if lookforward2_h4(entry):  # если среди 2 тегов снизу есть h4
#         print('YEEEEP')
#         deep = 2
#         condition = True
#         t = entry.findNextSibling('h4')
#         while condition:
#             h4 = t
#             print(h4)
#             ul = h4.findNextSibling('ul')
#             alist = ul.findChildren('a')
#             for tagA in alist:
#                 print(tagA['href'], tagA.text)
#                 url = tagA['href']
#
#             # print(ul.next_sibling)
#             # print(ul.next_sibling.next_sibling)
#             # print(ul.next_sibling.next_sibling.next_sibling)
#             # print(ul.next_sibling.next_sibling.next_sibling.next_sibling)
#             t = h4.findNextSibling('h4')
#             condition = ul.next_sibling.next_sibling.name == 'h4'
#
#             pass
#         continue
#
#     # print()
#     # print(name.a['title'])
#     # print("2:", entry.next_sibling.next_sibling)
#     ul = entry.findNextSibling('ul')
#     # print("ul:", ul)
#     alist = ul.findChildren('a')
#     # print(alist)
#     for tagA in alist:
#         print(tagA['href'], tagA.text)
#         url = tagA['href']
#         # lcl_res = requests.get(url)
#         # lcl_res.encoding = 'utf-8'
#         # sup = bs(lcl_res.text, 'html.parser')
#         # res = sup.find('code', attrs={"class": " language-python"})
