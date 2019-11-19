import tkinter as tk
from .models import Theme
from .settings_gui import SettingsWindow

class Menubar(tk.Menu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.themes_menu = tk.Menu(self)
        self.options_menu = tk.Menu(self)
        self.selected_theme = tk.IntVar()
        self.selected_theme.set(0)
        self.settings_toplevel = None
        
        self.themes = Theme.get_all_themes()
        
        self.init_theme_menu()
        self.options_menu.add_command(label="Settings", command=self.open_settings_menu)
        self.options_menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.add_cascade(label="Options", menu=self.options_menu)
        
    def init_theme_menu(self):
        for theme in self.themes:
            self.themes_menu.add_radiobutton(label=theme.name, 
                                             value=theme.id, 
                                             variable=self.selected_theme)
    
    def open_settings_menu(self):
        if self.settings_toplevel is None:
            self.settings_toplevel = tk.Toplevel(self.master)
            self.settings_toplevel.title("Settings")
            gui = SettingsWindow(self.settings_toplevel, controller=self)
            gui.grid(sticky='nswe')
            self.settings_toplevel.mainloop()
