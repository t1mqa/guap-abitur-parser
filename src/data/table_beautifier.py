import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_table(page: requests.Response) -> [list, str]:
    soup = BeautifulSoup(page.text, "html.parser")
    table_name = soup.find_all('h3')[2].text.split('"')[1]
    table = soup.find('table')
    table_rows = table.find_all('tr')
    parsed_table = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        parsed_table.append(row)
    return parsed_table, table_name


