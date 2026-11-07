import webbrowser

def open_youtube(gesture):
    if gesture.category_name == "Thumb_Up":
        webbrowser.open("https://youtube.com")
        