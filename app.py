from MyClass import MyClass
from flask import Flask
#from sf import sf
from simple_salesforce import Salesforce
import requests
import configfilereader

app = Flask(__name__)
myclass = MyClass.x


@app.route("/")
def index():
    #myclass()
    session = requests.Session()
    sf = Salesforce(instance=configfilereader.getsfprop('sf.instance'), session_id=configfilereader.getsfprop('sf.sessionId'))
    contact = sf.Contact.create({'LastName':'Smith','Email':'example@example.com'});
    print(contact['id'])
    return "Hello World!"