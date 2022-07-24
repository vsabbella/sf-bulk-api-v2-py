#!/usr/bin/env python3
from simple_salesforce import Salesforce
import requests
import json
import SFBulkJobv2Request
import csv
import configfilereader


class SFUtil:

    def sf():   
        session = requests.Session()
        session = requests.Session()
        sf = Salesforce(instance=configfilereader.getsfprop('sf.instance'), session_id=configfilereader.getsfprop('sf.sessionId'))
        
        SFBulkJobv2Request.callBulkFlowonSobject() 



SFUtil.sf()    