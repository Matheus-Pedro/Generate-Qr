from tkinter import *
from tkinter import ttk

def send(data_entry, save_entry):
    print(data_entry, save_entry)

def create_app():
    root = Tk()
    root.title("Gerador de QR Code")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text="Gerar um QR Code").grid(column=1, row=0)

    ttk.Label(frm, text="Endereço Web:").grid(column=0, row=1)
    data_entry = ttk.Entry(frm)
    data_entry.grid(column=1, row=1)

    ttk.Label(frm, text="Salvar como:").grid(column=0, row=2)
    save_entry = ttk.Entry(frm)
    save_entry.grid(column=1, row=2)

    ttk.Button(frm, text="Enviar", command=lambda: send(data_entry.get(), save_entry.get())).grid(column=1, row=4)
    root.mainloop()

'''
    fill: str = field(default="black")
    back_color: str = field(default="white")
'''