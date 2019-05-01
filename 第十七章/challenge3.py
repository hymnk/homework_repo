import re

string = "THe ghost that says boo haunts the loo"
m = re.findall(".oo", string, re.IGNORECASE)
print(m)