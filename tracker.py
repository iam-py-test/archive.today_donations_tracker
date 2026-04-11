import requests, json, datetime

from bs4 import BeautifulSoup

URL = "https://liberapay.com/archiveis/donate"

req_liberapay = requests.get(URL)
soup = BeautifulSoup(req_liberapay.text, 'html.parser')

try:
    payment_data = json.loads(open("payment_data.json").read())
except:
    payment_data = {
        "liberapay": {}
    }

# there is a better way to do this, but I don't care
all_p = soup.find_all("p")
amount = 0
for p in all_p:
    try:
        if "archiveis currently receives" in p.get_text():
            amount = float(p.get_text().replace("archiveis currently receives €", "").replace(" per week.", ""))
            break
    except:
        pass

print(amount)            

date = datetime.datetime.now().strftime("%Y-%m-%d")

payment_data["liberapay"][date] = amount
try:
    paydata_out = open("payment_data.json", 'w')
    paydata_out.write(json.dumps(payment_data))
    paydata_out.close()
except:
    pass




