
import tkinter as tk
from tkinter import ttk
import string


# Password analysis function
def analyze_password(password):

    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
        color = "#ff4d4d"

    elif score == 3:
        strength = "MEDIUM"
        color = "#ffc107"

    elif score == 4:
        strength = "STRONG"
        color = "#28a745"

    else:
        strength = "VERY STRONG"
        color = "#00c853"

    return score, strength, color, feedback


# Analyze button function
def check_password():

    password = password_entry.get()

    if not password:
        result_label.config(
            text="Please enter a password!",
            fg="#ff4d4d"
        )
        return

    score, strength, color, feedback = analyze_password(password)

    result_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    score_label.config(
        text=f"Security Score: {score}/5"
    )

    # Update progress bar
    progress["value"] = score

    # Update progress bar color
    progress.configure(
        style="Green.Horizontal.TProgressbar"
        if score >= 4 else
        "Yellow.Horizontal.TProgressbar"
        if score == 3 else
        "Red.Horizontal.TProgressbar"
    )

    # Display suggestions
    suggestion_box.config(state="normal")
    suggestion_box.delete("1.0", tk.END)

    if feedback:
        suggestion_box.insert(
            tk.END,
            "\n".join("- " + item for item in feedback)
        )
    else:
        suggestion_box.insert(
            tk.END,
            "Your password meets all basic checks!"
        )

    suggestion_box.config(state="disabled")


# Show/hide password function
def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# Reset function
def reset_fields():

    password_entry.delete(0, tk.END)

    result_label.config(
        text="Enter a password to begin",
        fg="#aaaaaa"
    )

    score_label.config(text="Security Score: 0/5")

    progress["value"] = 0

    suggestion_box.config(state="normal")
    suggestion_box.delete("1.0", tk.END)
    suggestion_box.config(state="disabled")


# Main window
root = tk.Tk()

root.title("Password Strength Analyzer")
root.geometry("520x600")
root.resizable(False, False)
root.configure(bg="#101820")


# Heading
title_label = tk.Label(
    root,
    text="PASSWORD STRENGTH ANALYZER",
    font=("Arial", 18, "bold"),
    bg="#101820",
    fg="#00e676"
)
title_label.pack(pady=25)


# Subtitle
subtitle = tk.Label(
    root,
    text="Cybersecurity Password Checker",
    font=("Arial", 11),
    bg="#101820",
    fg="#aaaaaa"
)
subtitle.pack(pady=5)


# Password label
password_label = tk.Label(
    root,
    text="Enter Your Password",
    font=("Arial", 12, "bold"),
    bg="#101820",
    fg="white"
)
password_label.pack(pady=(25, 8))


# Password input
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=28,
    show="*",
    justify="center",
    bg="#263238",
    fg="white",
    insertbackground="white",
    relief="flat"
)
password_entry.pack(ipady=10)


# Show button
show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password,
    bg="#37474f",
    fg="white",
    relief="flat",
    cursor="hand2"
)
show_button.pack(pady=8)


# Analyze button
analyze_button = tk.Button(
    root,
    text="ANALYZE PASSWORD",
    command=check_password,
    font=("Arial", 12, "bold"),
    bg="#00c853",
    fg="#101820",
    relief="flat",
    cursor="hand2"
)
analyze_button.pack(pady=20, ipadx=20, ipady=8)


# Result label
result_label = tk.Label(
    root,
    text="Enter a password to begin",
    font=("Arial", 15, "bold"),
    bg="#101820",
    fg="#aaaaaa"
)
result_label.pack(pady=10)


# Score label
score_label = tk.Label(
    root,
    text="Security Score: 0/5",
    font=("Arial", 12),
    bg="#101820",
    fg="white"
)
score_label.pack(pady=5)


# Progress bar styles
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Green.Horizontal.TProgressbar",
    troughcolor="#263238",
    background="#00c853"
)

style.configure(
    "Yellow.Horizontal.TProgressbar",
    troughcolor="#263238",
    background="#ffc107"
)

style.configure(
    "Red.Horizontal.TProgressbar",
    troughcolor="#263238",
    background="#ff4d4d"
)


# Progress bar
progress = ttk.Progressbar(
    root,
    style="Red.Horizontal.TProgressbar",
    length=350,
    maximum=5,
    mode="determinate"
)
progress.pack(pady=10)


# Suggestions heading
suggestion_title = tk.Label(
    root,
    text="Security Suggestions",
    font=("Arial", 12, "bold"),
    bg="#101820",
    fg="#00e676"
)
suggestion_title.pack(pady=(20, 5))


# Suggestions box
suggestion_box = tk.Text(
    root,
    height=5,
    width=45,
    font=("Arial", 10),
    bg="#263238",
    fg="white",
    relief="flat",
    wrap="word"
)
suggestion_box.pack(pady=5)

suggestion_box.config(state="disabled")


# Reset button
reset_button = tk.Button(
    root,
    text="RESET",
    command=reset_fields,
    font=("Arial", 10, "bold"),
    bg="#37474f",
    fg="white",
    relief="flat",
    cursor="hand2"
)
reset_button.pack(pady=15, ipadx=25, ipady=5)


# Run application
root.mainloop()