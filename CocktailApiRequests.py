import requests
import json
import sqlite3
from win10toast import ToastNotifier
api_key = '1'
url = f'https://www.thecocktaildb.com/api/json/v1/{api_key}/search.php?s=margarita'
r = requests.get(url)
print(r.headers)
print(r.encoding)
print(r.text)
cocktails = r.json()
res_structured = json.dumps(cocktails, indent=4)
instructions = cocktails['drinks'][0]['strInstructions']
print(instructions)
photo_link = cocktails['drinks'][0]['strDrinkThumb']
print(photo_link)
drink_type = cocktails['drinks'][0]['strAlcoholic']
print(drink_type)

conn = sqlite3.connect('cocktails.db')
cursor = conn.cursor()

create = '''
    CREATE TABLE IF NOT EXISTS cocktail_data (
        instructions TEXT,
        photo_link TEXT,
        drink_type TEXT
    )'''

cursor.execute(create)

insert = '''INSERT INTO cocktail_data (instructions, photo_link, drink_type) VALUES (?, ?, ?)'''

cursor.execute(insert,(instructions, photo_link, drink_type))

conn.commit()
conn.close()

toaster = ToastNotifier()
toaster.show_toast("Cocktail Notification", "New cocktail added!", duration=10)

# print(res_structured)
# print(r)


