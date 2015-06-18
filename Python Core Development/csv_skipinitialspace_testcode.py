import csv
from tempfile import TemporaryFile

fp = TemporaryFile("w+")
fp.write("no space, space,  spaces,\ttab")
fp.seek(0)

reader = csv.reader(fp)
rows = list(reader)
for row in rows:
    print(row)

fp.seek(0)
reader = csv.reader(["no space, space,  spaces,\ttab"], skipinitialspace=True)
rows = list(reader)
for row in rows:
    print(row)

fp.close()
