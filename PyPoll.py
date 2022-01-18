##Election Analysis

#import dependencies
import os
import csv

# assign a variable for the data file and open the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# close the file

election_data.close()


#total number of votes cast

#complete list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of election based on popular vote
