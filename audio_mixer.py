from pydub import AudioSegment

song = AudioSegment.from_mp3("/home/msolorzanoc/Music/song.mp3")
voice = AudioSegment.from_wav("/home/msolorzanoc/Music/voice.wav")

# output = song.overlay(voice, position=0)
output = song.overlay(voice)

output.export("/home/msolorzanoc/Music/result.mp3", format="mp3")
