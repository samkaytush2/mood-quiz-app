import tkinter as tk
import random

# Questions
questions = [
    "Did you have a good day today?",
    "Are you feeling excited about anything?",
    "Do you feel happy right now?",
    "Did something make you smile today?",
    "Are you feeling motivated today?"
]

# Scores
happy_score = 0
sad_score = 0
current_question = 0

# Setup GUI
root = tk.Tk()
root.title("Mood Quiz App")
root.geometry("300x500")
root.configure(bg="green")

# Header
header = tk.Frame(root, bg="orange", height=70, bd=10)
header.pack(fill="x")
tk.Label(header, text="Mood Quiz", font=("Tomara", 30, "bold"), bg="orange", fg="White").pack(pady=30)

# Question card
card = tk.Frame(root, bg="orange", bd=12, relief="raised", padx=30, pady=30)
card.pack(pady=0, padx=0, fill="both", expand=False)

question_label = tk.Label(card, text=questions[current_question], font=("Times new roman", 16, "bold"), wraplength=650, bg="orange" , fg="Green")
question_label.pack(pady=30)

# Canvas for confetti
canvas = tk.Canvas(width=1000, height=300, bg="Green", highlightthickness=0)
canvas.pack()

# Function to process answer
def process_answer(answer):
    global happy_score, sad_score
    if answer == "Yes":
        happy_score += 2
    elif answer == "No":
        sad_score += 2
    elif answer == "I don't know":
        happy_score += 1
        sad_score += 1
    next_question()

# Move to next question
def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        question_label.config(text=questions[current_question])
    else:
        show_result()

# Confetti celebration
def celebrate():
    confetti = []
    colors = ["#ff4757", "#1e90ff", "#2ed573", "#ffa502", "#ff6b81", "#3742fa"]
    for _ in range(100):
        x = random.randint(-50, 700)
        y = random.randint(-250, 0)
        size = random.randint(10, 20)
        color = random.choice(colors)
        confetti.append(canvas.create_oval(x, y, x+size, y+size, fill=color, outline=""))

    def fall():
        for c in confetti:
            canvas.move(c, 0, random.randint(3, 7))
            pos = canvas.coords(c)
            if pos[1] > 250:
                canvas.coords(c, pos[0], -10, pos[2], -10 + (pos[3]-pos[1]))
        root.after(50, fall)
    fall()

# Show final result
def show_result():
    total = happy_score + sad_score
    mood_score = round((happy_score / total) * 10) if total else 5

    if mood_score >= 7:
        mood = "HAPPY"
        suggestion = "Listen to music and dance"
        question_label.config(text=f"Your mood score: {mood_score}/10\nYou seem {mood}!\n{suggestion}")
        celebrate()
    elif mood_score <= 4:
        mood = "SAD"
        suggestion = "Watch a funny video, take a walk, or treat yourself"
        question_label.config(text=f"Your mood score: {mood_score}/10\nYou seem {mood}.\n{suggestion}")
    else:
        mood = "NEUTRAL"
        suggestion = "Try a hobby, relax, or take a short break"
        question_label.config(text=f"Your mood score: {mood_score}/10\nYou seem {mood}.\n{suggestion}")

    yes_button.config(state="disabled", bg="#b0b0b0")
    no_button.config(state="disabled", bg="#b0b0b0")
    dontknow_button.config(state="disabled", bg="#b0b0b0")

# Buttons 
button_frame = tk.Frame(root, bg="green")
button_frame.pack(pady=10)

yes_button = tk.Button(button_frame, text="Yes", width=25, height=2, font=("Tomara", 14, "bold"), bg="#4cd137", fg="White", bd=10, command=lambda: process_answer("Yes"))
yes_button.pack(pady=10)

no_button = tk.Button(button_frame, text="No", width=25, height=2, font=("Tomara", 14, "bold"), bg="#ff4757", fg="White", bd=10, command=lambda: process_answer("No"))
no_button.pack(pady=10)

dontknow_button = tk.Button(button_frame, text="I don't know", width=25, height=2, font=("Tomara", 14, "bold"), bg="#ffa502", fg="white", bd=10, command=lambda: process_answer("I don't know"))
dontknow_button.pack(pady=10)

root.mainloop()