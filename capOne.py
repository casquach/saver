import requests
import json

customerId = '5ab6ed12322fa06b6779379a'
customerIdLaBadie = '5ab6ed12322fa06b6779379b'
accountId = '5ab6ed11322fa06b67793799'
apiKey = 'd2671a7d6cfb6174201d13901da7d502'

#########################################################################################################################
# # Create a Savings Account
# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key=d2671a7d6cfb6174201d13901da7d502'.format(customerIdLaBadie,apiKey)
# payload = {
#   "type": "Credit Card",
#   "nickname": "The Badie",
#   "rewards": 100000000,
#   "balance": 100000000,
# }
# # post : to submit data to be processed to the server
# # get : to request data from the server
# response = requests.post(
# 	url,
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)
# print(response.status_code)
# if response.status_code == 201:
# 	print('account created')

#########################################################################################################################
# # Create a bill
# url = 'http://api.reimaginebanking.com/accounts/5ab7c94ef0cec56abfa4047d/bills?key=d2671a7d6cfb6174201d13901da7d502'
#
# payload = {
#   "status": "pending",
#   "payee": "American Horses Association",
#   "nickname": "string",
#   "payment_date": "2029-03-25",
#   "recurring_date": 1,
#   "payment_amount": 20000
# }
# # post : to submit data to be processed to the server
# # get : to request data from the server
# response = requests.post(
# 	url,
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)
# print(response.status_code)

#########################################################################################################################
# #Gets bill from account id

# post : to submit data to be processed to the server
# get : to request data from the server
response = requests.get('http://api.reimaginebanking.com/accounts/5ab7c94ef0cec56abfa4047d/bills?key=d2671a7d6cfb6174201d13901da7d502')
print(response.status_code)
print(response.text)
#########################################################################################################################
