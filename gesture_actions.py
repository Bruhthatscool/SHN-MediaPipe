import webbrowser

def open_application(gesture):
    if gesture.category_name == "Thumb_Up":
        webbrowser.open("https://youtube.com")
    elif gesture.category_name == "Thumb_Down":
        webbrowser.open("https://google.com")
        