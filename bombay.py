import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Google Speech Recognition request failed: {e}")
        return ""

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def play_tomake():
    song_url = "https://youtu.be/FuLWFwfXFwQ?si=41-zZvyrJvqL1ZBw"
    webbrowser.open(song_url)

def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg(number, message, 0, 0)  # Send a WhatsApp message

def varsity_bio():
    bio_text = "I am a proud student of Bangladesh University of Business and Technology (BUBT). " \
                "BUBT is renowned for its commitment to providing high-quality education in various disciplines, " \
                "with a focus on preparing students for the challenges of the professional world. " \
                "The university's diverse and vibrant community, along with its dedicated faculty, " \
                "creates an environment that fosters learning, innovation, and personal growth."
    speak(bio_text)

def hey_bombay_response():
    speak("yes chief! How can I assist you today?")

def main():
    speak("Hello! I'm Bombay. How can I assist you chief?")

    while True:
        command = recognize_speech()

        if "exit" in command:
            speak("Goodbye chief!")
            break
        elif "open google" in command:
            speak("Opening Google.")
            open_google()
        elif "open youtube" in command:
            speak("Opening YouTube.")
            open_youtube()
        elif "play tomake" in command:
            speak("Playing Tomake by Artcell on YouTube.")
            play_tomake()
        elif "send message" in command:
            speak("To whom do you want to send a message?")
            contact = recognize_speech()
            speak("What message do you want to send?")
            message_content = recognize_speech()
            send_whatsapp_message(contact, message_content)
            speak(f"Message sent to {contact}.")
        elif "tell me about my varsity" in command:
            varsity_bio()
        elif "hey bombay" in command:
            hey_bombay_response()
        else:
            speak(f"You said: {command}")

if __name__ == "__main__":
    main()

#by mayday
