#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
README:
    This challenge was programmed with all functions we learned past classes. I did not use another libraries
    because I wanted help to reinforce knowledge. I hope this will be helpful to you.
    
    Summary:
        1.- Declare libraries
        2.- Functions:
            profile_per_candidate(dataset, total_votes) = Get name, votes, percentage and whether is a winner or not
            min_profit(dataset) = Get min value of a dataset
            avg_profit(dataset) = Get average value of a dataset
            total_profit(dataset) = Get sum of profit of a dataset
            poll_results_to_file(election_results) = Send results to txt file. 
    
"""

import os
import csv

resources_directory = 'Resources'
output_directory = 'Output'
csv_file_to_open = 'election_data.csv'
csv_file_to_create = 'election_results.txt'

path_election_data_file_csv = os.path.join(resources_directory, csv_file_to_open)
path_election_data_file_txt = os.path.join(output_directory, csv_file_to_create)


def poll_results_to_file(election_results):
    #It will send out the results to a txt file
    with open(path_election_data_file_txt, 'w') as election_results_txt_file:
        election_results_txt_file.write(f"{election_results['headers'][0]}\n{election_results['headers'][1]}\n")
        election_results_txt_file.write(f"{election_results['labels'][0]}: {election_results['votes']}\n")
        election_results_txt_file.write(f"{election_results['headers'][1]}\n")
        for candidate in election_results['candidates']['profile']:
            election_results_txt_file.write(f"{candidate}: {election_results['candidates']['profile'][candidate][1]:.3f}% ({election_results['candidates']['profile'][candidate][0]})\n")
        election_results_txt_file.write(f"{election_results['headers'][1]}\n")
        for winner in election_results['candidates']['profile']:
            if int(election_results['candidates']['profile'][winner][2]) == 1:
                election_results_txt_file.write(f"{election_results['labels'][1]}: {winner}")
                break
            

def profile_per_candidate(dataset, total_votes):
    #It will send back name, votes, percentage and whether is a winner or not.
    #winner = 1
    candidate_dict = {'profile':{}}
    
    #Find candidate name
    for candidate in dataset:    
        if candidate[2] not in candidate_dict.items():
            candidate_dict['profile'][candidate[2]] = 0
    
    #Count votes per candidate
    votes_counter = 0
    for candidate_name in candidate_dict['profile']:
        for rows in dataset:
            if rows[2] == candidate_name:
                votes_counter +=1
                candidate_dict['profile'][candidate_name] = [votes_counter]
                candidate_dict['profile'][candidate_name].append(100 * votes_counter/total_votes)
                candidate_dict['profile'][candidate_name].append(0)
        votes_counter = 0
    
    #Find candidate winner
    votes_winner = 0
    for i in candidate_dict['profile']:
        if candidate_dict['profile'][i][0] > votes_winner:
            votes_winner = candidate_dict['profile'][i][0]
            candidate_dict['profile'][i][2] = 1
        else:
            candidate_dict['profile'][i][2] = 0
    return candidate_dict

def poll_results():
    #Dict where all data will be allocated
    election_results = {
            'headers': ['Election Results', '----------------------'],
            'votes': 0,
            'labels': ['Total Votes', 'Winner'],
            'candidates': {}
            }
    
    with open(path_election_data_file_csv, 'r') as election_data_file:
        election_data_ds = csv.reader(election_data_file, delimiter=',')
        next(election_data_ds)
        
        #Comprehension list of elections.
        election_data_list = [election for election in election_data_ds]
        
        #Get total votes, no matter the candidate.
        election_results['votes'] = len(election_data_list)
        #Get profile for each candidate
        election_results['candidates'] = profile_per_candidate(election_data_list, election_results['votes'])
        
        #Print out Election Results
        print(f"{election_results['headers'][0]}\n{election_results['headers'][1]}")
        print(f"{election_results['labels'][0]}: {election_results['votes']}")
        print(f"{election_results['headers'][1]}")
        for candidate in election_results['candidates']['profile']:
            print(f"{candidate}: {election_results['candidates']['profile'][candidate][1]:.3f}% ({election_results['candidates']['profile'][candidate][0]})")
        print(f"{election_results['headers'][1]}")
        for winner in election_results['candidates']['profile']:
            if int(election_results['candidates']['profile'][winner][2]) == 1:
                print(f"{election_results['labels'][1]}: {winner}")
                break
            
        #Send results to a txt file
        poll_results_to_file(election_results)

#Start program
poll_results()