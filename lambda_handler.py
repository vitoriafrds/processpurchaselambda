from __future__ import print_function

import json
import urllib
import boto3
import datetime

print('Iniciando processamento da função..')

def process_purchase(message, context):
    #Exemplo de Input:
    #TransactionType: 'PURCHASE'

    print("Request da Step Function: ")
    print(message)

    response = {}
    response['TransactionType'] = message['TransactionType']
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    return response
