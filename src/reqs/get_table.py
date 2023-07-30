import requests
from src.data.spec_links import SPEC_LINKS


def get_spec_table(spec) -> requests.Response:
    link = SPEC_LINKS.get(spec)
    page = requests.get(link)
    return page


get_spec_table('27.03.05')
