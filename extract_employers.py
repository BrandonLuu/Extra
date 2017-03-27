"""
Author: Brandon Luu
Date: 3/27/17
Description: This is a script that reads a file with Wal-Mart CSV address list
and then writes a correct postal address style format into another file.
"""
# Input/Output file names
input_file = "final_employers.txt"
output_file = "out_test.txt"

# Open files
in_fd = open(input_file, 'r')
out_fd = open(output_file, 'w')

# Variables
count = 0

# Remove the "DAY 1 -" or "DAY 2 -" from the line
def RemoveDay(line):
	item = ""
	unwant = ("DAY", "1", "2", "-")
	
	# Write just the number and item
	line = line.split()		
	for i in range(len(line)):
		if all(s not in line[i] for s in unwant):
			item += line[i] + " " #write all but the beginning string
	return item

# Read in each line
for line in in_fd:
	
	if "ORGANIZATION NAME" in line:		
		count += 1
		item = ""
		unwant = ("ORGANIZATION", "NAME")

		# Write just the number and item
		line = line.split()		
		for i in range(len(line)):
			if all(s not in line[i] for s in unwant):
				item += line[i] + " " #write all but the beginning string
		out_fd.write(str(count) + ": " + item + "\n")
		
	if "MAJORS RECRUITED" in line:
		item = RemoveDay(line)
		out_fd.write(item + "\n")
		
	if "DEGREE LEVELS RECRUITED" in line:
		item = RemoveDay(line)
		out_fd.write(item + "\n")
		
	if "POSITION TYPES" in line:
		item = RemoveDay(line)
		out_fd.write(item + "\n\n")	

# Close Files
in_fd.close()
out_fd.close()