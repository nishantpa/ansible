import json


with open('/Users/nishantpatel/Development/ansible/logs/log.json') as data_file:    
    data = json.load(data_file)

print data["ec2"]