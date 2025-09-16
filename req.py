import requests
# # r=requests.get("https://www.google.com")
# # print(r.text)
# url="https://jsonplaceholder.typicode.com/posts"
# data={
#     "title": 'ahmad',
#     "body": 'hello',
#     "userId": 1,
#   }
# headers={'Content-Type': 'application/json; charset=UTF-8',}
# res=requests.post(url, headers=headers ,json=data)
# print(res.text)


from bs4 import BeautifulSoup

url="https://jsonplaceholder.typicode.com/guide/"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'html.parser')
for heading in soup.find_all("h3"):
    print(heading.text)