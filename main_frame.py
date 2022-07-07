import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import webbrowser

from GSC_Node_Editor.node_types import NodeValue, NodeOperation, NodeResult
from GSC_Node_Editor.node_wire import NodeWire

class MainWindow_MainFrame(tk.Frame):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        # 'self' = main_frame

        left_frame = MainFrame_LeftFrame(self, borderwidth=1, bg='#D3D3D3', relief=tk.FLAT)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=1, pady=1, ipadx=None, ipady=None, anchor=None)

        middle_frame = MainFrame_MiddleFrame(self, borderwidth=1, bg='#D3D3D3', relief=tk.FLAT, width=None, height=None)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=1, pady=1, ipadx=None, ipady=None, anchor=None)

        right_top_frame = MainFrame_RightTopFrame(self, borderwidth=1, bg='#D3D3D3', relief=tk.FLAT, widht=None, height=None)
        right_top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=1, pady=1, ipadx=None, ipady=None, anchor=None)

        right_bottom_frame = MainFrame_RightBottomFrame(self, borderwidth=1, bg='#D3D3D3', relief=tk.FLAT, widht=None, height=None)
        right_bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=1, pady=1, ipadx=None, ipady=None, anchor=None)

class MainFrame_LeftFrame(tk.Frame):
    def __init__(self, main_frame, *args, **kwargs):
        super().__init__(main_frame, *args, **kwargs)
        # 'self' = left_frame

        button = tk.Button(self, text="Button1", command=set)
        button.pack(side=None, fill=None, expand=False, padx=None, pady=None, ipadx=None, ipady=None)

class MainFrame_MiddleFrame(tk.Frame):
    def __init__(self, main_frame, *args, **kwargs):
        super().__init__(main_frame, *args, **kwargs)
        # 'self' = middle_frame

        canvas = MyCanvas(self, bg='white', width=950, height=768)
        canvas.pack(side=None, fill=tk.Y, expand=False, padx=None, pady=None, ipadx=None, ipady=None, anchor=None)

        node = NodeValue(canvas, value=50)
        node = NodeValue(canvas, value=100)

        node = NodeOperation(canvas, text='ADD')
        # node = NodeOperation(canvas, text='SUB')

        node = NodeResult(canvas)

class MyCanvas(tk.Canvas):
    def __init__(self, master, bg='white', width=950, height=768):
        super().__init__(master, bg=bg, width=width, height=height)
        # 'self' = tk.Canvas

        self.inputcell = None
        self.outputcell = None
        self.clickcount = 0
        self.IDc = None

        self.right_click_on_canvas()

    def conectcells(self):
        if self.IDc == 'input1': self.inputcell.cellinput1 = self.outputcell
        if self.IDc == 'input2': self.inputcell.cellinput2 = self.outputcell

        self.line = NodeWire(self, self.outputcell, self.inputcell)
        self.inputcell.update()

    def right_click_on_canvas(self):
        RightClickMenu = tk.Menu(self, tearoff=False, background='#A0A0A0', fg='black')
        RightClickMenu.add_command(label="Node Value", command=lambda: NodeValue(self, value=50))
        RightClickMenu.add_command(label="Node Operation - ADD", command=lambda: NodeOperation(self, text='ADD'))
        RightClickMenu.add_command(label="Node Operation - SUB", command=lambda: NodeOperation(self, text='SUB'))
        RightClickMenu.add_command(label="Node Result", command=lambda: NodeResult(self))

        def do_popup(event):
            try: RightClickMenu.tk_popup(event.x_root, event.y_root)
            finally: RightClickMenu.grab_release()

        self.bind("<Button-3>", do_popup)

class MainFrame_RightTopFrame(tk.Frame):
    def __init__(self, main_frame, *args, **kwargs):
        super().__init__(main_frame, *args, **kwargs)
        # 'self' = right_top_frame

        code_output_area = tk.Text(self, relief=tk.FLAT, bd=None, width=None, height=20, background='#D3D3D3', insertbackground='#1E1E1E')
        code_output_area.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=tk.N)
        code_output_area.config(font=("Courier New", 10), fg="black")
        code_output_area.insert("1.0", 'Console log..')
        code_output_area.configure(state='disabled')

class MainFrame_RightBottomFrame(tk.Frame):
    def __init__(self, main_frame, *args, **kwargs):
        super().__init__(main_frame, *args, **kwargs)
        # 'self' = right_bottom_frame

        control_panel = ttk.Notebook(self, bd=None, width=None, height=None)
        control_panel.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=tk.S)

        self.tab1 = tk.Frame(control_panel, borderwidth=1, relief=tk.FLAT, bg='#D3D3D3')
        # tab1.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=None)
        self.tab2 = tk.Frame(control_panel, borderwidth=1, relief=tk.FLAT, bg='#D3D3D3')
        # tab2.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=None)
        self.tab3 = tk.Frame(control_panel, borderwidth=1, relief=tk.FLAT, bg='#D3D3D3')
        # tab3.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=None)
        self.tab4 = tk.Frame(control_panel, borderwidth=1, relief=tk.FLAT, bg='#D3D3D3')
        # tab4.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=None, ipadx=None, ipady=None, anchor=None)

        control_panel.add(self.tab1, text='Quick Notes')
        control_panel.add(self.tab2, text='tab2')
        control_panel.add(self.tab3, text='tab3')
        control_panel.add(self.tab4, text='Useful Links')

        self.populate_tab1()
        self.populate_tab2()
        self.populate_tab3()
        self.populate_tab4()

    def populate_tab1(self):
        # TAB 1 - Quick Notes
        label = ctk.CTkLabel(self.tab1, text='Quick Notes', bg_color=None, fg_color='black', relief=tk.FLAT)
        label.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)
        label.config(font=("Courier New", 10), fg="white")

        textbox = tk.Text(self.tab1, relief=tk.FLAT, bd=None, width=None, height=None, bg='#1E1E1E', insertbackground='white', undo=True, wrap=tk.NONE)
        textbox.pack(side=None, fill=tk.BOTH, expand=True, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)
        textbox.config(font=("Courier New", 10), fg='white')
        textbox.insert("1.0", 'Note: Nothing here gets saved.')
        # textbox.configure(state='disabled')

    def populate_tab2(self):
        pass

    def populate_tab3(self):
        pass

    def populate_tab4(self):
        # TAB 4 - Useful Links
        Dev_note_label = ctk.CTkLabel(self.tab4,text='Useful Links', bg_color=None, fg_color='black', relief=tk.FLAT)
        Dev_note_label.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)
        Dev_note_label.config(font=("Courier New", 10), fg="white")

        CME_LABEL = ctk.CTkLabel(self.tab4, text='CME (CoD Modding Elite)', bg_color=None, fg_color='#1C1CCE', relief=tk.FLAT)
        CME_LABEL.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)
        CME_LABEL.config(font=("Courier New", 10), fg="white")

        CME_DISCORD = ctk.CTkButton(master=self.tab4, height=25, text="Discord", border_width=3, fg_color='#1C94CF', text_color='black', command=lambda:hyperlink("https://discord.gg/w6v6HuFRYD"))
        CME_DISCORD.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)

        CME_WEBSITE = ctk.CTkButton(master=self.tab4, height=25, text="Website", border_width=3, fg_color='#1C94CF', text_color='black', command=lambda:hyperlink("https://cme-mods.com/"))
        CME_WEBSITE.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)

        CME_YOUTUBE = ctk.CTkButton(master=self.tab4, height=25, text="YouTube", border_width=3, fg_color='#1C94CF', text_color='black', command=lambda:hyperlink("https://www.youtube.com/channel/UC1q44w1Zs1c5xABRjzjj1xA"))
        CME_YOUTUBE.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)

        Tkinter_And_Tcl_Tk_LABEL = ctk.CTkLabel(self.tab4, text='Tkinter And Tcl/Tk', bg_color=None, fg_color='#1C1CCE', relief=tk.FLAT)
        Tkinter_And_Tcl_Tk_LABEL.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)
        Tkinter_And_Tcl_Tk_LABEL.config(font=("Courier New", 10), fg="white")

        Tkinter_And_Tcl_Tk_DISCORD = ctk.CTkButton(master=self.tab4, height=25, text="Discord", border_width=3, fg_color='#1C94CF', text_color='black', command=lambda:hyperlink("https://discord.gg/NBmjCZfMk7"))
        Tkinter_And_Tcl_Tk_DISCORD.pack(side=tk.TOP, fill=tk.X, expand=False, padx=None, pady=5, ipadx=None, ipady=None, anchor=None)

        def hyperlink(url):
            try: webbrowser.open_new(url)
            except:
                messagebox.showinfo("Failed", "Could be that you have no internet connection?")
                pass
