import tkinter as tk
import os

DEBUG = True

class App:
    def __init__(self):
        # Model Section
        self.folders = []  # List to store folder names
        
        # Initialize the app
        self.init_folders()
        
        # Controller Section
        

        # View Section
        pass

    def init_folders(self):
        """Search for folders.txt and store folder names in self.folders list"""
        try:
            # Search for folders.txt in current directory
            if os.path.exists("folders.txt"):
                with open("folders.txt", "r", encoding="utf-8") as file:
                    self.folders = [line.strip() for line in file.readlines() if line.strip()]
                if DEBUG:
                    print(f"Found {len(self.folders)} folders: {self.folders}")
                return True

            else:
                print("folders.txt not found in current directory")
                return False

        except Exception as e:
            print(f"Error reading folders.txt: {e}")
            self.folders = []
            return False

    def run(self):
        pass
        self.root.mainloop()

def main():
    app = App()
    app.run()
    





"""
# main window
root = tk.Tk()
root.title("PARA Notes")
root.geometry("400x300")
root.resizable(False, False)

# font
root.option_add('*Font', 'Arial 12')

# center the window
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# main frame enclosing the top and bottom frames
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill='both', padx=20, pady=20)

# large text field in top frame
top_text = tk.Text(main_frame, bg='white', relief='sunken', bd=2, height=8)
top_text.pack(fill='both', expand=True, pady=(0, 20))

# 4 smaller boxes in bottom frame
bottom_frame = tk.Frame(main_frame)
bottom_frame.pack(fill='x')
box_width = (width - 60) // 4 
for i in range(4):
    small_box = tk.Frame(bottom_frame, bg='lightblue', relief='raised', bd=2, width=box_width, height=80)
    small_box.pack(side='left', padx=(0, 10) if i < 3 else (0, 0))
    small_box.pack_propagate(False) 

# main loop
root.mainloop() 
"""


if __name__ == "__main__":
    main()