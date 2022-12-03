"""
File: webcrawler.py
Name: Norah Liao
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
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        male_number = 0
        female_number = 0

        # get data
        tags = soup.tbody.text
        data = tags.split()

        # get rank 1-200 data
        for i in range(200*5):
            # Males number
            if i % 5 == 2:
                # print(int(data[i].replace(',', '')))
                male_number += int(data[i].replace(',', ''))
            # Females number
            if i % 5 == 4:
                female_number += int(data[i].replace(',', ''))

        print(f'Male Number: {male_number}')
        print(f'Female Number: {female_number}')


if __name__ == '__main__':
    main()
