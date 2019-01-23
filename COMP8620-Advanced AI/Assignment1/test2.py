import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=False)
browser.open('http://www.ohchr.org/EN/UDHR/Pages/SearchByLang.aspx')

# Search for Porcupine Tree
form = browser.get_form()
# for key in form.keys():
#     print(key)
#print(form)                # <RoboForm q=>
form['ctl00$PlaceHolderMain$usrUDHRSearchByLangID$ddlUDHRSearchByID'].value = "(Title LIKE 'E*') OR (Title LIKE 'F*') OR (Title LIKE 'G*') OR (Title LIKE 'H*')"
# form['ctl00$PlaceHolderMain$usrUDHRSearchByLangID$ImgbtnUDHRSearchByID'].value = "(Title LIKE 'E*') OR (Title LIKE 'F*') OR (Title LIKE 'G*') OR (Title LIKE 'H*')"
browser.submit_form(form)
print(browser.find_all('a', id = re.compile('^ctl00')))
# langs = browser.find_all("a", id = re.compile('^ctl00'))
# for lang in langs:
#     print(lang)
#
# # Look up the first song
# songs = browser.select('.song_link')
# browser.follow_link(songs[0])
# lyrics = browser.select('.lyrics')
# lyrics[0].text      # \nHear the sound of music ...
#
# # Back to results page
# browser.back()
#
# # Look up my favorite song
# song_link = browser.get_link('trains')
# browser.follow_link(song_link)
#
# # Can also search HTML using regex patterns
# lyrics = browser.find(class_=re.compile(r'\blyrics\b'))
# lyrics.text         # \nTrain set and match spied under the blind...
