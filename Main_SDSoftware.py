from tkinter.filedialog import *
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from deep_translator import GoogleTranslator
from gtts import gTTS
import moviepy.editor as mpe
import os

def mainSDS():
    # from desktop for file access use askopenfilename()
    enteredVideoFile = askopenfilename()

    AudioClipFile = AudioFileClip(enteredVideoFile)
    # declaration of TranscribedAudioFileName
    TranscribedAudioFileName = "GeneratedSpeech.wav"
    AudioClipFile.write_audiofile(TranscribedAudioFileName)

    '''
        "LOGIC PART"
        duration = frameNumber / float(frameRate) 
        total_duration = math.ceil(duration / 60)
    '''
    with contextlib.closing(wave.open(TranscribedAudioFileName, 'r')) as file:
        # using getnframes(), for find the no of frame
        frameNumber = file.getnframes()
        # using getframerate(), for find the rate of frame
        frameRate = file.getframerate()
        duration = frameNumber / float(frameRate)
        total_duration = math.ceil(duration / 60)
        recognizeVoice = sr.Recognizer()

    ''' 
        "LOGIC PART"
        audio = r.record(source, offset=i*60, duration=60
     '''
    for i in range(0, total_duration):
        with sr.AudioFile(TranscribedAudioFileName) as source:
            audio = recognizeVoice.record(source, offset=i * 60, duration=60)
        Text_file = open("generatedTxtFile.txt", "a")
        Text_file.write(recognizeVoice.recognize_google(audio))
        Text_file.write(" ")
        Text_file.close()
    print(".mp4 to .txt okay...")

    # translation english to hindi
    translatedHindi = GoogleTranslator(source='english', target='hindi').translate_file('generatedTxtFile.txt')
    # print(translatedHindi)
    print("translation okay...")

    # Hindi text to hindi mp3
    language = 'hi'
    output = gTTS(text=translatedHindi, lang=language, slow=False)
    output.save("TranslatedHindiVoice.mp3")
    print("Hindi text to mp3 okay...")

    # Overlap the video and audio
    print("Video & Audio Overlap Started... ")

    def combine_audio(vidname, audname, outname, fps=60):
        my_clip = mpe.VideoFileClip(vidname)
        audio_background = mpe.AudioFileClip(audname)
        final_clip = my_clip.set_audio(audio_background)
        final_clip.write_videofile(outname, fps=fps)

    combine_audio(enteredVideoFile, "TranslatedHindiVoice.mp3","Converted.mp4")
    print("Video & Audio Overlap Successfully okay...")

    # remove .txt, .wav, .mp3 file

    directory = os.getcwd()
    test = os.listdir(directory)

    for item in test:
        if item.endswith(".mp3"):
            os.remove(os.path.join(directory, item))

    for item in test:
        if item.endswith(".wav"):
            os.remove(os.path.join(directory, item))
    for item in test:
        if item.endswith(".txt"):
            os.remove(os.path.join(directory, item))