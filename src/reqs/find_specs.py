from src.reqs.get_table import get_spec_table
from src.data.spec_links import SPEC_LINKS
from src.data.table_beautifier import get_table


def check_snils_everywhere(snils: str) -> list[list[bool, str, str]]:
    data = []
    for spec in SPEC_LINKS.keys():
        raw = get_spec_table(spec)
        table, name = get_table(raw)
        snilses = [x[1] for x in table[1:]]
        if snils in snilses:
            data.append([True, name, spec])
        else:
            data.append([False, name, spec])
    return data
