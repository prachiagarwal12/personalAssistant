import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import wolframalpha
import smtplib
from twilio.rest import Client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('rate',130)
engine.setProperty('volume',1.0)

def enunciate(audio):

    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        enunciate("Good Morning!")
    
    elif hour>=12 and hour<16:
        enunciate("Good Afternoon!")
    
    else:
        enunciate("Good Evening!")
        
    enunciate(name)

    enunciate("I am Zira. Please tell me how may I assist you")


def takecommand():

    r = sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:  
        r.adjust_for_ambient_noise(source,duration=1)  #use the default microphone as the audio source
        print("Speak now!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing..')
        text = r.recognize_google(audio, language='en-in')
        print("User:", text)
    
    except Exception as e:
        print(e)
        print("Could you please repeat yourself?")
        enunciate("Could you please repeat yourself?")
        return "None"

    return text


def username():
    
    global name
    enunciate("What should I call you?")
    while name=="None":
        name = takecommand()
    enunciate(name)


def assisname():

    global asname
    enunciate("What would you like to call me?")
    asname = takecommand()
    while asname=="None":
        asname = takecommand()



def sendEmail(to,content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email@gmail.com','your password')
    server.sendemail('')


def calculate(query):

    try:
        question = query
        app_id = 'PUXPWH-YY4K2WU5RQ'
        client = wolframalpha.Client(app_id) 
        res = client.query(question) 
        answer = next(res.results).text 
        print("The result is " , answer)
        enunciate(f"The result is {answer}")
    
    except Exception:
        print("This isn't a valid question")
        enunciate("This isn't a valid question")
        
def whatsapp():
    client = Client()
    enunciate("Please tell your whastapp number")
    from_number = int(takecommand())
    enunciate("Please tell the whatsapp number to which you want to send a message")
    to_number = int(takecommand())
    enunciate("What message would you like me to send?")
    text= takecommand()
    client.messages.create(body=text,
                       from_=from_number,
                       to=to_number)


if __name__ == "__main__":

    name = "None"
    #username()
    #wishMe()
    asname="Zira"

    while True:
        query = takecommand().lower()

        #wikipedia search
        if 'wikipedia' in query:
            enunciate('Searching Wikipedia')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            enunciate("According to Wikipedia")
            print(results)
            enunciate(results)
        
        elif 'open youtube'in query:
            enunciate("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            enunciate("Opening instagram")
            webbrowser.open("instagram.com")

        elif 'open google'in query:
            enunciate("Opening google")
            webbrowser.open("google.com")
        
        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")

        elif 'exit' in query or 'bye' in query:
           enunciate("Ok bye!")
           break

        elif 'how are you' in query:
            enunciate("I am fine. Thank you.")
            enunciate(f"How are you {name}?")
            
        elif 'my name' in query:
            print(name)
            enunciate(name)

        elif 'change my name' in query:
            username()
            enunciate(f"From now I will call you {name}")

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            enunciate("The current time is")
            print(strTime)
            enunciate(strTime)
        
        elif 'what is your name' in query or "what's your name" in query:
            enunciate(f"I love being called {asname}")

        elif 'change your name' in query:
            assisname()
            enunciate(f"From now on you can call me {asname} ")

        elif 'who made you' in query or 'who created you in query' in query:
            enunciate("I have been created by my best friend Prachi!")

        elif 'joke' in query:
            enunciate("I have a joke for you")
            enunciate(pyjokes.get_jokes())

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'calculate' in query or 'question' in query:
            calculate(query)

        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)

        elif "who am i" in query: 
            enunciate("I would like to think you are a human being.") 

        elif "who are you" in query:
            enunciate(f"I am virtual assitant {asname} . I am here to do cool tasks for you.")

        elif 'email to prachi' in query:
            try:
                enunciate("What should I say in the mail?")
                content = takecommand()
                to = "agarwal.ashu.21@gmail.com"
                sendEmail(to,content)
                enunciate("Email has been sent!")

            except Exception as e:
                #print(e)
                enunciate("Sorry")
                enunciate(username)
                enunciate("email could not be sent at this moment!")