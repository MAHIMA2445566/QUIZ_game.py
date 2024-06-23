import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("800x500")
        
        # Set background image
        self.bg_image = Image.open("C:/Users/mahim/Downloads/image.webp")  # Replace with your image path
        #self.bg_image = self.bg_image.resize((800, 500), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Overlay frame
        self.overlay_frame = tk.Frame(self.root, bg="#ffffff", bd=10)
        self.overlay_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.85)
        
        # Quiz data
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
            {"question": "What is the capital of Italy?", "options": ["Rome", "Paris", "Lisbon", "Athens"], "answer": "Rome"},
            {"question": "What is the capital of Germany?", "options": ["Berlin", "Vienna", "Amsterdam", "Prague"], "answer": "Berlin"},
            {"question": "What is the capital of Spain?", "options": ["Madrid", "Barcelona", "Valencia", "Seville"], "answer": "Madrid"},
            {"question": "What is the capital of Portugal?", "options": ["Lisbon", "Porto", "Faro", "Braga"], "answer": "Lisbon"},
        ]
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(self.overlay_frame, text="", font=("Arial", 16), bg="#ffffff", wraplength=700)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.options_frame = tk.Frame(self.overlay_frame, bg="#ffffff")
        self.options_frame.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.options_frame, text="", variable=self.options_var, value="", font=("Arial", 14), bg="#ffffff", wraplength=700)
            btn.pack(anchor="w")
            self.option_buttons.append(btn)

        self.next_button = tk.Button(self.overlay_frame, text="Next", command=self.next_question, font=("Arial", 14), bg="#008CBA", fg="#ffffff", padx=20, pady=10, bd=0, highlightthickness=0)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.options_var.set("")
        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.options_var.get() == self.questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1

        if self.current_question >= len(self.questions):
            messagebox.showinfo("Quiz Complete", f"You scored {self.score}/{len(self.questions)}")
            self.root.destroy()
        else:
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
