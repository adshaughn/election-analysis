### Election Analysis

## Overview

The Colorado Board of Elections is requesting the following data as part of an election audit of a recent congressional election.

1. Calculate the number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate receieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

## Resources

Data source: election_results.csv
Software: python 3.8.9, VS Code 1.38.1

## Summary

The analysis of the election shows that:

- There were 369,711 votes cast in this election

- Votes per county:

-- Jefferson: 38,855 (10.5% of total)

-- Denver: 306,055 (82.8% of total)

-- Arapahoe: 24,801 (6.7% of total)


- Denver county had the largest number of votes

- Results by candidate (number of votes):
-- Charles Casper Stockham: 85,213

-- Diana DeGette: 272,892

-- Raymon Anthony Doane: 11,606


- Results by candidate (percentage of votes):

-- Charles Casper Stockham: 23.0%

-- Diana DeGetter: 73.8%

-- Raymon Anthony Doane: 3.1%

- Overall winner: Diana DeGette

## Election-Audit Summary

The script contained within this repo can be used with slight modifications for any election. By modifying the underlying data source, the script can pull new counties into its county library. Similarly, modifcations to the candidates in the data source will allow it to be used to determine the victors of other elections. It is recommended that a standardized format be rolled out to all election precincts to preclude the need for significant modifications to this script.