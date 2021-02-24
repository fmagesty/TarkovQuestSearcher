import requests, bs4

questName = str(input()).title()
if ' ' in questName:
    questName.replace(' ', '_')
url = 'https://escapefromtarkov.gamepedia.com/' + str(questName)
print('Quest url: ' + url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
allpost = soup.select('p')
for post in allpost:
    text = post.getText('p')
    print(text)
