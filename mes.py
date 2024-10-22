import tkinter as tk
from tkinter import ttk

import read


class MessengerApp:
    def __init__(self, master,name):
        self.master = master
        self.name=name
        self.master.title("Мессенджер")
        self.master.geometry("700x500")
        self.chats = {f"Чат {i}": [] for i in range(1, 7)}

        # Основной фрейм для размещения кнопок
        button_frame = ttk.Frame(self.master)
        button_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Создаем кнопки для чатов
        for i in range(1, 7):
            button = ttk.Button(button_frame, text=f"Чат {i}", command=lambda i=i: self.open_chat(i))
            button.pack(pady=5)

        # Фрейм для отображения чата
        self.chat_frame = ttk.Frame(self.master)
        self.chat_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Текстовое поле для сообщений
        self.text_area = tk.Text(self.chat_frame, state='disabled', wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Поле для ввода сообщения
        self.message_entry = ttk.Entry(self.chat_frame)
        self.message_entry.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)

        # Кнопка отправки сообщения
        send_button = ttk.Button(self.chat_frame, text="Отправить", command=self.send_message)
        send_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.current_chat = None

    def open_chat(self, chat_number):
        self.current_chat = f"Чат {chat_number}"

        text=read.read_file_to_list(self.current_chat+".txt")
        self.text_area.config(state='normal')
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, f"Открыт {self.current_chat}\n")
        if(len(text)>0):
            if text[0].startswith("\n"):
                text[0] = text[0][1:]
        for i in range(len(text)):
            self.text_area.insert(tk.END, text[i]+"\n")
        self.text_area.config(state='disabled')

    def send_message(self):
        if self.current_chat:
            message = self.message_entry.get()
            read.write_file(self.current_chat+".txt", self.name+": "+message)
            if message:
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, f"{self.name}: {message}\n")
                self.text_area.config(state='disabled')
                self.message_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MessengerApp(root,"egor")
    root.mainloop()