from bs4 import BeautifulSoup
import re
import requests

session = requests.Session()
langDic = {}
params = {'ctl00$PlaceHolderMain$usrUDHRSearchByLangID$ImgbtnUDHRSearchByID': "(Title LIKE 'E*') OR (Title LIKE 'F*') OR (Title LIKE 'G*') OR (Title LIKE 'H*')"}
r = session.post("http://www.ohchr.org/CH/UDHR/Pages/SearchByLang.aspx", data=params)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
langs = soup.find_all("a", id = re.compile('ctl00_PlaceHolderMain_usrUDHRSearchByLangID_dataListbyLangID_ct'))
i = 0
for lang in langs:
    if lang.has_attr('href'):
        print(lang['href'].split('=')[1])
