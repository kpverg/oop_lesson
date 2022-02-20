"""
0--->9999 0.0
10000--->19999 0.1
... --->0.2

"""
dicTaxScale={
    "scale1":0.00,
    "scale2":0.10,
    "scale3":0.20
}
incomeScale={
    "incomeLv1":10000,
    "incomeLv2":20000
}

income=19000
totalTax=0

if 0<income<=incomeScale["incomeLv1"]:
    totalTax=0
elif incomeScale["incomeLv1"]<income<=incomeScale["incomeLv2"]:
    totalTax=(income-incomeScale["incomeLv1"])*dicTaxScale["scale2"]
else:
    totalTax=incomeScale["incomeLv1"]*dicTaxScale["scale2"]+(income-
    incomeScale["incomeLv2"])*dicTaxScale["scale3"]

print(f"Το συνολικό ύψος του φόρου είναι : {totalTax}")




