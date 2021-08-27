# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Storing rows in a list
    rows = []
    for row in file_reader:
        rows.append(row)

    # Total vote count
    total_votes = len(rows)

    #Make a list (set) of all candidates who received votes
    candidates = []
    for i in rows:
        candidates[i[2]] = i
        
        


    
    # Create a county list (set) and county votes dictionary.
    counties = {}
    for i in rows:
        counties[i[1]] = i

# Name dictionary for votes per candidate and county
#votes_each_candidate = dict((name, sum(1 for i in rows if name in i)) for name in candidates)
votes_each_candidate = {}
for i in rows:
    for name in candidates: 
        if name in i:
            votes_each_candidate[name] += 1

votes_each_county = dict((name, sum(1 for i in rows if name in i)) for name in counties)


# Percentage of votes for candidates and counties in a dictionary
vote_percentage1 = dict((name, (float(votes_each_candidate[name]) / float(total_votes) * 100)) for name in candidates)
vote_percentage2 = dict((name, (float(votes_each_county[name]) / float(total_votes) * 100)) for name in counties)

#Choose the winner and largest county turnout of the election (highest percentage) 
winner = [i for i, j in vote_percentage1.items() if j == max(vote_percentage1[i] for i in candidates)][0]
maxcounty = [i for i, j in vote_percentage2.items() if j == max(vote_percentage2[i] for i in counties)][0]

with open(file_to_save, "w") as txt_file:
# Print total votes to terminal
    numvotes = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n\n"
        f"County Votes:\n")
    print(numvotes) 

    # Save total votes results to text file
    txt_file.write(numvotes)

    # Print county results to terminal
    for name in counties:
        county_results = (
            f"{name}: {vote_percentage2[name]:.1f}% ({votes_each_county[name]:,})\n")
        print(county_results)

        # Save county results to text file
        txt_file.write(county_results)

    # Print largest county turnout to terminal
    maxcounty_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {maxcounty}\n"
        f"-------------------------\n")
    print(maxcounty_results)

    # Save largest county turnout to text file
    txt_file.write(maxcounty_results)    

    # Print candidate results to terminal
    for name in candidates:
        candidate_results = (
            f"{name}: {vote_percentage1[name]:.1f}% ({votes_each_candidate[name]:,})\n")  
        print(candidate_results)

        # Save candidate results to text file
        txt_file.write(candidate_results)

    # Print winner summary to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {votes_each_candidate[winner]:,}\n"
        f"Winning Percentage: {vote_percentage1[winner]:.1f}%\n"
        f"-------------------------")
    print(winning_candidate_summary)

    # Save winner summary to text file
    txt_file.write(winning_candidate_summary)