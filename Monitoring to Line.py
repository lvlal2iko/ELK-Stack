import requests,json
import urllib.parse
import time
import schedule

def job() :

	LINE_ACCESS_TOKEN="WgWPI4FFJExCiy9aLirOYBfPNUzuwe4UDjP96u3arEx"
	url = "https://notify-api.line.me/api/notify"
	message ="Test Alert every 10 minutes"
	msg = urllib.parse.urlencode({"message":message})
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
	session = requests.Session()
	a = session.post(url, headers=LINE_HEADERS, data=msg)
	print(a.text)

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.do(job)

while 1:
	schedule.run_pending()
	time.sleep(1)