import requests
import json

customerId = '5ab6ed12322fa06b6779379a'
accountId = '5ab6ed11322fa06b67793799'
apiKey = 'd2671a7d6cfb6174201d13901da7d502'

#########################################################################################################################
# # Create a Savings Account
# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key=d2671a7d6cfb6174201d13901da7d502'.format(customerId,apiKey)
# payload = {
#   "type": "Credit Card",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000,
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
# url = 'http://api.reimaginebanking.com/accounts/5ab71acef0cec56abfa40445/bills?key=d2671a7d6cfb6174201d13901da7d502'
#
# payload = {
#   "status": "pending",
#   "payee": "Comcast",
#   "nickname": "string",
#   "payment_date": "2018-03-25",
#   "recurring_date": 1,
#   "payment_amount": 20
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
response = requests.get('http://api.reimaginebanking.com/accounts/5ab71acef0cec56abfa40445/bills?key=d2671a7d6cfb6174201d13901da7d502')
print(response.status_code)
print(response.text)
#########################################################################################################################
