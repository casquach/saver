import requests
import json

customerId = '5ab6ed12322fa06b6779379a'
apiKey = 'd2671a7d6cfb6174201d13901da7d502'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key=d2671a7d6cfb6174201d13901da7d502'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')
