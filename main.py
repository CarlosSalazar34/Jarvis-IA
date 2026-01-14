from openai import OpenAI
from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)   # velocidad de voz
engine.setProperty("volume", 1.0) # volumen
voices = engine.getProperty("voices")
for voice in voices:
    if "spanish" in voice.name.lower() or "es" in voice.id.lower():
        engine.setProperty("voice", voice.id)
        break

def escuchar():
    with sr.Microphone() as source:
        print("Escuchando")
        audio = r.listen(source=source)
    try:
        texto = r.recognize_google(audio, language="es-ES")
        return texto
    except sr.UnknownValueError:
        return "No se entendio"
    except sr.RequestError:
        return "Error en el serrvicio de reconocimiento"

def main() -> None:
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    messages = [
        {"role": "system", "content": "Eres un chatbot amable y útil."}
    ]

    print("🤖 Chatbot iniciado (escribe 'salir' para terminar)\n")

    while True:
        user_input = escuchar()

        if user_input.lower() in ["salir", "terminar"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print("Pensando...")
        print(f"Bot: {reply}\n")
        engine.stop()
        engine.say(reply.replace("*", ""))
        engine.runAndWait()



if __name__ == "__main__":
    main()
