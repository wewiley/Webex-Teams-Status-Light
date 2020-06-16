import os
import time
from webexteamssdk import WebexTeamsAPI
import board
import neopixel
from config import access_token, person

#define the neopixel object by GPIO pin and number of pixels 
pixels = neopixel.NeoPixel(board.D12, 16)

#Webex Teams API Tokens
api = WebexTeamsAPI(access_token)

#Color functions
def red_on():
    pixels.fill((200, 0, 0))
    print ("Turning red on!")
    return
    
def green_on():
    pixels.fill((0, 200, 0))
    print ("Turning green on!")
    return

def blue_on():
    pixels.fill((0, 0, 200))
    print ("Turning blue on!")
    return

#Main function that checks the status of the person via the Webex Teams People API
#and set's the color of the neopixel based on status.
def check_status():
    status = api.people.get(person).status
    print (status)
    if status == "active":
        print ("He's active! GREEN")
        green_on()
    elif status == "call":
        print ("On a call!")
        red_on()
    elif status == "inactive":
        print ("Inactive")
        blue_on()
    else:
        #DND, In a meeting, Presenting, etc.
        red_on()
        print ("Busy")

# Calls the check_status function every 5 seconds.  Important note that any less than 5
# seconds will result in rate limiting by the API.
try:
    while True:
        check_status()
        time.sleep(5)
        print ("Slept for 5 seconds")

         
except KeyboardInterrupt:
    print ("Interrupted")
    pixels.fill(0)
