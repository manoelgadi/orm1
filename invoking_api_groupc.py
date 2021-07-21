# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:26:05 2020

@author: Prof. Manoel Gadi
"""



from urllib.request import urlopen
sourceCode = urlopen("http://groupc.pythonanywhere.com/to_json?nif=A82489451&json=YES").read()

import json
companies = json.loads(sourceCode)

print(companies[0]['company_name'])
print(companies[0]['CNAE'])
print("------------------")


for company in companies:
    print(company['company_name'])
    print(company['CNAE'])

print("------------------")

for company in companies:
    for key in company.keys():
        print("key={} : value={} ".format(key,company[key]))
    print("------------------")
        