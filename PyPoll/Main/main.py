import csv

csv_file_path = "../Resources/election_data.csv"

def analyze_votes(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        total_votes = 0
        candidate_votes = {}

        for row in reader:
            total_votes += 1

            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    return total_votes, candidate_votes

def calculate_percentage(candidate_votes, total_votes):
    percentages = {}
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentages[candidate] = round(percentage, 2)
    return percentages

def find_winner(candidate_votes):
    max_votes = max(candidate_votes.values())
    winner = [candidate for candidate, votes in candidate_votes.items() if votes == max_votes]
    return winner[0]

total_votes, candidate_votes = analyze_votes(csv_file_path)
percentages = calculate_percentage(candidate_votes, total_votes)
winner = find_winner(candidate_votes)

print("Election Results")
print(f"Total Votes: {total_votes}")
for candidate, votes in candidate_votes.items():
    percentage = percentages[candidate]
    print(f"{candidate}: {percentage}% ({votes})")
print(f"Winner: {winner}")

output_file_path = "../analysis/results.txt"
with open(output_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = percentages[candidate]
        file.write(f"{candidate}: {percentage}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")


