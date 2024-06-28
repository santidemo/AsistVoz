import speech_recognition as sr
import pyttsx3
import webbrowser

# Inicialización del reconocedor de voz y el motor de texto a voz
reconocedor = sr.Recognizer()
motor = pyttsx3.init()

# Configuración de la voz
voces = motor.getProperty("voices")
motor.setProperty("voice", voces[0].id)

def hablar(texto):
    """Convierte texto a voz y lo dice en voz alta."""
    motor.say(texto)
    motor.runAndWait()

def escuchar():
    """Escucha a traves del microfono y devuelve la entrada de voz como texto."""
    try:
        with sr.Microphone() as fuente:
            print("Te escucho...")
            audio = reconocedor.listen(fuente)
            texto_reconocido = reconocedor.recognize_google(audio, language="es-ES")
            texto_reconocido = texto_reconocido.lower()
            return texto_reconocido
    except sr.UnknownValueError:
        hablar("No pude entender lo que dijiste. Inténtalo de nuevo.")
    except sr.RequestError:
        hablar("Error de conexión. Por favor, verifica tu conexión a internet.")
    except Exception as e:
        print(f"Error al reconocer el audio: {str(e)}")
        hablar("Ocurrió un error al reconocer el audio.")
    return None

def abrir_youtube():
    """Abre YouTube en el navegador predeterminado"""
    url = "https://www.youtube.com/"
    webbrowser.open(url)

def ejecutar_asistente():
    """Funcion principal que ejecuta el asistente de voz."""
    hablar("Buenas noches Ában, ¿qué quieres que repita por ti hoy?")
    texto_reconocido = escuchar()

    if texto_reconocido:
        hablar(f"Has dicho: {texto_reconocido}")
        print(texto_reconocido)
        if any(palabra_clave in texto_reconocido for palabra_clave in ["ver un video", "abrir youtube", "youtube"]):
            hablar("Abriendo YouTube.")
            abrir_youtube()
    else:
        hablar("No se entendió. Inténtalo de nuevo.")

ejecutar_asistente()
