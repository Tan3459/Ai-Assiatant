import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime


r = sr.Recognizer()
phone_numbers={"ravi":"8787365091","raj":"7629917568","raja":"7629912878"}
gmails={"ravi":"tdas71372@gmail.com","raj":"raj8736@gmail.com","raja":"raja55773@gmail.com"}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print('Listening... Ask now...')
            audioin = r.listen(source)
            # Replace with recognize_google or any configured method
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)
            
            #Ask to play song
            if 'play' in my_text:
                my_text=my_text.replace('play','')
                speak('playing'+ my_text)
                pywhatkit.playonyt(my_text) 
            
            #Ask Date
            if 'date' in my_text:
                today=datetime.date.today()
                speak(today)

            #Ask Time
            if 'time' in my_text:
                timenow=datetime.datetime.now().strftime('%H:%M')
                speak(timenow)

            #Ask details about any person
            if 'who is' in my_text:
                person=my_text.replace('who is','')
                info=wikipedia.summary(person,5)
                speak(info)

            #Ask phone number
            if "phone number" in my_text:
                names=list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name + "Phone numbers" + phone_numbers[name])
                        speak(name + "Phone numbers" + phone_numbers[name])
            #Ask gmail
            if "gmail" in my_text:
                gmail=list(gmails)
                print(gmail)
                for gmail in gmails:
                    if gmail in my_text:
                        print(gmail + "Gmail is" + gmails[gmail])
                        speak(gmail + "Gmail is" + gmails[gmail])

    except Exception as e:
        print(f"Error in capturing microphone: {e}")


commands()
