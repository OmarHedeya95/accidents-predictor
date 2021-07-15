import requests
import json
import pandas as pd

url = 'http://0.0.0.0:5000/api/'

#data = [[2020, 10]]
data = {"year":2020, "month":10}

'''df = pd.DataFrame({
                "Year": 2020,
                "Month": 10

                },
                index = [0]      
            )'''

#data = [{"year": 2020}]

j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)