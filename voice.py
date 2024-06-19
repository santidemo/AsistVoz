import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess

# Prueba 1
# listener = sr.Recognizer()

# engine = pyttsx3.init()
# voice = engine.getProperty("voices")
# engine.setProperty("voice", voice[0].id)


# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
    
# def listen():
#     rec = None  
#     try:
#         with sr.Microphone() as source:
#             print("Te escucho")
#             audio = listener.listen(source)
#             rec = listener.recognize_google(audio, language="es-ES")
#             rec = rec.lower() 
            
#     except Exception as e:
#         print(f"Error al reconocer el audio: {str(e)}")
    
#     return rec


# def run_mike():
#     talk("Buenas noches Ában, Que  quieres que repita por ti hoy?")
#     rec = listen()
    
#     if rec:
#         talk(f"Has dicho: {rec}")
#     else:
#         talk("No se entendió. Inténtalo de nuevo.")


# run_mike()






# Prueba 2 ------------
listener = sr.Recognizer()

engine = pyttsx3.init()
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    rec = None  
    try:
        with sr.Microphone() as source:
            print("Te escucho")
            audio = listener.listen(source)
            rec = listener.recognize_google(audio, language="es-ES")
            rec = rec.lower() 
            
    except Exception as e:
        print(f"Error al reconocer el audio: {str(e)}")
    
    return rec

def open_youtube():
    url = "https://www.youtube.com/"
    webbrowser.open(url)

def run_mike():
    talk("Buenas noches Ában, ¿qué quieres que repita por ti hoy?")
    rec = listen()
    
    if rec:
        talk(f"Has dicho: {rec}")
        print(rec)
        if "ver un video" in rec or "abrir youtube" in rec in rec or "youtube" in rec:
            talk("Abriendo YouTube.")
            open_youtube()
    else:
        talk("No se entendió. Inténtalo de nuevo.")


run_mike()



