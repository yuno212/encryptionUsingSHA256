import requests,pprint
from datetime import *

id = 'acct_1KMHJCAcN5kjnBXE'
apiKey = "sk_test_51KMHJCAcN5kjnBXEFd7UpFbgiPPY61KB7WdBOkbs7XruLXkCmIuvLwu6CSva4wTxlLcXax8ahvYxDys9SA5af7Wz00sVgsjyC9"


def getResponse():
  base = "https://api.stripe.com/v1/charges?limit=100"
  response = requests.get(base, auth=(apiKey,id))
  x = response.json()
  baseResponse = dict(x)
  return baseResponse['data']

data = getResponse()

def convertEpoch(epoch):
  x = datetime.fromtimestamp(epoch)
  return str(x)

def formattedDate(Set):
  response = [convertEpoch(i) for i in Set]
  return response

def getDate():
  response = []
  for i in range(len(data)):
    x = data[i]['created']
    response.append(x)
  return formattedDate(response)

def getTxId():
  response = []
  for i in range(len(data)):
    x = data[i]['payment_method']
    response.append(x)
  
  return response

def getId():
  response = []
  for i in range(len(data)):
    x = data[i]['id']
    response.append(x)
  
  return response

def getAmountSpent():
  response = []
  for i in range(len(data)):
    x = data[i]['amount']
    response.append(x/100)
  
  return response

def getEmail():
  response = []
  for i in range(len(data)):
    x = data[i]['billing_details']['email']
    response.append(x)
  
  return response

def getName():
  response = []
  for i in range(len(data)):
    x = data[i]['billing_details']['name']
    response.append(x)
  
  return response

def getSuccessfulPayments():
  response = []
  for i in range(len(data)):
    x = data[i]['paid']
    response.append(x)
  
  return response

def buildDB():
  defaultCurrency = 'USD'
  name = getName()
  emails = getEmail()
  txDates = getDate()
  amountSpent = getAmountSpent()
  ids = getId()
  txIds = getTxId()
  success = getSuccessfulPayments()
  response = []

  for n,e,d,a,i,t,s in zip(name,emails,txDates,amountSpent,ids,txIds,success):
    resp = {'customerName': n, 'customerEmail': e, 'txDate': d, f'amountSpent({defaultCurrency})': a, 'orderId': i, 'txId': t,'success': s}
    response.append(resp)
  
  for i in response:
    if i['success'] == False:
      response.remove(i)

  response = [{k: v for k, v in d.items() if k != 'success'} for d in response][::-1]

  return response


def getSpecificOrderDetails(index):
  db = buildDB()
  return db[index]

def showDb():
  db = buildDB()
  pprint.pprint(db)

showDb()