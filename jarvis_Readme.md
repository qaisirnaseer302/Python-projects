Jarvis Voice Assistant 🗣️🤖

A simple Python-based voice assistant that listens for the wake word “Jarvis” and can:

✅ Open websites (Google, YouTube, Facebook, Instagram)

✅ Play music from a predefined library

✅ Tell a random joke

✅ Perform basic calculations using voice commands

✅ Tell the current time, date, day, month, and year

✅ Speak all responses aloud using text-to-speech

==> Features :

Speech Recognition: Uses your microphone to listen for commands.

Text-to-Speech: Speaks responses using pyttsx3.

Web Integration: Opens commonly used websites on command.

Music Player: Plays songs from your musiclibrary.

Joke Generator: Fetches a random joke from pyjokes.

Date & Time Info: Tells the current date, time, day, month, or year.

Simple Calculator: Supports addition, subtraction, multiplication, division, modulus, and power via voice commands.

==> Requirements : 
Install the following Python packages before running:


pip install SpeechRecognition pyttsx3 pyjokes pyaudio

You must also have a musiclibrary.py file structured with:

music = {
    "song_name": "youtube_url",
    ...
}
==> Usage :

1️⃣ Clone or download this repository.

2️⃣ Ensure your microphone is enabled and working.

3️⃣ Run:


python jarvis.py

4️⃣ Wait for:

wellcome....
recognizing....
Listening....

5️⃣ Say "Jarvis" to activate, then give your command.

==> Example commands:

“open google”

“open youtube”

“play care”

“tell me a joke”

“what is the time”

“what is the date”

“calculate 5 plus 3”

“calculate 10 divided 2”

Say “exit” during the command phase to stop Jarvis.

File Structure

jarvis.py – Main Jarvis assistant code.

musiclibrary.py – Your custom song list for playing music by name.

==> Notes


✅ Requires internet access for speech recognition.

✅ Uses Google’s free speech recognition API via the speech_recognition module.

✅ Keep your environment quiet while using to avoid recognition errors.

✅ You can expand it to handle more commands like sending emails, fetching weather, etc., for practice.

==> License :

This project is for educational and personal use. Feel free to modify and expand it as your personal Python voice assistant project.