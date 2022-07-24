from operator import add
import requests
import json
import csv
import csvPayloadGenerator
import sys
import configfilereader


def createJob(
    instanceUrl,
    sobject,
    operation,
    callBack,
    contentType="application/json",
    auth=configfilereader.getSessionId(),
    cookie="BrowserId=7EVQEn73EeyPdb0nI37yPw; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    
):
    url = instanceUrl

    payload = json.dumps({"object": sobject, "operation": operation,"externalIdFieldName" : "APTS_Ext_ID__c"})
    headers = {"Content-Type": contentType, "Authorization": auth, "Cookie": cookie}

    try:
     response = requests.request("POST", url, headers=headers, data=payload)
     callBack(response)
    except Exception as e:
      print('error occured')
      print(e)

      


def addBatchToJob(jobId,callBack):
    url =configfilereader.getsfprop('sf.batchurl')+jobId+"/batches"

    headers = {
        "Content-Type": "text/csv",
        "Authorization": configfilereader.getSessionId(),
        "Cookie": "BrowserId=7EVQEn73EeyPdb0nI37yPw; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1",
    }

  
    payloadstr = csvPayloadGenerator.generatePayLoadFromCSV()
    response = requests.request("PUT", url, headers=headers, data=payloadstr)
    #print(payLoadLines)
    callBack(jobId)

def closeBatch(jobId,callback):
  url = configfilereader.getsfprop('sf.batchurl')+jobId

  payload = json.dumps({
    "state": "UploadComplete"
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': configfilereader.getSessionId(),
    'Cookie': 'BrowserId=7EVQEn73EeyPdb0nI37yPw; CookieConsentPolicy=0:1; LSKey-c$CookieConsentPolicy=0:1'
  }

  response = requests.request("PATCH", url, headers=headers, data=payload)
  callback(json.loads(response.text))
  #print(response.text)    

def callBulkFlowonSobject():
  createJobURL = configfilereader.getsfprop('sf.batchurl')
  sobject = "Contact"
  operation = "insert"
  def addJobDataCallBack(jobId):
    print("addJobDataCallBack")
    closeBatch(jobId,closeBatchCallback)

  def closeBatchCallback(res):
    print('Close Batch Call Back')  
    print(res)  

  def createJobCallBack(response):
    print("Create Job CallBack")
    print(response.text)
    jsonres = json.loads(response.text)
    print(jsonres["id"])
    jobId= jsonres["id"]
    addBatchToJob(jobId,addJobDataCallBack)

  createJob(createJobURL,sobject,operation, createJobCallBack)


