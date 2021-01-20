
# name dependencies
import os
import csv

# create file path

input_path = "Resources/election_data.csv"

# variables and lists
#candidate_set = set()


vote_count = []
candidate_list = []
unique_candidate_list = []
tally_list = []

# function

def tally(voter_data):

    # define the columns in voter data
    voter_id = str(voter_data[0])
    county = str(voter_data[1])
    candidate = str(voter_data[2])

    # populate lists for total vote, list of candidates, and unique list of candidates
    vote_count.append(voter_id)
    candidate_list.append(candidate)

# read input file

with open(input_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
 
    #for each row run the tally function
    for row in csv_reader:
        tally(row)

for candidate in candidate_list: 
        # check if exists in unique_list or not 
        if candidate not in unique_candidate_list: 
            unique_candidate_list.append(candidate) 

# for each candidate in candidate list
for candidate in unique_candidate_list:

    tally_list.append(candidate_list.count(candidate))

# create output variables
total_votes = len(vote_count)

can1_votes = tally_list[0]
can1_percentage = (tally_list[0]/total_votes)*100

can2_votes = tally_list[1]
can2_percentage = (tally_list[1]/total_votes)*100

can3_votes = tally_list[2]
can3_percentage = (tally_list[2]/total_votes)*100

can4_votes = tally_list[3]
can4_percentage = (tally_list[3]/total_votes)*100

#determine the winner by taking the max of the candidate tallys
winner_index = tally_list.index(max(tally_list))
winner = unique_candidate_list[winner_index]

#display output in terminal 
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Khan: {can1_percentage:.3f}%  ({can1_votes})')
print(f'Correy: {can2_percentage:.3f}%  ({can2_votes})')
print(f'Li: {can3_percentage:.3f}%  ({can3_votes})')
print(f'OTooley: {can4_percentage:.3f}%  ({can4_votes})')
print(f'Winner: {winner}')

# write output to a text file
text_file = open("Analysis/Output.txt", "w")
text_file.write('Election Results')
text_file.write("\n")
text_file.write('-------------------------')
text_file.write("\n")
text_file.write(f'Total Votes: {total_votes}')
text_file.write("\n")
text_file.write('-------------------------')
text_file.write("\n")
text_file.write(f'Khan: {can1_percentage:.3f}%  ({can1_votes})')
text_file.write("\n")
text_file.write(f'Correy: {can2_percentage:.3f}%  ({can2_votes})')
text_file.write("\n")
text_file.write(f'Li: {can3_percentage:.3f}%  ({can3_votes})')
text_file.write("\n")
text_file.write(f'OTooley: {can4_percentage:.3f}%  ({can4_votes})')
text_file.write("\n")
text_file.write(f'Winner: {winner}')

