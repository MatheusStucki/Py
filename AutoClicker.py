import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
from pynput.mouse import Button, Controller
from time import sleep
import threading

# Variaveis
mouse_controller = Controller()
is_clicking = False
num = 0.0
total_clicks = 0

# função pra ligar e desligar
def toggle_autoclicker():
    global is_clicking
    is_clicking = not is_clicking
    status_label.config(text=f"Auto Cilicker: {'Ligado' if is_clicking else 'Desligado'}")

# função para setar o tempo de atraso por clicks
def set_num():
    global num
    try:
        num = float(num_var.get())
        messagebox.showinfo("Information", f"Atraso por click: {num} segundos")
    except ValueError:
        messagebox.showerror("Error", "Entre um numero valido")

# função do auto clicker
def autoclicker():
    global num, total_clicks
    while True:
        if is_clicking:            
            mouse_controller.press(Button.left)
            mouse_controller.release(Button.left)
            total_clicks += 1
            click_label.config(text=f"Apertou um total de {total_clicks} x")
            sleep(num)
        else:
            sleep(0.1)

# Função para ligar pela tecla F7 tambem (irei fazer configuravel quando aprender a mexer melhor no tkinter)
def on_press(key):
    try:
        if key == keyboard.Key.f7:
            toggle_autoclicker()
    except Exception as e:
        print(e)

# Tela principal
root = tk.Tk()
root.title("Autoclicker.py")

# Tamanho da tela
root.geometry("300x250")

# Var para fazer uma entry no progama
num_var = tk.StringVar()

# A entry com a configuração do numvar para passar o tempo do sleep
entry = tk.Entry(root, textvariable=num_var, width=25)
entry.pack(pady=20)

# Botão para ir para telar pra settar o tempo
set_button = tk.Button(root, text="Tempo de clicks por segundo", command=set_num)
set_button.pack(pady=10)

# Botão para ligar/desligar
toggle_button = tk.Button(root, text="Ligar Autoclicker (F7 tambem funciona)", command=toggle_autoclicker)
toggle_button.pack(pady=10)

# Mostrar o status do auto clicker
status_label = tk.Label(root, text="Auto clicker esta ligado")
status_label.pack(pady=10)

# Label to show the total number of clicks
click_label = tk.Label(root, text=f"Apertou um total de {total_clicks} vezes")
click_label.pack(pady=10)

# Thread para o autoclicker
autoclicker_thread = threading.Thread(target=autoclicker, daemon=True)
autoclicker_thread.start()

# keyboard_listener para reconhecer as tecla do teclado sempre
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Aplicação do tkinter
root.mainloop()
