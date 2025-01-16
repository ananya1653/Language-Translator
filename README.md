# Language-Translator
This project is a Language Translator web application that allows users to translate text from one language to another. It also includes Speech-to-Text (STT) and Text-to-Speech (TTS) integration, enabling users to speak text that will be translated and then listen to the translated text.
# Features
Text Translation: Translate text from one language to another using the Google Translate API.
Speech-to-Text: Capture spoken text and fill the text input automatically using the browser's Speech Recognition API.
Text-to-Speech: Convert translated text to speech using the pyttsx3 library, and play it in the browser.
# Technologies Used
Flask: A lightweight Python web framework to build the backend.
Google Translate API: For translating text between different languages.
pyttsx3: For converting text to speech.
Speech Recognition API: For capturing user speech and converting it to text (only supported in Google Chrome).
# Requirements
Python 3.x
Flask
pyttsx3
googletrans==4.0.0-rc1
A modern web browser (Google Chrome recommended)
# How it Works
# Speech-to-Text:

The user can speak by clicking the 🎤 Speak button. The Speech Recognition API captures the user's voice, converts it into text, and automatically fills the input text box.
Text Translation:

The user enters text or uses speech input, selects the source and target languages, and clicks the Translate button.
The translation is done using the Google Translate API and displayed below the input field.
# Text-to-Speech:

After the translation is complete, the 🔊 Listen button is enabled.
Clicking Listen generates the speech from the translated text and plays it using pyttsx3, allowing the user to listen to the translated text.
