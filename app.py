from flask import Flask, render_template, request, send_file
import pyttsx3
import os
from googletrans import Translator

app = Flask(__name__)
translator = Translator()
engine = pyttsx3.init()

@app.route("/", methods=["GET", "POST"])
def home():
    translation = ""
    if request.method == "POST":
        text = request.form["text"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        if text:
            # Translate the text
            translated_text = translator.translate(text, src=source_lang, dest=target_lang)
            translation = translated_text.text

            # Save the translated text to a temporary file for Text-to-Speech
            with open("temp_translation.txt", "w", encoding="utf-8") as file:
                file.write(translation)

    return render_template("index.html", translation=translation)

@app.route("/speak", methods=["GET"])
def speak():
    try:
        # Read the translated text from the file
        with open("temp_translation.txt", "r", encoding="utf-8") as file:
            text_to_speak = file.read()

        # Generate the speech and save to a file in the 'static' folder
        audio_path = "static/translated_audio.mp3"
        engine.save_to_file(text_to_speak, audio_path)
        engine.runAndWait()

        # Send the generated audio file to the client
        return send_file(audio_path, mimetype="audio/mp3")

    except Exception as e:
        return f"Error generating speech: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)