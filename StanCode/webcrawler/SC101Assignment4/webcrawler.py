"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find('tbody')

        male_total = 0
        female_total = 0

        for info in tags.find_all("tr"):
            tds = info.find_all("td")
            if len(tds) >= 5:
                male_number = int(tds[2].text.replace(",", ""))
                female_number = int(tds[4].text.replace(",", ""))
                male_total += male_number
                female_total += female_number

        print('male number: ' + str(male_total))
        print('female Number: ' + str(female_total))


if __name__ == '__main__':
    main()
