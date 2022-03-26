import tkinter as tk
from tkinter import ttk, messagebox
import utils_for_data as utils


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginScreen, SignupScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = tk.Entry(self, show="*", textvariable=self.password_var)
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        self.login_button = ttk.Button(self, text="Login", command=self.submit_to_login)
        self.login_button.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5, ipadx=50)

        # Don't have account
        self.have_account_label = tk.Label(self, text="Don't have account?")
        self.have_account_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        self.signup_button = tk.Button(self, text="Signup", command=lambda: controller.show_frame(SignupScreen))
        self.signup_button.grid(column=1, row=3, sticky=tk.W, padx=10, pady=10)

    def submit_to_login(self):
        name = self.username_var.get()
        password = self.password_var.get()
        utils.login(username=name, password=password)


class SignupScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        self.username_entry = tk.Entry(self, textvariable=self.username_var)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.password_entry = tk.Entry(self, show="*", textvariable=self.password_var)
        self.password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # signUp button
        self.signup_button = ttk.Button(self, text="SignUp", command=self.sign_up)
        self.signup_button.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5, ipadx=50)

        self.login_button = ttk.Button(self, text="Login", command=lambda: controller.show_frame(LoginScreen))
        self.login_button.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5, ipadx=50)

    def sign_up(self):
        utils.sign_up(self.username_var.get(), self.password_var.get())
        self.username_var.set("")
        self.password_var.set("")
