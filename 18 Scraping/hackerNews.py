# kada se doda robots.txt na kraju url-a izadje sta moze i ne moze da se skrepjuje
# Beautiful soup biblioteka za skrejpovanje
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.find_all('a'))
# print(soup.find('a'))  # nadje prvi item
# print(soup.select('#score_26538005'))  # za id
links = soup.select('.storylink')
subtext = soup.select('.subtext')  # . za klasu


def sort_stories_by_votes(hnlist):
    # da bi votes bili od najmanje ka najveceg
    # lambda zbog key iz dict, da zna po cemu da sortira dict
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    # enumerate jer imamo 2 liste, treba nam links i subtext
    for i, item in enumerate(links):
        title = links[i].getText()  # getText je od BSoup
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):  # ako postoji vote, ako nije 0
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:  # ako imaju vise od 100 points vesti tad ih dodamo
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# pprint da izgleda lepse u terminalu
pprint.pprint(create_custom_hn(links, subtext))
