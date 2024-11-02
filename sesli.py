import speech_recognition as sr
import pyttsx3

# Sesli yanıt verme için pyttsx3'i ayarlayın
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    # Ses tanıyıcıyı oluştur
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinliyorum...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='tr-TR')
        print(f"Algılanan komut: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Anlayamadım, lütfen tekrar deneyin.")
        return None
    except sr.RequestError as e:
        print(f"Servis hatası: {e}")
        return None

def chat():
    print("Sohbete başlamak için 'merhaba' deyin.")
    while True:
        command = listen()
        if command:
            if "merhaba" in command:
                speak("Merhaba! Nasılsın?")
            elif "nasılsın" in command:
                speak("Ben bir yapay zeka, ama senin için buradayım!")
            elif "görüşürüz" in command:
                speak("Görüşürüz! İyi günler.")
                break
            else:
                speak("Bunu anlayamadım, lütfen başka bir şey söyle.")

if __name__ == "__main__":
    chat()
