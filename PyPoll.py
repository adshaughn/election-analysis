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
# Declaring an empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
     # read the header row
     headers = next(file_reader)
     
     #print each row in the CSV file
     for row in file_reader:
          # Add to the total vote count
          total_votes += 1

          # Print the candidate name from each row
          candidate_name = row[2]

          #add unique candidate name to the candidate list
          if candidate_name not in candidate_options:

               #add the candidate name to the candidate list
               candidate_options.append(candidate_name)

               #begin tracking candidate's vote count
               candidate_votes[candidate_name] = 0

          #add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

     #save results to our text file
     with open(file_to_save, "w") as txt_file:

          #print the final vote count
          election_results = (
               f"\nElection Results\n"
               f"--------------------\n"
               f"Total Votes: {total_votes:,}\n"
               f"--------------------\n"
          )
          print(election_results, end="")

          #save the final vote count to the text file
          txt_file.write(election_results)


          #determine vote percentages
          #iterate through the candidate list
          for candidate_name in candidate_votes:
               
               #retrieve vote count of candidate
               votes = candidate_votes[candidate_name]

               #calculate percentage of votes
               vote_percentage = float(votes) / float(total_votes) * 100

               candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

               # Print each candidate, their voter count, and percentage to the terminal.
               print(candidate_results)
               #  Save the candidate results to our text file.
               txt_file.write(candidate_results)

               #determine winning vote count and candidate
               #determine if the votes is greater than winning count
               if (votes > winning_count) and (vote_percentage > winning_percentage):

                    # if true then set winning_count = votes and winning_percent = vote_percentage
                    winning_count = votes
                    winning_percentage = vote_percentage

                    #and then set the winning_candidate equal to that candidate's name
                    winning_candidate = candidate_name
          
          winning_candidate_summary = (
               f"--------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage: {winning_percentage:.1f}%\n"
               f"--------------------\n"
          )
          #save the final candidate count to the text file
          txt_file.write(candidate_results)

          #save the winning candidate's name to the text file
          txt_file.write(winning_candidate_summary)

                    

     #total number of votes cast
          #answer: 369711

     #complete list of candidates who received votes

     #percentage of votes each candidate won

     #total number of votes each candidate won

     #winner of election based on popular vote
