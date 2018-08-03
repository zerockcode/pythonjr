from bs4 import BeautifulSoup
import urllib.request

print("currency")


path = 'http://www.kita.net/exchangeRate_info/exchangeRate_info_list.jsp'

response = urllib.request.urlopen(path)

content = str(response.read(),"utf-8")

soup = BeautifulSoup(content, 'html.parser')


table = soup.find("table", {"class": "tableType1"})

trs = table.find_all("tr")


print(trs)

