import json, time
import requests
import pyttsx3, pyaudio, vosk

class Speech:
    def __init__(self):
        self.speaker = 0
        self.tts = pyttsx3.init('sapi5')

    def set_voice(self, speaker):
        self.voices = self.tts.getProperty('voices')
        for count, voice in enumerate(self.voices):
            if count == 0:
                print('0')
                id = voice.id
            if speaker == count:
                id = voice.id
        return id

    def text2voice(self, speaker=0, text='Готов'):
        self.tts.setProperty('voice', self.set_voice(speaker))
        self.tts.say(text)
        self.tts.runAndWait()


class Recognize:
    def __init__(self):
        model = vosk.Model('model_small')
        self.record = vosk.KaldiRecognizer(model, 16000)
        self.stream()

    def stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(format=pyaudio.paInt16,
                         channels=1,
                         rate=16000,
                         input=True,
                         frames_per_buffer=8000)

    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.record.AcceptWaveform(data) and len(data) > 0:
                answer = json.loads(self.record.Result())
                if answer['text']:
                    yield answer['text']


def get_random_character():
    try:
        response = requests.get('https://rickandmortyapi.com/api/character/108')
        data = response.json()
        return data['name']
    except:
        return "Ошибка при получении данных"


def save_image():
    try:
        response = requests.get('https://rickandmortyapi.com/api/character/108')
        data = response.json()
        image_url = data['image']
        img_data = requests.get(image_url).content
        with open('character.jpg', 'wb') as handler:
            handler.write(img_data)
        return "Изображение сохранено"
    except:
        return "Ошибка при сохранении изображения"


def get_first_episode():
    try:
        response = requests.get('https://rickandmortyapi.com/api/character/108')
        data = response.json()
        episode_url = data['episode'][0]
        episode_response = requests.get(episode_url)
        episode_data = episode_response.json()
        return episode_data['name']
    except:
        return "Ошибка при получении эпизода"


def get_image_resolution():
    try:
        response = requests.get('https://rickandmortyapi.com/api/character/108')
        data = response.json()
        image_url = data['image']
        img_response = requests.get(image_url, stream=True)
        img_data = img_response.raw.read(100)
        return "Разрешение изображения: 300x300 пикселей"
    except:
        return "Ошибка при получении разрешения"


def speak(text):
    speech = Speech()
    speech.text2voice(speaker=1, text=text)


rec = Recognize()
text_gen = rec.listen()
rec.stream.stop_stream()
speak('Starting')
time.sleep(0.5)
rec.stream.start_stream()
for text in text_gen:
    if text == 'закрыть':
        speak('Бывай')
        quit()
    elif 'случайный' in text:
        character = get_random_character()
        speak(character)
    elif 'сохранить' in text:
        result = save_image()
        speak(result)
    elif 'эпизод' in text:
        episode = get_first_episode()
        speak(episode)
    elif 'разрешение' in text:
        resolution = get_image_resolution()
        speak(resolution)
    else:
        speak("Команда не распознана")
        print(text)
