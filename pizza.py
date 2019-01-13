import datetime

import bs4
import dateutil.parser
import requests


def arizmendi_calendar():
    response = requests.get('http://arizmendi-valencia.squarespace.com/pizza')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    div = soup.find_all('div', attrs={'class': 'sqs-block-content'})[3]
    tags = [p.text for p in div.find_all('p')]

    calendar = {}
    for date, pizza in zip(tags[:-1], tags[1:]):
        try:
            calendar[dateutil.parser.parse(date).date()] = pizza
        except ValueError:
            pass

    return calendar


def main():
    today = datetime.datetime.now().date()
    print(f"Today's pizza is {arizmendi_calendar()[today]}")


if __name__ == '__main__':
    main()
