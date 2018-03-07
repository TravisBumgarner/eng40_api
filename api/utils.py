from eng40.keys import PUSHOVER_APP_TOKEN, PUSHOVER_USER_KEY
import httplib
import urllib


def send(message):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
        urllib.urlencode({
            "token": PUSHOVER_APP_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
        }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

