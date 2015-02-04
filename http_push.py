# simplejson==3.4.1
# requests==2.3.0

import requests
import simplejson as json

url = 'https://android.googleapis.com/gcm/send'
api_key = '{api_key}'
reg_ids = ['APA91bEWpSQjhPkiwHnYdhC1MbW_7F5V6_aTiQRyk9TlnCzL43QTTpv61WVCHvgf5qsjJLcjyUKp4pU9jmWRtwE9s0g2g3aL3k-7UZybWtjunw8Nkp9G_H1oeAI0to2mXo1M9n46_S-H09oSnuwuFGt5WmTV_q9dCfshW-QcRHX6r_vwZBECad8']

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + api_key
}

data = {
    'registration_ids': reg_ids,
    'data': {
        'price': 'el cacash'
    },
}

r = requests.post(url, data=json.dumps(data), headers=headers)
print json.dumps(r.json(), indent=4)
