import csv, json, time
from datetime import datetime 
from sense_hat import SenseHat
sense = SenseHat()
def sense_env():
	pressure = sense.get_pressure()
	humidity = sense.get_humidity()
	temp = sense.get_temperature()
	current_date = datetime.today()
	iso_date = current_date.strftime("%d/%m/%y %H:%M:%S")
	data = {'pressure': pressure,'humidity': humidity,'temp': temp,'timestamp':iso_date}
	json_data = json.dumps(data)
	print(json_data)
	with open('env-readings.csv', 'a') as csvfile:
		envwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		envwriter.writerow([pressure,humidity, temp, iso_date])
 
	time.sleep(60)
while True:
	sense_env()
