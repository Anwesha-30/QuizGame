import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "Who developed the Python language?",
        "options": ["Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What will be the output of: print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "define", "lambda"],
        "answer": "def"
    },
    {
        "question": "Which of the following is used to take input from the user in Python?",
        "options": ["get()", "input()", "scan()", "read()"],
        "answer": "input()"
    },
    {
        "question": "What does the len() function do in Python?",
        "options": [
            "Returns the type of a variable",
            "Returns the length of an object",
            "Returns the memory size",
            "Returns the sum of numbers"
        ],
        "answer": "Returns the length of an object"
    },
    {
        "question": "Which one is a mutable data type in Python?",
        "options": ["Tuple", "String", "List", "Integer"],
        "answer": "List"
    }
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.root.geometry("700x520")
        self.root.config(bg="#e3f2fd")

        self.score = 0
        self.question_index = 0
        self.selected_option = tk.StringVar()

        # Header Frame
        header = tk.Frame(root, bg="#2196f3")
        header.pack(fill="x")

        tk.Label(
            header,
            text=" Python Quiz Challenge",
            font=("Segoe UI", 22, "bold"),
            bg="#2196f3",
            fg="white",
            pady=10
        ).pack(side="left", padx=20)

        # Live Score Display
        self.score_label = tk.Label(
            header,
            text=f"Score: {self.score}/{len(questions)}",
            font=("Segoe UI", 16, "bold"),
            bg="#2196f3",
            fg="white",
            pady=10
        )
        self.score_label.pack(side="right", padx=20)

        # Question Label
        self.question_label = tk.Label(
            root,
            text="",
            font=("Segoe UI", 16, "bold"),
            wraplength=600,
            bg="#e3f2fd",
            justify="center"
        )
        self.question_label.pack(pady=30)

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                root,
                text="",
                variable=self.selected_option,
                value="",
                font=("Segoe UI", 13),
                bg="#bbdefb",
                fg="#0d47a1",
                activebackground="#64b5f6",
                selectcolor="#bbdefb",
                anchor="w",
                indicatoron=0,
                padx=15,
                pady=8,
                width=40,
                relief="flat",
                borderwidth=0
            )
            btn.pack(pady=6)

            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#64b5f6"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#bbdefb"))

            self.option_buttons.append(btn)

        # Next Button
        self.next_button = tk.Button(
            root,
            text="Next ➡️",
            command=self.check_answer,
            font=("Segoe UI", 16, "bold"),
            bg="#1976d2",
            fg="white",
            activebackground="#0d47a1",
            relief="flat",
            padx=30,
            pady=12,
            width=15
        )
        self.next_button.pack(pady=40)

        self.load_question()


    def load_question(self):
        q = questions[self.question_index]
        self.question_label.config(text=f"Q{self.question_index + 1}. {q['question']}")
        self.selected_option.set("")
        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].config(
                text=opt,
                value=opt,
                bg="#bbdefb",
                fg="#0d47a1",
                state="normal",
                font=("Segoe UI", 13)
            )


    def check_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option before proceeding!")
            return

        correct_answer = questions[self.question_index]["answer"]

        for btn in self.option_buttons:
            btn.config(state="disabled")
            if btn["text"] == correct_answer:
                btn.config(bg="#4caf50", fg="white", font=("Segoe UI", 13, "bold"))  # Green
            elif btn["text"] == selected:
                btn.config(bg="#f44336", fg="white", font=("Segoe UI", 13, "bold"))  # Red

        if selected == correct_answer:
            self.score += 1
            self.update_score()

       
        if self.question_index == len(questions) - 1:
            self.root.after(1200, self.show_result)
        else:
            self.root.after(1200, self.next_question)

    def next_question(self):
        self.question_index += 1
        self.load_question()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}/{len(questions)}")

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root,
            text="🎯 Quiz Completed!",
            font=("Segoe UI", 24, "bold"),
            bg="#e3f2fd",
            fg="#0d47a1"
        ).pack(pady=40)

        total_q = len(questions)
        percentage = round((self.score / total_q) * 100, 2)
        marks = f"You scored {self.score} out of {total_q}"
        percent = f"Percentage: {percentage}%"

        tk.Label(
            self.root,
            text=marks,
            font=("Segoe UI", 20),
            bg="#e3f2fd",
            fg="#1a237e"
        ).pack(pady=5)

        tk.Label(
            self.root,
            text=percent,
            font=("Segoe UI", 18),
            bg="#e3f2fd",
            fg="#1a237e"
        ).pack(pady=10)

        if percentage >= 80:
            remark = "🌟 Excellent work! You're a Python Pro!"
        elif percentage >= 50:
            remark = "👍 Good job! Keep improving!"
        else:
            remark = "💪 Keep practicing, you’ll get there!"

        tk.Label(
            self.root,
            text=remark,
            font=("Segoe UI", 16, "italic"),
            bg="#e3f2fd",
            fg="#004d40"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Play Again 🔁",
            command=self.restart_quiz,
            font=("Segoe UI", 14, "bold"),
            bg="#1976d2",
            fg="white",
            relief="flat",
            padx=25,
            pady=10
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Exit",
            command=self.root.destroy,
            font=("Segoe UI", 13),
            bg="#ef5350",
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        ).pack()

    
    def restart_quiz(self):
        self.score = 0
        self.question_index = 0
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)



if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
