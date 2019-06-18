#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:15:50 2019

@author: albertocastillo
"""

import os
import csv

path_election_data_file = os.path.join('Resources', 'election_data_backup.csv')

def profile_per_candidate(dataset, total_votes):
    candidate_dict = {'profile':{}}
    
    #Find candidate name
    for candidate in dataset:    
        if candidate[2] not in candidate_dict.items():
            candidate_dict['profile'][candidate[2]] = 0
    
    votes_counter = 0
    for candidate_name in candidate_dict['profile']:
        for rows in dataset:
            if rows[2] == candidate_name:
                votes_counter +=1
                candidate_dict['profile'][candidate_name] = [votes_counter]
                candidate_dict['profile'][candidate_name].append(100 * votes_counter/total_votes)
                candidate_dict['profile'][candidate_name].append(0)
        votes_counter = 0
    
    votes_winner = 0
    for i in candidate_dict['profile']:
        if candidate_dict['profile'][i][0] > votes_winner:
            votes_winner = candidate_dict['profile'][i][0]
            candidate_dict['profile'][i][2] = 1
        else:
            candidate_dict['profile'][i][2] = 0
    return candidate_dict

def poll_results():

    election_results = {
            'headers': ['Election Results', '----------------------'],
            'votes': 0,
            'labels': ['Total Votes', 'Winner'],
            'candidates': {}
            }
    
    with open(path_election_data_file, 'r') as election_data_file:
        election_data_ds = csv.reader(election_data_file, delimiter=',')
        next(election_data_ds)
        #--election_data_ds = [next(election_data_file) for x in range(10)]
        #next(election_data_ds)
        
        election_data_list = [election for election in election_data_ds]
        
        election_results['votes'] = len(election_data_list)
        election_results['candidates'] = profile_per_candidate(election_data_list, election_results['votes'])
        
        
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

poll_results()