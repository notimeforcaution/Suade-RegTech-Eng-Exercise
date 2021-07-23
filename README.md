# Trading Counterparty Default Risk (K-TCD) for a Reverse Repo transaction
### **Introduction**

This Python file aims to calculate the Trading Counterparty Default Risk (K-TCD) of a Reverse Repo Transaction as outlined in the "Investment Firm Regulation 2019/2033"
### **Requirements**

Additional Python Modules required:
- json

### **How to use the Python file**

To run the file, the JSON file containing the two legs of the Reverse Repo Transaction should be in the same directory as the Python file and be under the name "data.json". There is an in-built check to see if the uploaded file is data from a Reverse Repo transaction.

The output of the file will be a figure that represents the K-TCD of the uploaded Reverse Repo Transaction.

### **Calculating K-TCD**

According to Article 26 in the "Investment Firm Regulation"
K-TCD = Own Funds Requirement = alpha * EV * RF * CVA

Where:
alpha=1.2
EV= Exposure Value
RF = Risk Factor defined per counterparty type
CVA = Credit Value Adjustment which for SFTs is defined as 1 as written in Article 32

According to Article 27:

Exposure Value = Max(0;RC + PFE - C)

Where: 

PFE= Potential Future Exposure which for Reverse Repos is 0 as this is only defined for derivatives

C= Collateral - this depends on whether the security under the repo is a government or non-government bond ( I have assumed that the maturity is <=1 year)

#### Assumptions:

- The maturity of the security involved in the transction is <=1 year
- To work out the counterparty type I've assumed that if the customer type ends in "govt" it will have a risk factor of 1.6% - otherwise it will have a risk factor of 8%
