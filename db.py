from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://raspberry-pi-ef36d.firebaseio.com/', None)
result = firebase.get('/data', None)

parsed_json = json.dumps(result)
print (parsed_json)
print unicode(result)

