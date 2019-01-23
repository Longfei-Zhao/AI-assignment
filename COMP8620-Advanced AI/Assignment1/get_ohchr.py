from bs4 import BeautifulSoup
import requests
import re

langDic = {}
r = requests.get("http://www.ohchr.org/EN/UDHR/Pages/SearchByLang.aspx")
data = r.text
soup = BeautifulSoup(data, 'html.parser')
langs = soup.find_all("a", id = re.compile('^ctl00_PlaceHolderMain_usrUDHRSearchByLangID_dataListbyLangID_ct'))
i = 0
for lang in langs:
    if lang.has_attr('href'):
        langDic[lang.string.split('/')[-1]] = lang['href'].split('=')[1]

url = 'http://www.ohchr.org/CH/UDHR/Pages/Language.aspx?LangID='

for name, langurl in langDic.items():
    r = requests.get(url + langurl)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    spans = soup.select('#DeltaPlaceHolderMain > div:nth-of-type(2) > div:nth-of-type(1) > span')
    with open('ohchr2/' + name, 'w') as f:
        span = spans[-1]
        f.write(' '.join(
            filter(None,
                map(lambda x:x.strip(), span.findAll(text=True)))))
        # for p in span.children:
        #     if p.string:
        #         f.write(p.string)
        #     else:
        #         for c in p.children:
        #             if c.string and c.string.strip():
        #                 f.write(c.string.strip())
