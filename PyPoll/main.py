# Import necessary modules
import csv
import os

# establish paths of files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # set a variable to hold total number of votes cast
candidateName = 0 #set a variable to hold the candidate's name
candidateVoteCount = 0 #set a variable to hold the count of votes cast for a candidate

# Define a list 'candidates' to hold the list of candidates
candidates = []
# Define a dictionary 'voteCounts' to hold the election results
voteCounts = {}
# define Winning Candidate and Winning Count variables
winningCandidate = 0
winningCount = 0

# Open the CSV file and load it to the reader
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the file:
    for row in reader:
        #Print a loading indicator (for large datasets)
        #print(". ", end="") *note: I removed this because it wasn't in the final output displayed in the module assignment

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidateName = (row[2])

        # If the candidate is not already in the candidate list, add them
        if candidateName not in candidates:
            candidates.append(candidateName)
            voteCounts[candidateName] = 1 #create the key value pair in the dictionary, initialize the vote count at 1
        else:
            #if the candidate is already in the list, add a vote to their total
            voteCounts[candidateName] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count to the terminal
    print("Election Results\n")
    print("----------------------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("----------------------------------------------\n")

    #print the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------------------------\n")

    # Loop through the candidates to determine vote percentages to 3rd decimal place and identify the winner
    for candidateName in voteCounts:
        percentage = round((voteCounts[candidateName]/total_votes)*100,3)

        #calculate and print the vote count and percentage to terminal
        print(f"{candidateName}: {percentage}% ({voteCounts[candidateName]})\n")

        #print the vote count and percentage to the text file
        txt_file.write(f"{candidateName}: {percentage}% ({voteCounts[candidateName]})\n")

        # Update the winning candidate if this one has more votes
        if voteCounts[candidateName] > winningCount:
            # record the winning vote count and the winning candidate:
            winningCount = voteCounts[candidateName]
            winningCandidate = candidateName

    #print the winning candidate to terminal
    print("----------------------------------------------\n")
    print(f"Winner: {winningCandidate}\n")
    print("----------------------------------------------\n")
    
    #print the winning candidate to the text file
    txt_file.write("----------------------------------------------\n")
    txt_file.write(f"Winner: {winningCandidate}\n")
    txt_file.write("----------------------------------------------\n")
