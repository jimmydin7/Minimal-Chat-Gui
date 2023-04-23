import tkinter as tk
from PIL import ImageTk, Image


class ChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x600")
        self.root.config(bg="#36393F")

        self.display_label = tk.Label(text="Select a user or group to chat!", bg="#36393F", fg="white", font=("Poppins", 15))
        self.display_label.pack()

        def open_boys(event=None):
            print("Boys Group Opened")
            self.display_label.configure(text=f"Boys Group - 7 Online")

        def open_school(event=None):
            print("School Group Opened")
            self.display_label.configure(text=f"School Group - 3 Online")

        def open_friend1(event=None):
            print("xJmd")
            self.display_label.configure(text=f"xJmd")

        def open_friend2(event=None):
            print("Thbop")
            self.display_label.configure(text=f"Thbop")

        def open_friend3(event=None):
            print("Alex")
            self.display_label.configure(text=f"Alex")

        self.left_frame = tk.Frame(self.root, bg="#36393F", width=200, height=600)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        self.label = tk.Label(self.left_frame, text="Friends & Group Chats", fg="white", bg="#36393F", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.list_frame = tk.Frame(self.left_frame, bg="#2C2F33")
        self.list_frame.pack(fill=tk.BOTH, padx=10, pady=5)

        self.boys_button = tk.Button(self.list_frame, text="The Boys", fg="white", bg="#7289DA", bd=0, font=("Helvetica", 10, "bold"), command=open_boys)
        self.boys_button.pack(fill=tk.X, pady=5)

        self.school_club_button = tk.Button(self.list_frame, text="School", fg="white", bg="#7289DA", bd=0, font=("Helvetica", 10, "bold"), command=open_school)
        self.school_club_button.pack(fill=tk.X, pady=5)

        self.friend1_button = tk.Button(self.list_frame, text="xJmd", fg="white", bg="#7289DA", bd=0, font=("Helvetica", 10, "bold"), command=open_friend1)
        self.friend1_button.pack(fill=tk.X, pady=5)

        self.friend2_button = tk.Button(self.list_frame, text="Thbop", fg="white", bg="#7289DA", bd=0, font=("Helvetica", 10, "bold"), command=open_friend2)
        self.friend2_button.pack(fill=tk.X, pady=5)

        self.friend3_button = tk.Button(self.list_frame, text="Alex", fg="white", bg="#7289DA", bd=0, font=("Helvetica", 10, "bold"), command=open_friend3)
        self.friend3_button.pack(fill=tk.X, pady=5)

        for button in [self.boys_button, self.school_club_button, self.friend1_button, self.friend2_button, self.friend3_button]:
            img = Image.open("pfp/user.png")
            img = img.resize((30, 30))
            img = ImageTk.PhotoImage(img)
            button.config(image=img, compound="left", padx=10, anchor="w")
            button.image = img

        self.right_frame = tk.Frame(self.root, bg="#2C2F33", width=700, height=600)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # Run the app
        self.root.mainloop()

if __name__ == '__main__':
    ChatGUI()