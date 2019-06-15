import pandas as pd

df = pd.read_csv("budget_data.csv")


#print(df.head())
#print(df.iloc[1]) #One single index
#print(df.loc[[3,8]]) #More than 1 index
#print(df.info())

totalMonths = len(df['Date'])       
totalProfitLosses = df['Profit/Losses'].sum()
avgProfitLosses = df['Profit/Losses'].mean()
maxProfit = df['Profit/Losses'].max()
minProfit = df['Profit/Losses'].min()

maxProfitDF = df[(df['Profit/Losses']==maxProfit)]

print(maxProfitDF['Date'])
print(maxProfitDF['Profit/Losses'])

    
def finalReport(p_totalMonths, p_totalProfitLosses, p_avgProfitLosses, p_maxProfit, p_minProfit):
    print("Financial Analysis\n----------------------------")
    print(f"Total Months: {p_totalMonths}")
    print(f"Total: ${p_totalProfitLosses}")
    print(f"Total: ${avgProfitLosses}")
    print(f"Greatest Increase in Profits: ${p_maxProfit}")
    print(f"Greatest Decrease in Profits: ${p_minProfit}")
    
    
    
finalReport(totalMonths, totalProfitLosses, avgProfitLosses, maxProfit, minProfit)