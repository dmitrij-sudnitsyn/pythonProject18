import json
import requests

resp = requests.get(r'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')

st = '[{"ccy":"EUR","base_ccy":"UAH","buy":"40.00000","sale":"41.00000"},{"ccy":"USD","base_ccy":"UAH","buy":"39.50000","sale":"40.00000"}]'

temp=json.loads(resp.text)
# print(temp)
for el in temp:
    el.setdefault("bank","PB")
print(temp,type(temp))

json_obj = json.dumps(temp)
print(json_obj,type(json_obj))

    # print(el)