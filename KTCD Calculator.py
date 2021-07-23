
import json

#"a" represents the alpha in the "Own funds requirement" formula in Article 26 where alpha is defined to be 1.2
a=1.2
#"cva" represents the Credit Valuation Adjustment which is defined as 1 for SFTs in Article 32
cva=1

#Opening and reading JSON file - the JSON file be under the name "data.json" and saved in the same directory as this python file
with open('data.json','r') as f:
    data = json.load(f)

#Calculating the replacement cost figure as defined in Article 28 and used to calculate the exposure value in Article 27
def replacement_cost():
    global RC
    RC=int(data["data"][0]["balance"])*(-1)

#Calculating the exposure value as defined in Article 27
def exposure_value():
    global EV
    #Defining the bond type in the reverse repo transaction
    bond_type = (data["data"][1]["issuer"]["type"])
    #If the bond type ends in govt, the volatility adjustment repurchase transaction rate is taken for Debt securities issued by central governments or central banks whcich are <=1 year - otherwise the rate is taken for ebt securities issued by other entities for <=1 year
    if bond_type[-4:] == "govt":
        C = 0.00707
    else:
        C=0.01414
    #Calculating the exposure value as Article 27 defines - taking the higher of either 0 or the Replacement Cost minus Collateral (excludes PFE as derivatives are not involved)
    EV=max(0,RC-C)

#Calculating the risk factor as defined in Article 26 - the risk factor is a component of the "Own Funds Requirement" formula
def risk_factor():
    global RF
    #Define the customer type in the transaction
    customer_type=(data["data"][0]["customer"]["type"])
    #Assumed that if the customer type (counterparty) ends in govt, the risk factor will be 1.6% - otherwise it will be 8% (as was not sure how to define it what customers were credit institutions and investment firms)
    if customer_type[-4:] =="govt":
        RF=0.016
    else:
        RF=0.08

def ktcd():
    #Running the above functions
    replacement_cost()
    exposure_value()
    risk_factor()

    #"y" is calculating the "Own Funds Requirement" as defined in Article 26 - which is the figure used for the K-TCD
    y=(a*EV*RF*cva)

    return y

#Printing the K-TCD value
print(ktcd())

# Closing JSON file
f.close()