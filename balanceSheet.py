import csv

f = open('DAL_annual_balance-sheet.csv')

csv_f = csv.reader(f)

l = []

for row in csv_f:
    l.append(row[1])

f.close()

date = "For the quater of " + l[0]
totalAsset = int(l[1].replace(",",""))
currentAsset = float(l[2].replace(",",""))
nonCurrentAsset = int(l[19].replace(",",""))
totalLia = int(l[35].replace(",",""))
currentLia = float(l[36].replace(",",""))
nonCurrentLia = int(l[51].replace(",",""))
totalEquity = float(l[63].replace(",",""))
retainedEarning = int(l[68].replace(",","")) 
AdditionalPaidIn = int(l[69].replace(",",""))
netDebt = int(l[82].replace(",",""))

def currRatio(asset, liability):

    currentRatio = float(currentAsset / currentLia)

    print("Current Ratio: " + str(currentRatio))

    if currentRatio >= 1:
        print("Good in paid off the current Liability")
    else:
        print("Bad in paid off the current Liability")

def printInfo(date, currentAsset, currentLiability, totalEquity):

    print(date)
    print("-----------------------------")
    print("Current Asset: " + str(currentAsset)) 
    print("Current Liability: " + str(currentLiability))
    print("Total Equity: " + str(totalEquity))

printInfo(date, currentAsset, currentLia, totalEquity)
print("-----------------------------")
currRatio(currentAsset, currentLia)




