#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
README:
    This challenge was programmed with all functions we learned past classes. I didn't use another libraries
    because I wanted help to enforce knowledge. I hope this will be helpful to you.
    
    Summary:
        1.- Declare libraries
        2.- Functions:
            max_profit(dataset) = Get max value of a dataset
            min_profit(dataset) = Get min value of a dataset
            avg_profit(dataset) = Get average value of a dataset
            total_profit(dataset) = Get sum of profit of a dataset
            financial_report_to_textfile(report_dict) = Send results to txt file. 
                Warning: Make sure resources_directory is set with your directory. If you want to save the txt in the same path of your main.py, leave resources_directory blank
            financial_report() = Retreive all data and print out results. At the same time calls financial_report_to_textfile(report_dict)                
"""
import os
import csv

#Change this variables according to your directory structure
resources_directory = 'Resources'
output_directory = 'Output'
csv_file_to_open = 'budget_data.csv'
csv_file_to_create = 'financial_report.txt'

#Assign path of csv file
path_csv_file = os.path.join(resources_directory, csv_file_to_open)
#Warning: To avoid hours of searching, the Financial report must be .txt instead of .csv due to csv = comma-separated-values
path_write_csv_file = os.path.join(output_directory, csv_file_to_create)

def max_profit(dataset):
    #Get Greates Increase Profit.
    #It expect a list
    #It will return a list with Month and Greates Increase Profit
    result = []
    month_profit = ''
    top_profit = 0
    
    for profit_row in range(len(dataset)-1):
        last_profit = float(dataset[profit_row][1])
        current_profit = float(dataset[profit_row+1][1])
        max_current_profit = current_profit - last_profit
        if max_current_profit > top_profit:
            top_profit = max_current_profit
            month_profit = str(dataset[profit_row+1][0])
                      
    result.append(month_profit)
    result.append(round(top_profit))
        
    return result

def min_profit(dataset):
    #Get Greates Decrease Profit.
    #It will return a list with Month and Greates Decrease Profit
    result = []
    month_profit = ''
    top_profit = 0
    
    for profit_row in range(len(dataset)-1):
        last_profit = float(dataset[profit_row][1])
        current_profit = float(dataset[profit_row+1][1])
        min_current_profit = current_profit - last_profit
        if min_current_profit < top_profit:
            top_profit = min_current_profit
            month_profit = str(dataset[profit_row+1][0])
                      
    result.append(month_profit)
    result.append(round(top_profit))
        
    return result
    
def avg_profit(dataset): 
    #It will return Average Change Profit.
    result = 0
    top_profit = 0
    
    for profit_row in range(len(dataset)-1):
        last_profit = float(dataset[profit_row][1])
        current_profit = float(dataset[profit_row+1][1])
        avg_current_profit = current_profit - last_profit
        top_profit += avg_current_profit
    
    result = round(top_profit / (len(dataset)-1),2)
        
    return result     

def total_profit(dataset):
    #It will return total profit
    result = 0
    
    for profit_row in dataset: 
        result += int(profit_row[1])
    
    return result
    
def financial_report_to_textfile(report_dict):
    #It will return a text file with Financial Analysis
    
    #Open file using 'w' = write.
    with open(path_write_csv_file, 'w') as financial_report_file:
        
        #At the final of each statement you'll see a "\n". Recall, it's used to emulate <enter> key
        financial_report_file.write(f"{report_dict['header']}\n")
        financial_report_file.write(f"{report_dict['labels'][0]} {report_dict['results'][0]}\n")
        financial_report_file.write(f"{report_dict['labels'][1]} {report_dict['results'][1]}\n")
        financial_report_file.write(f"{report_dict['labels'][2]} {report_dict['results'][2]}\n")
        financial_report_file.write(f"{report_dict['labels'][3]} {report_dict['results'][3][0]} (${report_dict['results'][3][1]})\n")
        financial_report_file.write(f"{report_dict['labels'][4]} {report_dict['results'][4][0]} (${report_dict['results'][4][1]})\n")
               
def financial_report():
    #It will build a report through a dict and list.
    report_dict = {
            'header': 'Financial Analysis\n------------------------------',
            'labels': ['Total Months:', 'Total: $', 'Average Change: $', 'Greatest Increase in Profits:', 'Greatest Decrease in Profits:'],
            'results': [],
            }
    
    #Open file using 'r' = readonly. It's a best practice to avoid damage a file
    with open(path_csv_file, 'r') as budget_data_obj:
        budget_data_ds = csv.reader(budget_data_obj, delimiter=',')
        #Remove headers to avoid misscounting
        next(budget_data_ds, None)
        #Set variables
        #budget_data_list is a -list comprehension- to get dataset ready
        #budget_data_list will be useful to activate other functions and save computer resources
        budget_data_list = [month for month in budget_data_ds]
        #Get total months
        get_total_months = len(budget_data_list)
        #Get total profit
        get_total_profit = total_profit(budget_data_list)
        #Add results to report dict
        #As we can see, every result is obtained through functions
        report_dict['results']= [
                get_total_months,
                get_total_profit,
                avg_profit(budget_data_list),
                max_profit(budget_data_list),
                min_profit(budget_data_list)]
        
        #Print out Financial Analysis
        print(f"{report_dict['header']}")
        print(f"{report_dict['labels'][0]} {report_dict['results'][0]}")
        print(f"{report_dict['labels'][1]} {report_dict['results'][1]}")
        print(f"{report_dict['labels'][2]} {report_dict['results'][2]}")
        print(f"{report_dict['labels'][3]} {report_dict['results'][3][0]} (${report_dict['results'][3][1]})")
        print(f"{report_dict['labels'][4]} {report_dict['results'][4][0]} (${report_dict['results'][4][1]})")
        
        #Save report to txt file
        financial_report_to_textfile(report_dict)
        
#Start program
financial_report()