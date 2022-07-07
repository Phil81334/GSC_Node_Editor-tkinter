import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from main_frame import MainWindow_MainFrame

class MainWindow(ctk.CTk):
    def __init__(self, window_size, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("GSC Node Editor")
        self.window_size = window_size
        self.geometry(f"{self.window_size[0]}x{self.window_size[1]}")
        self.minsize(self.window_size[0], self.window_size[1])
        self.resizable(0, 0) # This removes the maximise button
        # self.call('tk', 'scaling', 2.0) # A scale of 2.0 will 2x the size of all widgets and text, whereas a scale of 0.5 will do the opposite
        self.iconbitmap('skull_icon_c.ico')
        # self.state('zoomed')
        self.configure(background='#8585ad')
        # self.protocol("WM_DELETE_WINDOW", self.on_closing) # enable once beta is ready

    def on_closing(self):
        if messagebox.askokcancel("WARNING", "Are you sure you want to quit?"): self.destroy()
        else: pass

class MainWindow_Menu(tk.Menu):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        # 'self' = root_menu

        file_menu = tk.Menu(self, tearoff=False, background='#A0A0A0', fg='black')
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save As...")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=app.on_closing)

        edit_menu = tk.Menu(self, tearoff=False, background='#A0A0A0', fg='black')
        self.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")

        about_menu = tk.Menu(self, tearoff=False, background='#A0A0A0', fg='black')
        self.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="Discord")
        about_menu.add_command(label="Website")
        about_menu.add_command(label="YouTube")

""" Actual application window """
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainWindow(window_size=[1366,768])
    app_menu = MainWindow_Menu(app)
    app.config(menu=app_menu)

    main_frame = MainWindow_MainFrame(app, borderwidth=1, bg='#8585ad', relief=tk.FLAT)
    main_frame.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None)

    app.mainloop()

    # relief styles:
    # FLAT
    # RAISED
    # SUNKEN
    # GROOVE
    # RIDGE

    # .pack() **options
    # side = LEFT, RIGHT, TOP, BOTTOM
    # fill = X, Y, BOTH
    # expand = True, False
    # padx, pady = outter padding - int/float
    # ipadx, ipady = inner padding - int/float
