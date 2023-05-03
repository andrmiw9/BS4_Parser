import requests
from bs4 import BeautifulSoup as bs
import re

# print('hello ')

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
result = soup.find_all('h3')
graph = {}


def lookforward2_h4(entry):
    result = entry.next_sibling.next_sibling
    if result:
        if result.name == 'h4':
            return True
    result = entry.next_sibling.next_sibling.next_sibling.next_sibling
    if result:
        if result.name == 'h4':
            return True


# def lookforward2_h3(entry):
#     result = entry.next_sibling.next_sibling
#     if result:
#         if result.name == 'h3':
#             return True
#     result = entry.next_sibling.next_sibling.next_sibling.next_sibling
#     if result:
#         if result.name == 'h3':
#             return True

class cell:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        pass


for entry in result:
    if entry.text == 'Summary':
        break

    print(entry)
    local_graph1 = {}
    graph[entry.text] = local_graph1

    if lookforward2_h4(entry):  # если среди 2 тегов снизу есть h4
        local_graph2 = {}
        local_graph1['Next_Level'] = local_graph2
        print(graph)
        # print('YEEEEP')
        condition = True
        t = entry.findNextSibling('h4')
        while condition:  # следующий тег это h4
            h4 = t
            print(h4)
            local_graph3 = {}
            local_graph2[h4.text] = local_graph3
            # print(h4.next_sibling)
            # print(h4.next_sibling.next_sibling)
            # print(h4.next_sibling.next_sibling.next_sibling)
            # print(h4.next_sibling.next_sibling.next_sibling.next_sibling)

            rtest = h4.findNextSiblings(limit=3)
            flag = False
            for e in rtest:
                # print(e.name)
                if e.name == 'h3':  # если среди 3 ближайших соседей снизу есть h3, то не трогаем такой h4
                    flag = True
                    break
            if flag:
                # add to big graph
                break

            ul = h4.findNextSibling('ul')
            alist = ul.findChildren('a')
            for tagA in alist:
                print(tagA['href'], tagA.text)
                local_graph3[tagA.text] = tagA['href']

            t = h4.findNextSibling('h4')
            condition = ul.next_sibling.next_sibling.name == 'h4'  # следующий тег это h4

            pass
        continue
    else:
        ul = entry.findNextSibling('ul')
        # print("ul:", ul)
        alist = ul.findChildren('a')
        # print(alist)
        for tagA in alist:
            print(tagA['href'], tagA.text)
            # url = tagA['href']
            local_graph1[tagA.text] = tagA['href']
        pass

    # print()
    # print(name.a['title'])
    # print("2:", entry.next_sibling.next_sibling)

    # lcl_res = requests.get(url)
    # lcl_res.encoding = 'utf-8'
    # sup = bs(lcl_res.text, 'html.parser')
    # res = sup.find('code', attrs={"class": " language-python"})

print(graph)
print(graph['Python Operators'])
