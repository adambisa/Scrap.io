from bs4 import BeautifulSoup
import re
# Html source
html_source = '''
<div>
<p>child y</p>
<p class='price'>child g</p>
<p class='price-of-item'>child 31216515616,48432</p>
<p class='itemprice'>9</p>
</div>
'''

# Parsing
soup = BeautifulSoup(html_source, 'html.parser')

# find <p> with child 2 value
el = soup.find(string=re.compile('class=price'))

print(el)