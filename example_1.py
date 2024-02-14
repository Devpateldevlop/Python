import pyttsx3
# import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib

from sys import platform
import os
import getpass
# import cv2

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
            hour = int(datetime.datetime.now().hour)
            engine.say("Good Morning SIR")

elif hour >= 12 and hour < 18:
       hour = int(datetime.datetime.now().hour)
       engine.say("Good Afternoon SIR")

else:
           hour = int(datetime.datetime.now().hour)
           engine.say ('Good Evening SIR')

engine.say(" i am at your service ")
engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
engine.setProperty("rate", 200)  # Adjust the speaking rate (words per minute)
engine.setProperty("volume", 1.0)  # Adjust the volume (0.0 to 1.0)

recognizer = sr.Recognizer()
        # Capture audio from the microphone
while True:
    
        with sr.Microphone() as source:
            print("Listening for speech...")
            audio_data = recognizer.listen(source, timeout=None, phrase_time_limit=None)

         # Perform speech recognition
            recognized_text = recognizer.recognize_google(audio_data)
        #     if not isinstance(audio_data, dict) or len(audio_data.get("alternative", [])) == 0:
        #      print("say again")
            
         # Check if recognized text is not null (contains speech)
            if recognized_text:
             print("Recognized Text:", recognized_text)
             c= len(recognized_text)
            print(c)
          # if 'Jarvis' in recognized_text:
          #  engine.say("yes sir")
          # if 'hello' in recognized_text:
          #   engine.say("yes sir")
          # if 'time' in recognized_text:
          #   strTime = datetime.datetime.now().strftime("%H:%M:%S")
          #   engine.say(f'Sir, the time is {strTime}')
          # 


    # with sr.Microphone() as source:
    #         print("Listening...")
    #         audio = recognizer.listen(source)

    #     # Convert speech to text
    # text = recognizer.recognize_google(audio)
    # print(text)
  
        if 'Jarvis' in recognized_text:
         engine.say("yes sir")
         if 'hello' in recognized_text:
          engine.say("yes sir")

          if 'hii' in recognized_text:
          engine.say("yes sir")

         if 'jarvis are you there' in recognized_text:
          engine.say("Yes Sir, at your service")
         if 'time' in recognized_text:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           engine.say(f'Sir, the time is {strTime}')



        engine.runAndWait()


 
        



# Initialize the recognizer
# recognizer = sr.Recognizer()

# # print("Say something:")
# # audio = recognizer.listen(sr.Microphone())
# # text = recognizer.recognize_google(audio)
# # print("You said:", text)
# # Capture audio from a microphone
# with sr.Microphone() as source:
#     print("Say something:")
#     audio = recognizer.listen(source)

# try:
#     # Recognize speech using Google Web Speech API
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Could not understand audio")
# except sr.RequestError as e:
#    print("Could not request results; {0}".format(e))


# Initialize the text-to-speech engine
# engine = pyttsx3.init()

# Initialize the recognizer

 

# Set the properties of the text-to-speech engine (optional)
 
#  if text==None:
#  print("said again")
#  if text =="0":
#    print("say somthing")
#  else:
#    while True:
#     recognizer = sr.Recognizer()
#         # Capture audio from the microphone
#  with sr.Microphone() as source:
#             print("Listening...")
#             audio = recognizer.listen(source)

#         # Convert speech to text
#  text = recognizer.recognize_google(audio)    
        
        # engine.say(text)
        # engine.runAndWait()

    # except sr.UnknownValueError:
    #     print("Could not understand the audio.")
    # except sr.RequestError as e:
    #     print(f"Error with the speech recognition service: {e}")
    # except KeyboardInterrupt:
    #     print("Stopping the program.")
    # recognizer = sr.Recognizer()    
    # audio = recognizer.listen(source)
    # text = recognizer.recognize_google(audio)
    
 # # print(text)
 # hour = int(datetime.datetime.now().hour)
 # print(hour)






    

# class Jarvis:
#     def __init__(self) -> None:
#         if platform == "linux" or platform == "linux2":
#             self.chrome_path = '/usr/bin/google-chrome'

#         elif platform == "darwin":
#             self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

#         elif platform == "win32":
#             self.chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#         else:
#             print('Unsupported OS')
#             exit(1)
#         webbrowser.register(
#             'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
#         )

#     # def wishMe(self) -> None:
#         hour = int(datetime.datetime.now().hour)
#         if hour >= 0 and hour < 12:
#             engine.say("Good Morning SIR")
#         elif hour >= 12 and hour < 18:
#          engine.say("Good Afternoon SIR")

        # else:
        #    engine.say ('Good Evening SIR')

#         weather()
#         engine.say('I am JARVIS. Please tell me how can I help you SIR?')

#     def sendEmail(self, to, content) -> None:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#         server.login('email', 'password')
#         server.sendmail('email', to, content)
#         server.close()

#     def execute_query(self, query):
#         # TODO: make this more concise
#         if 'wikipedia' in query:
#             engine.say('Searching Wikipedia....')
#             query = query.replace('wikipedia', '')
#             results = wikipedia.summary(query, sentences=2)
#             engine.say('According to Wikipedia')
#             print(results)
#             engine.say(results)
#         elif 'youtube downloader' in query:
#             exec(open('youtube_downloader.py').read())
            
        
            
#         elif 'voice' in query:
#             if 'female' in query:
#                 engine.setProperty('voice', voices[1].id)
#             else:
#                 engine.setProperty('voice', voices[0].id)
#             engine.say("Hello Sir, I have switched my voice. How is it?")

        # if 'jarvis are you there' in text:
        #     engine.say("Yes Sir, at your service")
        # if 'jarvis who made you' in text:
        #     engine.say("Yes Sir, my master build me in AI")
            
         

#         elif 'open youtube' in query:

#             webbrowser.get('chrome').open_new_tab('https://youtube.com')
            
#         elif 'open amazon' in query:
#             webbrowser.get('chrome').open_new_tab('https://amazon.com')

#         elif 'cpu' in query:
#             cpu()

#         elif 'joke' in query:
#             joke()

#         elif 'screenshot' in query:
#             speak("taking screenshot")
#             screenshot()

#         elif 'open google' in query:
#             webbrowser.get('chrome').open_new_tab('https://google.com')

#         elif 'open stackoverflow' in query:
#             webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

#         elif 'play music' in query:
#             os.startfile("D:\\RoiNa.mp3")

#         elif 'search youtube' in query:
#             engine.say('What you want to search on Youtube?')
#             youtube(takeCommand())
#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             engine.say(f'Sir, the time is {strTime}')

#         elif 'search' in query:
#             engine.say('What do you want to search for?')
#             search = takeCommand()
#             url = 'https://google.com/search?q=' + search
#             webbrowser.get('chrome').open_new_tab(
#                 url)
#             engine.say('Here is What I found for' + search)

#         elif 'location' in query:
#             engine.say('What is the location?')
#             location = takeCommand()
#             url = 'https://google.nl/maps/place/' + location + '/&amp;'
#             webbrowser.get('chrome').open_new_tab(url)
#             engine.say('Here is the location ' + location)

#         elif 'your master' in query:
#             if platform == "win32" or "darwin":
#                 engine.say('Gaurav is my master. He created me couple of days ago')
#             elif platform == "linux" or platform == "linux2":
#                 name = getpass.getuser()
#                 engine.say(name, 'is my master. He is running me right now')

#         elif 'your name' in query:
#             engine.say('My name is JARVIS')
#         elif 'who made you' in query:
#             engine.say('I was created by my AI master in 2021')
            
#         elif 'stands for' in query:
#             engine.say('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
#         elif 'open code' in query:
#             if platform == "win32":
#                 os.startfile(
#                     "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
#             elif platform == "linux" or platform == "linux2" or "darwin":
#                 os.system('code .')

#         elif 'shutdown' in query:
#             if platform == "win32":
#                 os.system('shutdown /p /f')
#             elif platform == "linux" or platform == "linux2" or "darwin":
#                 os.system('poweroff')

#         elif 'cpu' in query:
#             cpu()
#         elif 'your friend' in query:
#             engine.say('My friends are Google assisstant alexa and siri')

#         elif 'joke' in query:
#             joke()

#         elif 'screenshot' in query:
#             engine.say("taking screenshot")
#             screenshot()

#         elif 'github' in query:
#             webbrowser.get('chrome').open_new_tab(
#                 'https://github.com/gauravsingh9356')

#         elif 'remember that' in query:
#             engine.say("what should i remember sir")
#             rememberMessage = takeCommand()
#             engine.say("you said me to remember"+rememberMessage)
#             remember = open('data.txt', 'w')
#             remember.write(rememberMessage)
#             remember.close()

#         elif 'do you remember anything' in query:
#             remember = open('data.txt', 'r')
#             engine.say("you said me to remember that" + remember.read())

#         elif 'sleep' in query:
#             sys.exit()

#         elif 'dictionary' in query:
#             engine.say('What you want to search in your intelligent dictionary?')
#             translate(takeCommand())

#         elif 'news' in query:
#             engine.say('Ofcourse sir..')
#             speak_news()
#             speak('Do you want to read the full news...')
#             test = takeCommand()
#             if 'yes' in test:
#                 speak('Ok Sir, Opening browser...')
#                 webbrowser.open(getNewsUrl())
#                 engine.say('You can now read the full news from this website.')
#             else:
#                 engine.say('No Problem Sir')

#         elif 'voice' in query:
#             if 'female' in query:
#                 engine.setProperty('voice', voices[0].id)
#             else:
#                 engine.setProperty('voice', voices[1].id)
#             engine.say("Hello Sir, I have switched my voice. How is it?")

#         elif 'email to gaurav' in query:
#             try:
#                 engine.say('What should I say?')
#                 content = takeCommand()
#                 to = 'email'
#                 self.sendEmail(to, content)
#                 engine.say('Email has been sent!')

#             except Exception as e:
#                 engine.say('Sorry sir, Not able to send email at the moment')


# def wakeUpJARVIS():
#     bot_ = Jarvis()
#     bot_.wishMe()
#     while True:
#         query = takeCommand().lower()
#         bot_.execute_query(query)
               

# if __name__ == '__main__':
    
#     recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
#     recognizer.read('./Face-Recognition/trainer/trainer.yml')   #load trained model
#     cascadePath = "./Face-Recognition/haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

#     font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


#     id = 2 #number of persons you want to Recognize


#     names = ['','Gaurav']  #names, leave first empty bcz counter starts from 0


#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
#     cam.set(3, 640) # set video FrameWidht
#     cam.set(4, 480) # set video FrameHeight

#     # Define min window size to be recognized as a face
#     minW = 0.1*cam.get(3)
#     minH = 0.1*cam.get(4)

#     # flag = True

#     while True:

#         ret, img =cam.read() #read the frames using the above created object

#         converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

#         faces = faceCascade.detectMultiScale( 
#             converted_image,
#             scaleFactor = 1.2,
#             minNeighbors = 5,
#             minSize = (int(minW), int(minH)),
#         )

#         for(x,y,w,h) in faces:

#             cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

#             id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

#             # Check if accuracy is less them 100 ==> "0" is perfect match 
#             if (accuracy < 100):
                
#                 # Do a bit of cleanup
#                 engine.say("Optical Face Recognition Done. Welcome")
#                 cam.release()
#                 cv2.destroyAllWindows()
#                 wakeUpJARVIS()
#             else:
#                engine.say("Optical Face Recognition Failed")
            #    break;


    
    