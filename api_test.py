from woocommerce import API

wcapi = API(
    url="http://example.com",
    consumer_key="ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    consumer_secret="cs_e44fc67bfd555f12d395cee4544016b5dcc95fa0",
    version="wc/v3"
)

r = wcapi.get("prodeucts")

import pprint
print(r.status_code)

print(r.json())
pprint.pprint(r.json())
