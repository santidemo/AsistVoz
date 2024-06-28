import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime

# Inicialización del reconocedor de voz y el motor de texto a voz
reconocedor = sr.Recognizer()
motor = pyttsx3.init()

# Configuración de la voz
voces = motor.getProperty("voices")
motor.setProperty("voice", voces[0].id)

nombre_usuario = ""

def hablar(texto):
    """Convierte texto a voz y lo dice en voz alta."""
    motor.say(texto)
    motor.runAndWait()

def escuchar():
    """Escucha a través del micrófono y devuelve la entrada de voz como texto."""
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
    """Abre YouTube en el navegador predeterminado."""
    url = "https://www.youtube.com/"
    webbrowser.open(url)

def saludar():
    """Saluda según la hora del día."""
    hora_actual = datetime.now().hour
    if 6 <= hora_actual < 12:
        return "Buenos días"
    elif 12 <= hora_actual < 18:
        return "Buenas tardes"
    else:
        return "Buenas noches"

def pedir_nombre():
    """Pregunta el nombre del usuario y lo guarda."""
    global nombre_usuario
    hablar("¿Cómo te llamas?")
    nombre_usuario = escuchar()
    if nombre_usuario:
        hablar(f"Encantado de conocerte, {nombre_usuario}.")
    else:
        hablar("No pude entender tu nombre. Por favor, inténtalo de nuevo.")
        pedir_nombre()

def ejecutar_asistente():
    """Función principal que ejecuta el asistente de voz."""
    global nombre_usuario
    saludo = saludar()
    hablar(f"{saludo}, soy Otto, tu asistente médico.")
    pedir_nombre()

    while True:
        hablar(f"{nombre_usuario}, ¿en qué puedo ayudarte?")
        texto_reconocido = escuchar()

        if texto_reconocido and "otto" in texto_reconocido:
            if any(palabra_clave in texto_reconocido for palabra_clave in ["ver un video", "abrir youtube", "youtube"]):
                hablar("Abriendo YouTube.")
                abrir_youtube()
            else:
                hablar("Lo siento, no entendí tu solicitud. Por favor, inténtalo de nuevo.")
        else:
            hablar("Recuerda mencionar 'Otto' antes de hacer una solicitud.")

ejecutar_asistente()
