import tkinter as tk
from tkinter import ttk
import mes
import read


class Registration:
    def __init__(self, master):
        self.master = master
        self.master.title("форум")
        self.master.geometry("300x175+100+100")
        self.master.resizable(False, False)

        self.button_1 = ttk.Button(self.master, text="Вход", command=self.enter)
        self.button_2 = ttk.Button(self.master, text="Регистрация", command=self.register)

        # Используем place для точного позиционирования
        self.button_1.place(x=100, y=50)  # Позиция по X и Y
        self.button_2.place(x=100, y=100)  # Позиция по X и Y
        self.users_passwords = read.read_file_to_dict()

    def register(self):
        self.master.destroy()  # Закрываем текущее окно, когда открываем новое
        # Создаем новое окно
        self.new_window = tk.Tk()
        self.name=""
        self.new_window.title("регистрация")# Используем новый экземпляр Tk
        self.new_window.geometry("350x300+207+133")
        self.new_window.resizable(False, False)
        # Добавляем виджеты в зависимости от типа окна
        label_name = tk.Label(self.new_window, text="Имя:")
        label_name.pack(pady=(10, 0))
        self.message_name = tk.Entry(self.new_window, width=30)
        self.message_name.pack(pady=(0, 10))

        label_password = tk.Label(self.new_window, text="Пароль:")
        label_password.pack(pady=(10, 0))
        self.message_password = tk.Entry(self.new_window, width=30, show='*')
        self.message_password.pack(pady=(0, 10))

        label_password_too = tk.Label(self.new_window, text="Повторите пароль:")
        label_password_too.pack(pady=(10, 0))
        self.message_password_too = tk.Entry(self.new_window, width=30, show='*')
        self.message_password_too.pack(pady=(0, 10))


        self.new_window.button_1 = ttk.Button(self.new_window, text="Вход", command=self.checking_registration)
        self.new_window.button_1.place(x=210, y=200)

        self.new_window.button_2 = ttk.Button(self.new_window, text="Назад", command=self.back)
        self.new_window.button_2.place(x=50, y=200)

        self.new_window.mainloop()
    def enter(self):
        self.master.destroy()  # Закрываем текущее окно, когда открываем новое
        # Создаем новое окно
        self.new_window = tk.Tk()  # Используем новый экземпляр Tk
        self.new_window.geometry("350x300+207+133")
        self.new_window.resizable(False, False)
        label_name = tk.Label(self.new_window, text="Имя:")
        label_name.pack(pady=(10, 0))
        self.message_name_enter = tk.Entry(self.new_window, width=30)
        self.message_name_enter.pack(pady=(0, 10))

        label_password = tk.Label(self.new_window, text="Пароль:")
        label_password.pack(pady=(10, 0))
        self.message_password_enter = tk.Entry(self.new_window, width=30, show='*')
        self.message_password_enter.pack(pady=(0, 10))
        self.new_window.button_1 = ttk.Button(self.new_window, text="Вход", command=self.checking_enter)
        self.new_window.button_1.place(x=210, y=200)

        self.new_window.button_2 = ttk.Button(self.new_window, text="Назад", command=self.back)
        self.new_window.button_2.place(x=50, y=200)
        self.new_window.mainloop()
    def checking_registration(self):
        name = self.message_name.get()
        pas1 = self.message_password.get()
        pas2 = self.message_password_too.get()
        if(name not in self.users_passwords.keys()):
            if(pas1==pas2):
                self.users_passwords[name] = pas1
                read.write_users(self.users_passwords)
                self.new_window.destroy()
                self.new_window2 = tk.Tk()
                self.new_window2.geometry("350x300+207+133")
                self.new_window2.resizable(False, False)
                label = ttk.Label(self.new_window2, text="Вы успешно зарегестрировались.")
                label.pack(pady=20)
                self.new_window2.button_2 = ttk.Button(self.new_window2, text="ВОЙТИ", command=self.get)
                self.new_window2.button_2.place(x=140, y=200)
            else:
                self.new_window2 = tk.Tk()
                self.new_window2.geometry("350x300+207+133")
                self.new_window2.resizable(False, False)
                label = ttk.Label(self.new_window2, text="пароли не совпадают")
                label.pack(pady=20)
                self.new_window2.button_2 = ttk.Button(self.new_window2, text="ОК", command=self.not_pass)
                self.new_window2.button_2.place(x=140, y=200)
        else:
            self.new_window2 = tk.Tk()
            self.new_window2.geometry("350x300+207+133")
            self.new_window2.resizable(False, False)
            label = ttk.Label(self.new_window2, text="пользователь с таким именем уже есть")
            label.pack(pady=20)
            self.new_window2.button_2 = ttk.Button(self.new_window2, text="ОК", command=self.not_pass)
            self.new_window2.button_2.place(x=140, y=200)

    def checking_enter(self):
        self.name = self.message_name_enter.get()
        pas = self.message_password_enter.get()
        keys=self.users_passwords.keys()
        if(self.name in keys):
            if(self.users_passwords[self.name]==pas):
                self.new_window.destroy()
                self.new_window2 = tk.Tk()
                self.new_window2.geometry("350x300+207+133")
                self.new_window2.resizable(False, False)
                label = ttk.Label(self.new_window2, text="Вы успешно вошли.")
                label.pack(pady=20)
                self.new_window2.button_2 = ttk.Button(self.new_window2, text="ВОЙТИ", command=self.get)
                self.new_window2.button_2.place(x=140, y=200)
            else:
                self.new_window2 = tk.Tk()
                self.new_window2.geometry("350x300+207+133")
                self.new_window2.resizable(False, False)
                label = ttk.Label(self.new_window2, text="неверный пароль.")
                label.pack(pady=20)
                self.new_window2.button_2 = ttk.Button(self.new_window2, text="ОК", command=self.not_pass)
                self.new_window2.button_2.place(x=140, y=200)
        else:
            self.new_window2 = tk.Tk()
            self.new_window2.geometry("350x300+207+133")
            self.new_window2.resizable(False, False)
            label = ttk.Label(self.new_window2, text="пользователя с таким именем нет")
            label.pack(pady=20)
            self.new_window2.button_2 = ttk.Button(self.new_window2, text="ОК", command=self.not_pass)
            self.new_window2.button_2.place(x=140, y=200)

    def back(self):
        self.new_window.destroy()
        root = tk.Tk()
        app = Registration(root)
        root.mainloop()

    def get(self):
        self.new_window2.destroy()
        root = tk.Tk()
        mes.MessengerApp(root,self.name)
    def not_pass(self):
        self.new_window2.destroy()



# Запуск приложения