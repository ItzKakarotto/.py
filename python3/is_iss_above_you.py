#DAY "Pichhle se Agla" - ISS LOCATION NOTIFIER
#; ) - GitHub.com/ItzKakarotto

import requests as r
import math
import time
import smtplib

MY_LONG = 85.137566
MY_LAT = 25.594095
MY_EMAIL = ""
MY_PASS = ""
TO_EMAIL = ""

def iss_is_close():
    
    resp = r.get("http://api.open-notify.org/iss-now.json").json()
    iss_lat = float(resp["iss_position"]["latitude"])
    iss_long = float(resp["iss_position"]["longitude"])
    
    if math.isclose(iss_lat, MY_LAT, abs_tol=5) and math.isclose(iss_long, MY_LONG, abs_tol=5):
        return True
    return False


while True:
    if iss_is_close():
        msg = 'Subject: {}\n\n{}'.format("Look Up", "Hey dawg Look Up ISS is above You!")
        email_cli = smtplib.SMTP("smtp.gmail.com", port=587)
        email_cli.starttls()
        email_cli.login(user=MY_EMAIL, password=MY_PASS)
        email_cli.sendmail(MY_EMAIL, TO_EMAIL, msg)
    time.sleep(69)