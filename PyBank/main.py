#Best practices tip: Declare modules on top
import pandas as pd

#Best practices tip: Naming in variables, function, methods, packages, modiles: lower_case_with_underscores
def report_financial_records():
    #Pandas reader inside a function to improve performance. Recommended whether you're going to use the csv after a function call
    df = pd.read_csv("Resources/budget_data.csv")
    
    #Count total months using len()
    count_months = len(df['Date'])
    #Sum total profit using sum()
    sum_profit_losses = df['Profit/Losses'].sum()
    #Average total profit using mean()
    avg_profit_losses = df['Profit/Losses'].mean()
    #Get greates increase using max()
    greatest_increase = df['Profit/Losses'].max()
    #Get greatest increase month name using loc and iloc
    greates_increase_month_name = df.loc[df['Profit/Losses']==greatest_increase, 'Date'].iloc[0]
    #Get greatest decrease using min()
    greatest_decrease = df['Profit/Losses'].min()
    #Get greatest decrease month name using loc and iloc
    greatest_decrease_month_name = df.loc[df['Profit/Losses']==greatest_decrease, 'Date'].iloc[0]
    
    #Print Financial Report
    print("Financial Analysis\n----------------------------")
    print(f"Total Months: {count_months}")
    print(f"Total: ${sum_profit_losses}")
    print(f"Total: ${avg_profit_losses}")
    print(f"Greatest Increase in Profits: {greates_increase_month_name} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month_name} ${greatest_decrease}")
    
#Call function       
report_financial_records()