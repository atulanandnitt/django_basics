# from bs4 import BeautifulSoup as bs4
# import urllib
#
# url="https://www.westernunion.com/us/en/web/send-money/start"
#
# soup = bs4(urllib.urlopen(url))
# for link in soup.findAll('a'):
#         print (link.string)


from requests import get
url = 'https://www.westernunion.com/us/en/web/send-money/start'
response = get(url)

# print(response.text[:500])

# All available methods of receiving money
def rev_money(html_soup):
    for method in html_soup.find_all('span'):
        print(method)
        print(method.get())

    print("rev_money done 2")

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')
print(type(html_soup))
rev_money(html_soup)
# print(html_soup)


movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))
