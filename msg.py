import pywhatkit as kit
import pyautogui
# Número de teléfono con el código del país
numero_telefono = '+543873226948'

# Mensaje a enviar
msg = "Hola, esta es la prueba para mandar mensaje. Si te llegó, significa que funcionó."

# Envía el mensaje automáticamente de forma inmediata
kit.sendwhatmsg_instantly(numero_telefono, msg, wait_time=2)

pyautogui.press('enter')
print(f"Mensaje enviado a {numero_telefono}")

