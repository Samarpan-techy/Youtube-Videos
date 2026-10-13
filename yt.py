import pyttsx3
import pywhatkit
import ctypes

# Speech Engine Setup (AI bolega, lekin sunege hum text ke zariye)
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Bolne ki speed

def speak(text):
    print(f"AI: {text}")
    engine.say(text)
    engine.runAndWait()

def set_full_volume():
    # Windows system volume ko 100% karne ke liye
    WM_APPCOMMAND = 0x319
    APPCOMMAND_VOLUME_UP = 0x0A
    for _ in range(50):
        ctypes.windll.user32.SendMessageW(0xFFFF, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP << 16)

def main():
    speak("Hello! What do you want to do?")
    user_intent = input("You: ").lower()

    if "watch video" in user_intent or "video" in user_intent or "youtube" in user_intent:
        speak("Which video would you like to watch?")
        video_name = input("Enter video name: ")
        
        if video_name.strip():
            speak("Setting volume to full...")
            set_full_volume()
            
            speak(f"Playing {video_name} on YouTube.")
            pywhatkit.playonyt(video_name)
        else:
            speak("No video name provided.")
    else:
        speak("I didn't understand that command.")

if __name__ == "__main__":
    main()