import json

textfile = open("test.txt", "a")

obj = { 'hello':'world'}
parse_object = json.dumps(obj)

textfile.write(parse_object)

textfile.close()
