import json
import csv

csvfile = open("text.csv", "a")
csvfieldnames = ['first', 'second']
writer = csv.DictWriter(csvfile, csvfieldnames)
writer.writeheader()
writer.writerow({'first':'this thing', 'second':'this other thing'})
csvfile.close()



textfile = open("test.txt", "a")

obj = { 'hello':'world'}
parse_object = json.dumps(obj)

textfile.write(parse_object)

textfile.close()
