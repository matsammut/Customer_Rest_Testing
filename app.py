from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime,timedelta

app = Flask(__name__)

file_path = "CustomerData.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()

headers = lines[0].strip().split('|')
data_lines = [line.strip().split('|') for line in lines[1:]]

date = str(datetime.now())
date = date[slice(0,10)]

# @app.route('/customers/statistics', methods=['GET'])
def GetCustomers(grouping = 'Country', ageVerified = 'Yes', IdentityExpired = 'Yes'):
    # if request.method == 'GET':
    #     grouping = request.args.get('grouping', default=None)
    #     ageVerified = request.args.get('AgeVerified', default=None)
    #     identityExpired = request.args.get('IdentityExpired', default=None)
    if grouping is not None:
        if grouping == 'Country' or grouping == 'CustomerType':
            pass
        else:
            return 'Error: Invalid grouping provided',404
    else:
        return 'Error: No grouping provided',404

    grouped_data = {}
    count = 0
    if grouping == 'Country':
        for data in data_lines:
            if ageVerified is not None and ageVerified == 'Yes':
                if data[4]=='0':
                    continue
            if IdentityExpired is not None and IdentityExpired == 'Yes':
                if data[5] < date:
                    continue
            country = data[3]
            if country in grouped_data:
                grouped_data[country].append(data)
            else:
                grouped_data[country] = [data]

    for key in grouped_data:
        count = len(grouped_data[key])
        sum = 0
        for sets in grouped_data[key]:
            sum += int(sets[7])
        avg = sum/count
        print(key)
        print(grouped_data[key])
        print(count)
        print(avg)
        print('\n')
            # count = len(grouped_data)
            # avg = 0
            # for group in grouped_data:
            #     avg += 
        

GetCustomers()