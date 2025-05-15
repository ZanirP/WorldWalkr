filepath = "database/token_counts.txt"


with open(filepath, "r") as f:
	lines = f.readlines()
	for index in range(len(lines)):
		# Remove any leading or trailing whitespace characters
		lines[index] = int(lines[index].strip())
		if type(lines[index]) != int:
			print(f"Error: {lines[index]} is not an integer")
			lines[index] = 0
print(f"Total number of books: {len(lines)}")
  
print(f"Average number of tokens: {sum(lines) / len(lines)}")
print(f"Minimum number of tokens: {min(lines)}")
print(f"Maximum number of tokens: {max(lines)}")
print(f"Variance of tokens: {sum((x - (sum(lines) / len(lines))) ** 2 for x in lines) / len(lines)}")
print(f"25th percentile of tokens: {sorted(lines)[int(len(lines) * 0.25)]}")
print(f"Median of tokens: {sorted(lines)[int(len(lines) * 0.5)]}")
print(f"75th percentile of tokens: {sorted(lines)[int(len(lines) * 0.75)]}")
print(f"80th percentile of tokens: {sorted(lines)[int(len(lines) * 0.8)]}")
print(f"90th percentile of tokens: {sorted(lines)[int(len(lines) * 0.9)]}")

'''
Total number of books: 16559
Average number of tokens: 549.6566217766773
Minimum number of tokens: 2
Maximum number of tokens: 13876
Variance of tokens: 415720.7791262409
25th percentile of tokens: 152
Median of tokens: 335
75th percentile of tokens: 726
80th percentile of tokens: 857
90th percentile of tokens: 1264
'''

