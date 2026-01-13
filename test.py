import speech_recognition as sr

# Crear reconocedor
r = sr.Recognizer()

# Usar micrófono
with sr.Microphone() as source:
    print("Habla ahora...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language="es-ES")
    print("Dijiste:", texto)
except sr.UnknownValueError:
    print("No entendí el audio")
except sr.RequestError:
    print("Error con el servicio de reconocimiento")
