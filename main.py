import speech_recognition as sr
from googletrans import Translator

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def translate_text(text, target_language='hi'):  # 'hi' is the code for Hindi
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translation to Hindi: {translation.text}")

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        translate_text(recognized_text, target_language='hi')
