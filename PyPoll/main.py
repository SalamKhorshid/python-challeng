# Importing required modules:
import os
import csv

# Open CSV file:
with open ('/Users/salam/Documents/BootCamp/Weekly Challenges/python-challenge/PyPoll/Resources/election_data.csv') as election_data:
    lines = csv.reader(election_data)

    # Skip the header:
    header = next(lines)

    # Initialize variables:
    votes = 0
    candidates = []
    candidate_votes = {}

    # Iterate over each row in the CSV:
    for line in lines:

        # The total number of votes:
        votes = votes + 1

        # Add the candidates names to the list:
        candidate = line[2]
        if candidate not in candidates:
            candidates.append(candidate)
        
        # Count the numbers  of votes each candidate won:
        if candidate in candidate_votes:
            candidate_votes [candidate] +=1
        else:
            candidate_votes[candidate] = 1
    print ('Election Results')
    print ('-------------------------')
    print ('Total Votes: ' + str(votes))
    print ('-------------------------')

    # Create a new text file:
    analysis = '/Users/salam/Documents/BootCamp/Weekly Challenges/python-challenge/PyPoll/analysis'
    output = os.path.join (analysis, 'PyPoll_Text.txt')

    # Open the new text file and export the results to it:
    with open (output, 'w') as file:
        file.write ('Election Results' + '\n')
        file.write('-------------------------' + '\n')
        file.write('Total Votes: ' + str(votes) + '\n')
        file.write('-------------------------' + '\n')

        # Calculate the percentage of votes:
        for candidate in candidate_votes:
            vote_count = candidate_votes[candidate]
            percentage = (vote_count / votes) * 100
            print(f"{candidate}: {percentage:.3f}% ({vote_count})")
            file.write(f"{candidate}: {percentage:.3f}% ({vote_count})" + '\n')
        print ('-------------------------')

        # The winner of the election:
        winner = max(candidate_votes, key=candidate_votes.get)
        
        # Print the results:
        print ('Winner: ' + winner)
        print ('-------------------------')
        file.write('-------------------------' + '\n')
        file.write('Winner: ' + winner + '\n')
        file.write('-------------------------' + '\n')