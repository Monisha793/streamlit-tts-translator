 # app.py

import streamlit as st
from gtts import gTTS
from googletrans import Translator
from io import BytesIO

# Define the speech synthesis class
class SpeechSynthesis:
    def __init__(self, text, target_lang, source_lang='en'):
        self.text = text
        self.target_lang = target_lang
        self.source_lang = source_lang
        self.translator = Translator()

    def translate_text(self):
        translated = self.translator.translate(self.text, src=self.source_lang, dest=self.target_lang)
        return translated.text

    def synthesize(self):
        translated_text = self.translate_text()
        tts = gTTS(text=translated_text, lang=self.target_lang)
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return translated_text, audio_file

# Streamlit UI
st.set_page_config(page_title="🗣️ Text Translator & Speech Synthesizer", layout="centered")
st.title("🗣️ Translate and Speak Your Text")

# Input fields
text_input = st.text_area("Enter your text here:", "Hello! How are you today?")
source_lang = st.selectbox("Select source language", options=["en", "hi", "ta", "te", "mr", "fr", "es", "de", "ja"], index=0)
target_lang = st.selectbox("Select target language", options=["hi", "ta", "te", "mr", "fr", "es", "de", "ja"], index=4)

# Run translation and TTS
if st.button("Translate & Speak"):
    with st.spinner("Translating and generating speech..."):
        try:
            synth = SpeechSynthesis(text=text_input, target_lang=target_lang, source_lang=source_lang)
            translated_text, audio_data = synth.synthesize()
            st.success("✅ Translation and Audio Ready!")

            # Show results
            st.write(f"**Translated Text ({target_lang}):** {translated_text}")
            st.audio(audio_data, format='audio/mp3')
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
