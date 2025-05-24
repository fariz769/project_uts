import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12346)

# GUI
window = tk.Tk()
window.title("UDP Client")
window.configure(bg="#f0f0f0")
window.resizable(False, False)

frame = tk.Frame(window, bg="#f0f0f0", padx=10, pady=10)
frame.pack()

title = tk.Label(frame, text="UDP Client", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title.grid(row=0, column=0, columnspan=3, pady=(0, 10))

status_label = tk.Label(frame, text="Status: Siap mengirim", font=("Helvetica", 10), bg="#f0f0f0", fg="green")
status_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 5))

log = scrolledtext.ScrolledText(frame, width=50, height=20, font=("Consolas", 10), bg="#fff")
log.grid(row=2, column=0, columnspan=3, pady=5)

entry = tk.Entry(frame, width=40, font=("Helvetica", 10))
entry.grid(row=3, column=0, pady=10)

btn_send = tk.Button(frame, text="Kirim", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), command=lambda: send_message())
btn_send.grid(row=3, column=1, padx=5)

btn_clear = tk.Button(frame, text="Clear Log", bg="#f44336", fg="white", font=("Helvetica", 10), command=lambda: log.delete(1.0, tk.END))
btn_clear.grid(row=3, column=2)

def send_message():
    msg = entry.get()
    if msg:
        client_socket.sendto(msg.encode(), server_addr)
        log.insert(tk.END, f"Anda: {msg}\n")
        entry.delete(0, tk.END)

def receive():
    while True:
        try:
            data, _ = client_socket.recvfrom(1024)
            log.insert(tk.END, f"Server: {data.decode()}\n")
        except:
            break

threading.Thread(target=receive, daemon=True).start()
window.mainloop()
