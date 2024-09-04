import tkinter as tk
from tkinter import ttk, messagebox
from facedetection import facedetection
def show_student_info(root, windows):
    if "student_window" in windows and tk.Toplevel.winfo_exists(windows["student_window"]):
        windows["student_window"].lift()
        return

    # Open a new window for student information
    student_window = tk.Toplevel(root)
    student_window.title("Student Information")
    student_window.geometry("400x300")
    student_window.configure(bg="lightblue")
    windows["student_window"] = student_window

    # Customize Combobox style
    style = ttk.Style()
    style.configure('TCombobox', background='white', fieldbackground='white', foreground='black')
    style.map('TCombobox', fieldbackground=[('readonly', 'white')])

    # Branch selection
    branch_label = tk.Label(student_window, text="Select Branch:", font=('Helvetica', 12, 'bold'), bg="lightblue")
    branch_label.pack(pady=10)
    
    branches = ("Computer Science", "Electrical", "Mechanical", "Civil", "electromics And Communication")
    branch_var = tk.StringVar()
    branch_combobox = ttk.Combobox(student_window, textvariable=branch_var, values=branches, state="readonly", width=30, style='TCombobox')
    branch_combobox.set("Select Branch")
    branch_combobox.pack(pady=5)

    # Academic year selection
    year_label = tk.Label(student_window, text="Select Academic Year:", font=('Times New Roman', 10, 'bold'), bg="lightblue")
    year_label.pack(pady=10)
    
    years = ("2020", "2021", "2022", "2023", "2024")
    year_var = tk.StringVar()
    year_combobox = ttk.Combobox(student_window, textvariable=year_var, values=years, state="readonly", width=30, style='TCombobox')
    year_combobox.set("Select Academic Year")
    year_combobox.pack(pady=5)

    # Proceed button
    proceed_button = tk.Button(student_window, text="Proceed", font=('Times New Roman', 10, 'bold'), command=lambda: proceed(branch_var.get(), year_var.get()))
    proceed_button.pack(pady=20)

def proceed(branch, year):
    years = ("2020", "2021", "2022", "2023", "2024")
    branches = ("Computer Science", "Electrical", "Mechanical", "Civil", "electromics And Communication")
    if branch in branches and year in years:
      print(branch,year)
      facedetection()
    else:
        messagebox.showwarning("Incomplete Selection", "Please select both branch and academic year.")
    
   
    


    