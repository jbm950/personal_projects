import csv

print("Case 1: Default (skipinitialspace = False)")

f = open('csv_skipinitialspace_testing.csv','r')
reader = csv.reader(f)
mon_rows = list(reader)
print("Output from reader:")
for row in mon_rows:
    print("\t",end = "")
    print(row)
f.close()

print("\nCase 2: skipinitialspace = True")

f = open('csv_skipinitialspace_testing.csv','r')
reader = csv.reader(f, skipinitialspace = True)
mon_rows = list(reader)
print("Output from reader:")
for row in mon_rows:
    print("\t",end = "")
    print(row)
f.close()

