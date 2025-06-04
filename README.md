# streamlit-tts-translator
A Streamlit app that translates text and converts it to speech using gTTS and Google Translate.
# 🗣️ Streamlit Text Translator & Speech Synthesizer

This is a fun and functional Streamlit web app that **translates English text into any target language** and then **converts it into speech** using Google Text-to-Speech (gTTS). Perfect for language learning, accessibility, or just experimenting with AI!

---

## 🚀 Features

- 🔤 Translate English to over 30 languages
- 🎧 Generate speech in the translated language
- 🌍 Streamlit UI for real-time interaction
- 🧠 Built using NLP tools like `googletrans`, `gTTS`, and `Streamlit`

---

## 🧪 How to Run the App in Google Colab

You can easily run this app in Google Colab using LocalTunnel for public access. Follow the steps below 👇

### 🔧 Step 1: Install Dependencies

!pip install streamlit transformers torch gTTS googletrans==4.0.0-rc1 requests

### 📝 Step 2: Create the app.py File

%%writefile app.py

Paste your full Streamlit code here

### 🌐 Step 3: Get Your Public IP 

!wget -q -O - ipv4.icanhazip.com

### 🚀 Step 5: Run Streamlit and Open Tunnel

!streamlit run app.py & npx localtunnel --port 8501

You’ll get a public URL like https://random-name.loca.lt — click it to view your app from anywhere in the world.

🛠️ Tech Stack
Frontend: Streamlit

Speech: gTTS (Google Text-to-Speech)

Translation: googletrans (unofficial Google Translate API)

Extras: torch, transformers
