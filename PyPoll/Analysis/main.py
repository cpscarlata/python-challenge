import csv
import os
# Set file path
csvpath = os.path.join(r'C:\Users\cpsca\OneDrive\Documents\Python Scripts\PyPoll\Resources','election_data.csv')

total_votes = 0
candidates = []
votes_per_candidate = {}

with open('election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 1
        else:
            votes_per_candidate[candidate] += 1

winner = ""
winner_votes = 0

for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print("Candidates:")
print("---------------------------")
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")
