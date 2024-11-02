import speech_recognition as sr
import webbrowser
import subprocess

def listen_for_commands():
    # Ses tanıyıcıyı oluştur
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Komut bekleniyor...")
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

def open_youtube():
    # Firefox'u aç ve YouTube'a git
    webbrowser.get('firefox').open('https://www.youtube.com')

def open_google():
    # Firefox'u aç ve Google'a git
    webbrowser.get('firefox').open('https://www.google.com')

def open_cheese():
    # Cheese uygulamasını başlat
    subprocess.run(['cheese'])

if __name__ == "__main__":
    while True:
        command = listen_for_commands()
        if command:
            if "youtube aç" in command:
                open_youtube()
            elif "google aç" in command:
                open_google()
            elif "peynir" in command:
                open_cheese()
            elif "çık" in command:
                print("Uygulama kapatılıyor...")
                break
