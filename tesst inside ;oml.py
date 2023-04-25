from bs4 import BeautifulSoup

html = """
<h3 class='item-title'><a href="dement">link1</a></h3>
<h3><a href="cigan">link2</a></h3>
<h3><a href="/notebook-apple-macbook-air-13-m1-256-gb-gold-sk-mgnd3sl-a.html">link3</a></h3>
<h3><a href="retard">link4</a></h3>
"""

soup=BeautifulSoup(html,'html.parser')
names = soup.find_all('h3')

for a in names:
    print(a.a.get('href'))
