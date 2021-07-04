import smtplib
import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3   # python install pyttsx
from email.message import EmailMessage #import email module





listener =sr.Recognizer()
engine =pyttsx3.init()   #driver module

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
#pip install pyaudio
def takingInput():
    try:
        with sr.Microphone() as source:
              print('I m Listening...')
              voice =listener.listen(source,phrase_time_limit=10)
              info =listener.recognize_google(voice)
              print(info)
              return info
    except:
       pass
    
    
def sendEmail(receiver,subject,message):
        server =smtplib.SMTP('smtp.gmail.com',587)
        server.starttls() 
        server.login('tempproject9090@gmail.com','urvashi9090')
        email =EmailMessage()
        email['From']='amangoel9876@gmail.com'
        email['To']=receiver
        email['Subject']=subject
        email.set_content(message)
        server.send_message(email)
        talk('The messeage is send')
        



email_list = {
       'Ankit': 'ankitsharma97194@gmail.com',
       'Aman': 'amansharm@gmail.com',
       'Urvashi':'urvashi181132@gmail.com',
       'Bali':'kashvibali696@gmail.com',
       'Akash':'baliakash145@gmail.com'
       
}


def getEmailInfo():
   e="yes"
   t="no"
   m="no"
   while(e=="yes"):
        while(t == m):
            talk('Hey Urvashi, To whom you want to mail any email,please select the serial no in a list')
            name =takingInput()
            receiver=email_list[name]
            print(receiver)
            talk("is it correct email id of receiver to whom u want to mail  that is")
            talk(receiver)
            talk("say yes if it is correct emailid otherwise say no")
            m=takingInput()
        talk('Can you tell me the subject of the email?')
        subject=takingInput()
        talk('What you wanna text in this email')
        message=takingInput()
      
        sendEmail(receiver,subject,message)
        talk('Do u want to send more mail')
        e=takingInput()
        m="no"
   talk(" ok,Thank You Urvashi")
        
      
       
     
     
      
getEmailInfo()

