#!/usr/bin/env python3
import json
#returns field API Names seperated by commas suitable for pasting in a query.
def getWritableFields():
  with open("Product2Metadata.json") as prodMetadatafile:
    data = json.load(prodMetadatafile)
    print("type:",type(data["fields"]),len(data["fields"]) )
    product2Fields=data["fields"]
    writeable = list(filter(lambda f: f["calculated"]==False 
                     and f["name"] not in ["CreatedDate",
                                          "LastModifiedDate",
                                          "CreatedById",
                                          "SystemModstamp"],product2Fields))
    fieldAPINames = list(map(lambda x:x["name"],writeable))
    fields = ",".join(fieldAPINames)
    print('fieldAPINames',fields)

getWritableFields()    

