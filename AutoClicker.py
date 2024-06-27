from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
from time import sleep
import threading

print("Auto clicker ligado aperta F7")
mouse_controller = Controller()
is_clicking = False

def on_press(key):
    global is_clicking
    try:
        if key == keyboard.Key.F7:
            is_clicking = not is_clicking
            print(f"Auto clicker is {'on' if is_clicking else 'off'}")
    except Exception as e:
        print(e)

def autoclicker():
    while True:
        if is_clicking:            
            mouse_controller.press(Button.left)
            mouse_controller.release(Button.left)
            print("krikaste")
            sleep(2.5)

# Listener do teclado em uma thread separada
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Auto clicker em uma thread separada
autoclicker_thread = threading.Thread(target=autoclicker)
autoclicker_thread.start()

# Mantendo o programa em execução
keyboard_listener.join()
autoclicker_thread.join()