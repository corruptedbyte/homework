sample1 = open("files/sample.txt", "r")
sample2 = open("files/sample_two.txt", "r")

lines1 = sample1.readlines()
lines2 = sample2.readlines()

print(set(lines1) & set(lines2))

sample1.close()
sample2.close()