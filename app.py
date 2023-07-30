import json
from src.reqs.find_specs import check_snils_everywhere


class App:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.TG_APIKEY = self.kwargs.get('TG_APIKEY')

    def start(self):
        snils = input('Enter your SNILS >> ')
        with open('specs.json', 'r', encoding='utf8') as specs:
            data = json.load(specs)
            if len(data) == 0:
                print('Checking all specs with your SNILS...')
                specsj = {}
                data = check_snils_everywhere(snils)
                for arr in data:
                    if arr[0]:
                        specsj[arr[1]] = arr[2]
                with open('specs.json', 'w', encoding='utf8') as specs:
                    json.dump(specsj, specs, indent=4, ensure_ascii=False)
                    print(f'Loaded specs for SNILS: {snils}')
            #	186-522-806 92



