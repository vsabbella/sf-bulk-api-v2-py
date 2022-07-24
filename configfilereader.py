#!/usr/bin/env python3
import csv
import io
import configparser



def getSessionId(filepath='Product2.csv'):
    sessionId=''
    config = configparser.RawConfigParser()
    config.read('config.properties')
    sessionId=config.get('SFSection', 'sf.sessionId');
    return sessionId

def getsfprop(property='sf.username'):
    configprop=''
    config = configparser.RawConfigParser()
    config.read('config.properties')
    configprop=config.get('SFSection', property);
    return configprop    




print(getSessionId())



