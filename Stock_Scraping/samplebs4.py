from bs4 import BeautifulSoup
 
html = '<html><title>TITLE</title><body><div id="main">BODY</div></body></html>'
soup = BeautifulSoup(html, 'html.parser')
print(soup.title.text)
print(soup.find(id="main").text)