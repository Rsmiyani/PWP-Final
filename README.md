🗣️ Voice Assistant in Python

A simple yet powerful Voice Assistant built using Python that listens to your voice commands and performs various tasks like opening websites, playing music, and running apps — all hands-free!

🚀 Features

✅ Speech Recognition – Listens to your commands using your microphone.
✅ Text-to-Speech (TTS) – Speaks back responses using pyttsx3.
✅ Web Control – Opens websites like Google, YouTube, Instagram, Gmail, and GitHub.
✅ App Launcher – Opens local applications like Notepad, Calculator, and Chrome.
✅ Music Player – Plays your favorite songs from a given file path.
✅ Time Announcement – Tells you the current time.
✅ Smart Error Handling – Responds politely when it doesn’t understand your command.

🧠 Technologies Used

Python 3.13+

speech_recognition – for recognizing speech from the microphone

pyttsx3 – for converting text to speech

datetime – for fetching and announcing the current time

webbrowser – for opening websites

os – for running system commands

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/Rsmiyani/PWP-Final.git
cd PWP-Final


Install the required dependencies

pip install -r requirements.txt


Run the Voice Assistant

python voice_assistant.py

🎧 Usage

Once the program starts, say one of the following commands:

Command	Action
"What is the time"	Tells the current time
"Open Google"	Opens Google in your browser
"Open YouTube"	Opens YouTube
"Open Instagram"	Opens Instagram
"Open Gmail"	Opens Gmail
"Open GitHub"	Opens GitHub
"Open Notepad"	Launches Notepad
"Open Calculator"	Launches Calculator
"Open Chrome"	Opens Google Chrome
"Play music"	Plays your music file
"Exit" / "Stop"	Quits the assistant
🎵 Change Music Path

To play your own song, update the line below inside the code:

music_path = "C:\\Path\\To\\Your\\MusicFile.mp3"

🧩 Example Output
Listening...
You said: open youtube
Opening YouTube


The assistant will speak:

“Opening YouTube”

💡 Future Improvements

Add weather and news updates

Add system control commands (volume, brightness, etc.)

Integrate with ChatGPT or GPT models for smart conversations

Add GUI interface

👨‍💻 Author

Rudra Miyani
📍 Marwadi University
💻 GitHub: Rsmiyani

Would you like me to make this README visually enhanced (with icons, badges, and color highlights) for GitHub?
I can turn it into a stylish markdown version next.
