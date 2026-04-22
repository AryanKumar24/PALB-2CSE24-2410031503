from collections import Counter

def winner(arr):
    freq = Counter(arr)
    
    max_votes = max(freq.values())
    
    candidates = [name for name, votes in freq.items() if votes == max_votes]
    
    winner_name = min(candidates)
    
    return [winner_name, str(max_votes)]


n = int(input("Enter number of votes: "))
arr = []

for _ in range(n):
    arr.append(input("Enter candidate name: ").lower())

result = winner(arr)

print("Winner:", result)
