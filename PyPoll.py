##Election Analysis

#import dependencies
from email import header
import os
import csv

# assign a variable for the data file and open the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# STEP ONE Initialize a total vote counter
total_votes = 0

# Declaring a new list
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # read the header row
     headers = next(file_reader)
     
     #print each row in the CSV file
     for row in file_reader:
          # STEP 2 Add to the total vote count
          total_votes += 1

          # Print the candidate name from each row
          candidate_name = row[2]

          #add unique candidate name to the candidate list
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)

# STEP 3 Print the total votes
print(total_votes)

# print the candidate list
print(candidate_options)


#total number of votes cast
     #answer: 369711

#complete list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of election based on popular vote
