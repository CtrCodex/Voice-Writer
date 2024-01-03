import pyautogui
import speech_recognition as sr

class Dictation:
    def __init__(self):
        self.dictating = False
        self.mic = sr.Microphone()
        self.r = sr.Recognizer()
        self.stop_listening = None

    def start(self):
        self.dictating = True
        self.stop_listening = self.r.listen_in_background(self.mic, self.callback)
        print('Dictation Started!')
        
    def stop(self):
        if self.dictating:
            self.dictating = False
            self.stop_listening()
            print('Dictation Stopped!')

    def callback(self, recognizer, audio):
        try:
            words = recognizer.recognize_google(audio)
            if not self.dictating:
                return  # Stop listening if dictation was manually stopped
            if not any(keyword in words.lower() for keyword in ["stop", "dictate", "jarvis"]):
                print('You said: '+words)
                pyautogui.typewrite(words + ' ')
            else:
                self.stop()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Sorry, I am experiencing issues with speech recognition.')
        except Exception as e:
            print(e)

def test():
    d = Dictation()
    d.start()
    while d.dictating:
        pass
    d.stop()

def spell_word(input_text):
    output = (input_text + " is spelled ")

    for letter in input_text:
        output = output + letter + ", "
    return output.capitalize()


test()

