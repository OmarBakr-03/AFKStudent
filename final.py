#Please read the README file before assessing

#Importing Libraries
import pyautogui
import os
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Omar Bakr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import time
from twilio.rest import Client
import json
import requests

# Your Account SID from twilio.com/console
account_sid = "ACf083672641deb03941d505694edca2da"
# Your Auth Token from twilio.com/console
auth_token  = "8705fbcea0a5cb673ca3db5b6e49693e"

client = Client(account_sid, auth_token)
# from pushbullet import PushBullet

# API_KEY = "o.GoVgB0ldmujStfog709gCjfQNSSq5kFs"

calledName = False
# with open("test.txt", "r+") as file:

class specifications: #a class of the person who's using the program's specifications 
    def __init__(self, name, width, length):
        self.name = name #name
        self.width = width #width dimension of the tab of google meet
        self.length = length #height dimension of the tab of google meet

  #functions to retrieve the attributes
    def getName(self):
        return self.name
    def getWidth(self):
        return self.width
    def getLength(self):
        return self.length

name = str(input('Enter your name: '))
person = specifications(name, 800, 250)

previous = []
difference = []
total = []

while calledName == False:
    time.sleep(5)
    myScreenshot = pyautogui.screenshot(region=(325,400, 800, 250))
    myScreenshot.save('image3.png')
    userCurrent = " "
    userPast = " "
    # Use OCR to extract text from Image


    img = Image.open("image3.png")
    text = tess.image_to_string(img)
    os.remove("image3.png")

    
    s = text

    current = s.split()

    if len(previous) > 0:
        for i in range(len(current)):
            if current[0:i] in previous:
                continue
            else:
                difference = current[i -1:len(current)]
    else:
        difference = current

    previous = current
    total.append(difference)
    totalLen = len(total)
    # print(totalLen)


        
        
        
    word = person.getName()
    # count = 1

    if word in text:
        # print("found on line", count)
        # pb = PushBullet(API_KEY)
        print("Found")
        calledName = True
        #The Twilio api that allows to make phone calls and send sms messages
        message = client.messages.create(
            to="+16475499325", 
            from_="+16463511854",
            body="You've been called in your meet")

        print(message.sid)

        call = client.calls.create(
            twiml='<Response><Say>Hello</Say></Response>',
            to="+16475499325", 
            from_="+16463511854",
        )
        break

print(total)
asdf = []
for v in range(len(total)):
    totalString = " ".join(total[v])
    asdf.append(totalString)

t = ' '.join(asdf)
f = open('test.txt', 'w')
for i in range(len(t)):
    if t[i] != '.':
        f.write(t[i])
    else:
        f.write('.\n')

f.close()

#Google Drive API that allows us to uplpoad the txt file to google drive
headers = {"Authorization": "Bearer ya29.a0ARrdaM9I0w2oHfBQQ7WdoNFz7WRsjwffKh-1wxvLntC086bapTFEd86_MwuZxojUhzIl6YiJPA9Q-paYPAg0CxQUe5-glYy2fKofCYSwd2WDHzaR2BaNqyESm5WMXG3QYnygkloKq4hppzm-fV36uZaYTrGo"}
para = {
    "name": "sample.txt",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./test.txt", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
#Credits:
#https://www.twilio.com/docs/sms/quickstart/python
#https://www.youtube.com/watch?v=JwGzHitUVcU

    
