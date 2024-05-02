from tkinter import *
from tkinter import messagebox
from tkinter import ttk as tk
import os
import model
import qrcode

def create_app(title):
    root = Tk()
    root.title(title)
    frm = tk.Frame(root, padding=10)
    frm.grid()

    tk.Label(frm, text="Para gerar o QR Code, preencha os seguintes campos.").grid(column=1, row=0)

    tk.Label(frm, text="Endereço Web:").grid(column=0, row=1)
    data_entry = tk.Entry(frm)
    data_entry.grid(column=1, row=1)

    tk.Label(frm, text="Salvar como:").grid(column=0, row=2)
    save_entry = tk.Entry(frm)
    save_entry.grid(column=1, row=2)

    tk.Button(frm, text="Gerar QR", command=lambda: generate_qr(data_entry.get(), save_entry.get())).grid(column=1, row=4)
    root.mainloop()


def generate_qr(data_address, save_entry):
    if is_http_link(data_address):
        object_qr = model.Qrcode(data_address=data_address, qr = qrcode.QRCode(version=1, box_size=10, border=4), save_address=f"media/qrs/{save_entry}.png")
        object_qr.create_qr()
    else:
        confirmar = messagebox.askyesno("Confirmação", "Não é um link HTTP. Tem certeza que deseja prosseguir?")
        if confirmar:
            object_qr = model.Qrcode(data_address=data_address, qr = qrcode.QRCode(version=1, box_size=10, border=4), save_address=f"media/qrs/{save_entry}.png")
            object_qr.create_qr()
        else: 
            messagebox.showinfo("Cancelado", "Operação cancelada.")


def is_http_link(string):
    if string.startswith("http://") or string.startswith("https://"):
        return True
    else:
        return False

create_app(title="Gerador de QR Code")

'''
    fill: str = field(default="black")
    back_color: str = field(default="white")
'''