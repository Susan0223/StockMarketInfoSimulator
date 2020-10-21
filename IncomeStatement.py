import csv

f = open('AAPL_annual_financials.csv')

csv_f = csv.reader(f)

l = []

for row in csv_f:
    l.append(row[1])

f.close()

date = "At Trailing 12 month"
TotalRevenue = int(l[1].replace(",",""))
GrossProfit = float(l[4].replace(",",""))
OperatingExpenses = int(l[5].replace(",",""))
NetIncome = int(l[26].replace(",",""))

def printInfo(date, TotalRevenue, GrossProfit, OperatingExpenses, NetIncome):

    print(date)
    print("-----------------------------")
    print("Total Revenue: " + str(TotalRevenue)) 
    print("Gross Profit: " + str(GrossProfit))
    print("Operating Expenses: " + str(OperatingExpenses))

printInfo(date, TotalRevenue, GrossProfit, OperatingExpenses, NetIncome)
