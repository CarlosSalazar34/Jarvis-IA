import sounddevice as sd
import speech_recognition as sr
import scipy.io.wavfile as wav
import io
import pyttsx3

engine = pyttsx3.init()

def say_message(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar_voz():
    fs = 44100  # Frecuencia de muestreo
    segundos = 10 # Cuánto tiempo escuchará cada vez
    
    print(f"Escuchando por {segundos} segundos...")
    
    # Capturar el audio desde el micrófono
    grabacion = sd.rec(int(segundos * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Esperar a que termine la grabación
    
    # Convertir la grabación en un formato que SpeechRecognition entienda
    byte_io = io.BytesIO()
    wav.write(byte_io, fs, grabacion)
    byte_io.seek(0)
    
    # Usar SpeechRecognition para traducir el audio a texto
    r = sr.Recognizer()
    with sr.AudioFile(byte_io) as source:
        audio_data = r.record(source)
        try:
            texto = r.recognize_google(audio_data, language="es-ES")
            print(f"Jarvis entendió: {texto}")
            say_message(texto)
            return texto
        except sr.UnknownValueError:
            print("No se entendió el audio")
        except sr.RequestError:
            print("Error de conexión")

# Ejecutar
escuchar_voz()