import requests
from word_generator import word_generator
import pandas as pd

API_KEY = open("1. GOOGLE_SEARCH_API").read()
SEARCH_ENGINE_ID = open("2. SEARCH_ENGINE_ID").read()

prompt = str(input("Construa a persona: "))

word_list = word_generator(prompt)

table = {}

for keyword in word_list:
    url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'q': keyword,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID
    }

    response = requests.get(url, params=params)

    results = response.json()

    table[keyword] = [results['items'][link]['link'] for link in range(len(results['items'])) if 'items' in results]

df = pd.DataFrame.from_dict(table)

df.to_excel('table_generated.xlsx', index=False)