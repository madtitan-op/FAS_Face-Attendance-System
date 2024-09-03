import tkinter as tk
from tkinter import  messagebox
from time import strftime
from PIL import Image, ImageTk, ImageDraw
from student_info import show_student_info, proceed

def main():
    root = tk.Tk()
    root.title("Face Recognizing App")
    root.geometry("500x400")
    root.configure(bg="lightblue")

    windows = {}

    # Create a frame to hold all the components (styled as a card)
    card_frame = tk.Frame(root, bg="lightgray", bd=10, relief=tk.RAISED)
    card_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Create a frame for the clock inside the card
    clock_box = tk.Frame(card_frame, bg="green", bd=5, relief=tk.RIDGE)
    clock_box.pack(pady=10)

    # Create a label to display the clock inside the frame
    clock_label = tk.Label(clock_box, text="", font=('Times New Roman', 40, 'bold'), bg="pink", fg="black")
    clock_label.pack()

    # Create a frame for the icons inside the card
    icon_frame = tk.Frame(card_frame, bg="lightgray")
    icon_frame.pack(pady=10)

    # Load and resize the icons
    student_img = Image.open("student_icon.png").resize((80, 80), Image.LANCZOS)
    faculty_img = Image.open("faculty_icon.png").resize((80, 80), Image.LANCZOS)

    # Apply rounded corners to icons
    student_img = create_rounded_rectangle(student_img, 15, (255, 255, 255, 0))
    faculty_img = create_rounded_rectangle(faculty_img, 15, (255, 255, 255, 0))

    student_icon = ImageTk.PhotoImage(student_img)
    faculty_icon = ImageTk.PhotoImage(faculty_img)

    # Create and place the "Student" icon
    student_icon_label = tk.Label(icon_frame, image=student_icon, bg="lightgray")
    student_icon_label.pack(side=tk.LEFT, padx=50)

    # Create and place the "Faculty" icon
    faculty_icon_label = tk.Label(icon_frame, image=faculty_icon, bg="lightgray")
    faculty_icon_label.pack(side=tk.RIGHT, padx=50)

    # Create a frame to hold the buttons inside the card
    button_frame = tk.Frame(card_frame, bg="lightgray")
    button_frame.pack(pady=20)

    # Create and place the "Student" button with a 3D effect
    student_button = tk.Button(button_frame, text="Student", command=lambda: show_student_info(root, windows), width=15, height=2, relief=tk.RAISED, bd=3, font=('Helvetica', 12, 'bold'), bg="#e0f7fa", fg="#00695c")
    student_button.pack(side=tk.LEFT, padx=20)  # Place the button on the left side of the frame with padding

    # Create and place the "Faculty" button with a 3D effect
    faculty_button = tk.Button(button_frame, text="Faculty", command=lambda: messagebox.showinfo("Faculty", "Faculty button clicked"), width=15, height=2, relief=tk.RAISED, bd=3, font=('Helvetica', 12, 'bold'), bg="#e0f7fa", fg="#00695c")
    faculty_button.pack(side=tk.LEFT, padx=20)  # Place the button on the left side of the frame with padding

    # Start the clock
    update_time(clock_label)

    root.mainloop()

def create_rounded_rectangle(image, radius, color):
    """Create a rounded rectangle mask."""
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    mask = Image.new('L', image.size, 255)
    mask.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    mask.paste(circle.crop((0, radius, radius, radius * 2)), (0, image.height - radius))
    mask.paste(circle.crop((radius, 0, radius * 2, radius)), (image.width - radius, 0))
    mask.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (image.width - radius, image.height - radius))
    image.putalpha(mask)
    return image

def update_time(clock_label):
    current_time = strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, lambda: update_time(clock_label))

if __name__ == "__main__":
    main()
