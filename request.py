import requests
import json
import pandas as pd

url = 'https://cloud-run-forrest-regressor-ovgf2pkzmq-ey.a.run.app'

data = {"year":2020, "month":2}

j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)