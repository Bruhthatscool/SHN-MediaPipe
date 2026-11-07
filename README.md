# SHN-MEDIAPIPE
![Project Cover](assets/cover.jpeg)

# OPEN SESAME

### 💡 What's the idea?

An interactive, real-time hand gesture recognition system built using **Google MediaPipe** and **OpenCV** that maps physical hand gestures from your webcam to custom actions—such as launching websites or applications instantly with just a flick of your hand!

### 🌐 Check it out!

* **GitHub Repo:** [https://github.com/Bruhthatscool/SHN-MediaPipe](https://github.com/Bruhthatscool/SHN-MediaPipe)

### 🛠️ What did you use?

* **Python**
* **Google MediaPipe** (Vision Tasks / Gesture Recognizer)
* **OpenCV** (Webcam video capture & real-time UI display)
* **Webbrowser** (For gesture-triggered application/URL launching)

### 👥 The Humans Behind It

* Asher Thomas – [achutom](https://github.com/achutom)
* Anna Grace – [bruhthatscool](https://www.google.com/search?q=https://github.com/bruhthatscool)

### 📸 Show Us What You Built!

*(Add screenshots, photos, GIFs, or demo video links here)*

### ✨ Cool Things It Does

* **Real-Time Async Processing:** Uses MediaPipe's live stream mode with an asynchronous callback structure to automatically drop busy frames and keep tracking smooth and responsive.
* **Dynamic Gesture Triggering:** Detects hand gestures via webcam and triggers custom actions only when the gesture changes (e.g., thumbs up opens YouTube, thumbs down opens Google).
* **Multi-Hand Support:** Configured to track up to two hands concurrently for robust detection.

---

## 🚀 How to Run Locally

Want to try this project out on your own machine? Follow these steps:

### 1. Fork & Clone the Repository

First, go to the [GitHub Repository](https://github.com/Bruhthatscool/SHN-MediaPipe), click the **Fork** button in the top right corner to copy it to your GitHub account, and then clone your forked repository:

```bash
git clone https://github.com/YOUR-USERNAME/SHN-MediaPipe.git
cd SHN-MediaPipe

```

### 2. Set Up a Python Virtual Environment

It's recommended to run the project inside a virtual environment to keep your packages isolated:

```bash
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate

# On Windows (Command Prompt):
venv\Scripts\activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

```

### 3. Install Dependencies

Install the required libraries (`mediapipe`, `opencv-python`, and `numpy`):

```bash
pip install mediapipe opencv-python numpy

```

### 4. Add the Model File

Make sure you have the MediaPipe gesture recognition model file (`gesture_recognizer.task`) placed in the root directory of the project alongside your script.

### 5. Run the Project

Fire up the script and wave at your webcam!

```bash
python main.py

```

*(Press `q` in the webcam preview window to exit at any time).*

---

**Built with curiosity at Saturday Hack Night 💜**
