import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    log.insert(tk.END, "Menunggu koneksi client...\n")
    status_label.config(text="Status: Menunggu koneksi...", fg="orange")

    conn, addr = server_socket.accept()
    log.insert(tk.END, f"Terhubung dengan {addr}\n")
    status_label.config(text=f"Status: Terhubung dengan {addr}", fg="green")

    def handle_client():
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                log.insert(tk.END, f"Client: {data}\n")
                conn.send(f"Pesan diterima: {data}".encode())
            except:
                break

    threading.Thread(target=handle_client, daemon=True).start()

# GUI
window = tk.Tk()
window.title("TCP Server")
window.configure(bg="#f0f0f0")
window.resizable(False, False)

frame = tk.Frame(window, bg="#f0f0f0", padx=10, pady=10)
frame.pack()

title = tk.Label(frame, text="TCP Server", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

status_label = tk.Label(frame, text="Status: Belum berjalan", font=("Helvetica", 10), bg="#f0f0f0", fg="red")
status_label.grid(row=1, column=0, columnspan=2, sticky="w")

log = scrolledtext.ScrolledText(frame, width=50, height=20, font=("Consolas", 10), bg="#fff")
log.grid(row=2, column=0, columnspan=2, pady=5)

btn_start = tk.Button(frame, text="Mulai Server", bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"), command=lambda: threading.Thread(target=start_server).start())
btn_start.grid(row=3, column=0, pady=10)

btn_clear = tk.Button(frame, text="Clear Log", bg="#f44336", fg="white", font=("Helvetica", 10), command=lambda: log.delete(1.0, tk.END))
btn_clear.grid(row=3, column=1, pady=10)

window.mainloop()
