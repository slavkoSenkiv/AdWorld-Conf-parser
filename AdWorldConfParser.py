import requests, bs4, openpyxl

doc = open('Adworld.txt', 'w')
wb = openpyxl.Workbook()
sheet = wb.active
url = 'https://adworld.online/app/schedule?type=SCHEDULE'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# title
title = soup.select('.agenda-item-content-title')
print(title)
print(title[0].getText())

# tag
# speaker
# description

"""for i in range(5): # (len(title)):
    print(i, title[i].getText())
    doc.write(title[i].getText())"""

doc.close()
wb.save('AdWorld.xlsx')