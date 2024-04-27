# pip install eel
import eel

eel.init('GUI')  # Give folder containing web files

@eel.expose
def App():
    print("Application Running")

App()

eel.start('index.html',size=(500,600))