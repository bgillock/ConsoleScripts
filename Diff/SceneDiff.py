import sys

if (len(sys.argv) != 3):
    sys.stdout.write("Usage: SceneDiff file1 file2")
    exit()

file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

print("File1 has {} line", len(Lines))

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))