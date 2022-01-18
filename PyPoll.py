##Election Analysis

#import dependencies
from email import header
import os
import csv

# assign a variable for the data file and open the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze the data here

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # read and print the header row
     headers = next(file_reader)
     print(headers)


#total number of votes cast

#complete list of candidates who received votes

#percentage of votes each candidate won

#total number of votes each candidate won

#winner of election based on popular vote
