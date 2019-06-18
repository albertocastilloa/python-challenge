#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:29:58 2019

@author: albertocastillo - https://github.com/albertocastilloa/python-challenge
"""
import os
import csv

path_csv_file = os.path.join('Resources', 'budget_data.csv')
#Warning: To avoid hours of searching, the Financial report must be .txt instead of csv due to csv = comma-separated-values
path_write_csv_file = os.path.join('Resources', 'financial_report.txt')

def total_avg_profit(dataset, dataset_rows):
    #Calculate total profit and avg profit
    #It will return a list with Sum of profit and avg profit
    result = [0,0]
    #Sum profit
    for i in dataset: 
        result[0] += int(i[1])
    #Get average profit
    result[1] = result[0] / dataset_rows
    #Return sum of proft and avg profit at the same time
    return result

def max_min_profit(dataset, type_profit_value):
    #Get Max or Min Profit.
    #type_profit_value = boolean
    #type_profit_value = 1 for Max profit value. 
    #type_profit_value = 0 Min profit value
    #It will return a list of Month and Profit
    result = [0,0]
    
    if type_profit_value:
        for i in dataset:
            if int(i[1]) > int(result[1]):
                result = []
                result.append(i[0])
                result.append(i[1])
    else:
        for i in dataset:
            if int(i[1]) < int(result[1]):
                result = []
                result.append(i[0])
                result.append(i[1])
        
    return result
    
def financial_report_to_textfile(report_dict):
    #It will return a text file with Financial Analysis
    with open(path_write_csv_file, 'w') as financial_report_file:
        
        #At the final of each statement you'll see a "\n". Recall, it's used to emulate <enter> key
        financial_report_file.write(f"{report_dict['header']}\n")
        financial_report_file.write(f"{report_dict['labels'][0]} {report_dict['results'][0]}\n")
        financial_report_file.write(f"{report_dict['labels'][1]} {report_dict['results'][1][0]}\n")
        financial_report_file.write(f"{report_dict['labels'][2]} {report_dict['results'][1][1]:.2f}\n")
        financial_report_file.write(f"{report_dict['labels'][3]} {report_dict['results'][2][0]} (${report_dict['results'][2][1]})\n")
        financial_report_file.write(f"{report_dict['labels'][4]} {report_dict['results'][3][0]} (${report_dict['results'][3][1]})\n")
        
               
def financial_report():
    #This function will build report through a dict and list.

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
        total_months = len(budget_data_list)
        #Add results to report dict
        report_dict['results']= [total_months, 
                          total_avg_profit(budget_data_list, total_months),
                          max_min_profit(budget_data_list, 1),
                          max_min_profit(budget_data_list, 0)
                          ]
        
        print(report_dict['header'])
        print(f"{report_dict['labels'][0]} {report_dict['results'][0]}")
        print(f"{report_dict['labels'][1]} {report_dict['results'][1][0]}")
        print(f"{report_dict['labels'][2]} {report_dict['results'][1][1]:.2f}")
        print(f"{report_dict['labels'][3]} {report_dict['results'][2][0]} (${report_dict['results'][2][1]})")
        print(f"{report_dict['labels'][4]} {report_dict['results'][3][0]} (${report_dict['results'][3][1]})")
        
        financial_report_to_textfile(report_dict)

financial_report()