#!/usr/bin/env python3
import csv
import io

#contactwithAccount.csv
def generatePayLoadFromCSV(filepath='./contactwithAccount.csv'):
    payload=[]
    with open(filepath, newline='',encoding='utf-8-sig') as csvfile:
        content = csvfile.read().replace('"', '\\"')
        csvreader = csv.reader(io.StringIO(content), delimiter=',', doublequote=True, quoting=csv.QUOTE_ALL, escapechar='\\',quotechar='"')
        for row in csvreader:
         #print(row)   
         payload.append(",".join(row))     
    #LF, CLRL may be causing the issue - try matching to LF instead of \n     
    payloadstr='\n'.join(payload)
    
    return payloadstr.encode('utf-8')


def generatePayload2():
 output = io.StringIO()

generatePayLoadFromCSV()


