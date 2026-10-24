# 🎙️ Syntax Slayers — "Sara" Voice Assistant 🤖🏥

> ✨ Meet **Sara** — a voice-controlled AI assistant built at a hackathon 🏆, all in **one single Python file** 🐍. She listens through your microphone 🎤, chats using OpenAI 🧠, speaks her answers out loud 🔊, opens websites for you 🌐, and has a little healthcare streak — mention obesity, diabetes, malaria or cancer and she'll pull up the matching WebMD page for you 🩺.

![Python](https://img.shields.io/badge/Python-Single%20File%20Project-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenAI](https://img.shields.io/badge/OpenAI-Chat%20Brain-412991?style=for-the-badge&logo=openai&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/Speech-Recognition-blue?style=for-the-badge)
![Hackathon](https://img.shields.io/badge/Built%20At-A%20Hackathon-orange?style=for-the-badge)

---

## 📑 Table of Contents

- [📖 About](#-about)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [🚀 Getting Started](#-getting-started)
- [💻 Usage](#-usage)
- [🗣️ Voice Commands](#️-voice-commands)
- [⚠️ Good to Know](#️-good-to-know)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

## 📖 About

This is Team **Syntax Slayers'** hackathon build 🎉 — no framework, no fancy architecture, just one enthusiastic Python script: `final hackathon (1).py`.

Sara greets you out loud as soon as the script starts (*"Hello I am Sara, how may I help you today"* 👋), then sits in a listening loop. Everything you say goes one of three ways:

1. 🌐 It's a command she recognises → she opens a website for you
2. 🩺 It's a health topic she knows → she opens the matching WebMD page (or prints a support contact for "depression")
3. 💬 Anything else → she has a proper chat with you, powered by OpenAI, and reads the reply back to you 🔊

---

## ✨ Features

- 🎤 **Voice in** — microphone input via `SpeechRecognition`, transcribed with Google's recognizer (`en-in`)
- 🔊 **Voice out** — replies are spoken, not just printed
- 🧠 **OpenAI chat with memory** — the conversation is accumulated in a running transcript (`chatStr`), so Sara answers with context of what you both said 📜
- 📝 **Save an AI answer to a file** — a helper can write an OpenAI response into a `.txt` file inside an `Openai/` folder
- 🌐 **"Open …" commands** — say the word and she opens **YouTube**, **Wikipedia**, **Google**, or **Medical help (WebMD)** in your browser
- 🩺 **Health shortcuts** — obesity, diabetes, malaria and cancer open their WebMD pages; "depression" prints a call/WhatsApp contact number that's hardcoded in the script
- 🧹 **Reset chat** — say it and the conversation memory is wiped clean
- 👋 **"Sara Quit"** — the polite way to make her stop listening and exit

---

## 🛠️ Tech Stack

| Piece 🧩 | Used for 💡 |
|---|---|
| 🐍 **Python** | The whole thing — one script |
| 🎤 **SpeechRecognition** (`speech_recognition`) | Microphone capture + Google speech-to-text |
| 🧠 **OpenAI** (`openai`) | Chat & text generation (legacy Completion API, `text-davinci-003`) |
| 🔊 **pyttsx3** | Text-to-speech for Sara's greeting |
| 🔢 **NumPy** | Imported at the top of the script |
| 📚 Python standard library | `os`, `webbrowser` 🌐, `datetime`, `random` |

---

## 📂 Project Structure

```text
Syntax-Slayers/
└── final hackathon (1).py   🎙️ The entire assistant — Sara lives here!
```

That's genuinely it. One file, no folders, no config — hackathon style. 😄

---

## ⚙️ Prerequisites

- 🐍 **Python 3**
- 🎤 A working **microphone** (Sara can't help much without one 😅)
- 🔑 Your own **OpenAI API key** — see the notes in [⚠️ Good to Know](#️-good-to-know) before running
- 📦 The pip packages from the script's imports:

```bash
pip install SpeechRecognition openai pyttsx3 numpy
```

- 📁 A local **`apikey.py`** module — one helper in the script reads the key from a local module named `apikey`, and that file is *not* included in this repo (by design — keys shouldn't be committed 🔐). Create your own `apikey.py` next to the script if you use that helper.
- 🍎 **macOS note:** Sara's `say()` helper uses the macOS `say` command 🔊, while the startup greeting uses `pyttsx3` — keep that split in mind if you're running her on Windows/Linux.

---

## 🚀 Getting Started

```bash
# 1️⃣ Clone the repo 📥
git clone https://github.com/rajdeepkumar200/Syntax-Slayers.git
cd Syntax-Slayers

# 2️⃣ Install the dependencies 📦
pip install SpeechRecognition openai pyttsx3 numpy

# 3️⃣ Add your OpenAI key 🔑 (in the script / your own apikey.py — never commit it!)

# 4️⃣ Run Sara 🎙️ (mind the spaces & brackets in the file name — keep the quotes!)
python "final hackathon (1).py"
```

She'll greet you out loud 🎉, then start listening. Just… talk to her. 💬

---

## 💻 Usage

No menus, no buttons — the interface is your voice 🗣️:

1. ▶️ Run the script → Sara says hello through `pyttsx3`
2. 🎤 Wait for *"Listening…"*, then speak
3. 🌐 Try *"Open YouTube"* → browser opens YouTube
4. 🩺 Try *"diabetes"* → browser opens the WebMD diabetes page
5. 💬 Ask her anything else → she chats via OpenAI and reads the answer aloud
6. 👋 Say *"Sara Quit"* when you're done

---

## 🗣️ Voice Commands

| Say this 🎙️ | Sara does this 🤖 |
|---|---|
| *"Open YouTube"* | 🌐 Opens youtube.com |
| *"Open Wikipedia"* | 🌐 Opens wikipedia.com |
| *"Open Google"* | 🌐 Opens google.com |
| *"Open Medical help"* | 🩺 Opens webmd.com |
| *"Depression"* | 📞 Prints a call/WhatsApp contact number (hardcoded in the script) |
| *"Obesity"* / *"Diabetes"* / *"Malaria"* / *"Cancer"* | 🩺 Opens the matching WebMD topic page |
| *"Reset chat"* | 🧹 Clears the conversation memory |
| *"Sara Quit"* | 👋 Exits the assistant |
| Anything else 💬 | 🧠 Falls through to OpenAI chat, reply spoken aloud |

---

## ⚠️ Good to Know

A few honest hackathon-grade caveats 🙏:

- 🕰️ **Legacy OpenAI API** — the script uses `openai.Completion.create(...)` with the `text-davinci-003` model, which is the old pre-1.0 style API. Expect to pin an older `openai` version — and note the model itself has since been retired by OpenAI, so the chat path will need a model/API update to work against today's OpenAI platform. The voice-command and WebMD parts don't depend on it. 👍
- 🔑 **API key handling** — the script expects an OpenAI key to be set in the code / in a local `apikey.py`. Always use **your own** key, and never commit it to a public repo.
- 🎧 **Speech recognition needs internet** — transcription goes through Google's recognizer, and recognition is set to English (India) 🇮🇳, `en-in`.

---

## 🤝 Contributing

This was a hackathon project, but improvements are still welcome! 🙌 Modernising the OpenAI calls would be a great first PR, just saying. 😄

1. 🍴 Fork the repo
2. 🌿 Create a branch (`git checkout -b feature/my-improvement`)
3. 💾 Commit your changes (`git commit -m "Add my improvement"`)
4. 📤 Push the branch (`git push origin feature/my-improvement`)
5. 🔀 Open a Pull Request

---

## 📄 License

📌 No `LICENSE` file is currently included in this repository, so no open-source license is claimed for this code yet. Please ask the author before reusing it beyond personal reference. 🙏

---

## 👨‍💻 Author

**Rajdeep Kumar Singh** 🎓 — Team Syntax Slayers ⚔️

- 🐙 GitHub — [@rajdeepkumar200](https://github.com/rajdeepkumar200)
- 💼 LinkedIn — [rajdeep-kumar-singh-ai](https://www.linkedin.com/in/rajdeep-kumar-singh-ai)

---

<p align="center">⭐ Sara would say it herself if she could — thanks for stopping by! ⭐</p>
<p align="center">🎙️ One file. One voice. One hackathon. 🏆</p>
