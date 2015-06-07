import csv

# First test case: subclassing dialect

print("Test case 1: sub-classing Dialect (Mon)")

class Mon(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    doublequote = True
    quoting = 0
    lineterminator = '\n'

f = open('sans_headers.csv','r')
reader = csv.DictReader(f, fieldnames=('code', 'nom', 'texte'), dialect=Mon)
print("\tReader's dialect: %s" % reader.dialect)
mon_rows = list(reader)
print("\tOutput from reader:\n")
for row in mon_rows:
    print("\t",end = "")
    print(row)
f.close()

# Second test case: Keywords (same as subclass mon)

print("\nTest case 2: inputting attrs as keywords")

f = open('sans_headers.csv','r')
reader = csv.DictReader(f, fieldnames=('code', 'nom', 'texte'),
                        delimiter=',', quotechar='"', quoting=0,
                        lineterminator='\n')
print("\tReader's dialect: %s" % reader.dialect)
dflt_rows = list(reader)
print("\tOutput from reader:\n")
for row in dflt_rows:
    print("\t",end = "")
    print(row)

f.close()

# Test case 3: Default excel dialect

print("\nTest case 3: Default Excel Dialect")

f = open('sans_headers.csv','r')
reader = csv.DictReader(f, fieldnames=('code', 'nom', 'texte'))
print("\tReader's dialect: %s" % reader.dialect)
excel_rows = list(reader)
print("\tOutput from reader:\n")
for row in excel_rows:
    print("\t",end = "")
    print(row)

f.close()