import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime

# initialize db
connection = sqlite3.connect('my_hospital_db.db')
cursor = connection.cursor()
cursor.execute('drop table if exists appoint_tab')
cursor.execute(
    "CREATE TABLE appoint_tab (doctor_name char(20), patient_name char(20), patient_ID INT(10), SLOT CHAR(20))")

# INSERT SOME DUMMY DATA
cursor.execute("INSERT INTO appoint_tab VALUES ('{}', '{}','{}','{}')".format(
    "Dr. bruse banner", "William Stand", "91231231231", 'slot3: 10:00:00'))
cursor.execute("INSERT INTO appoint_tab VALUES ('{}', '{}','{}','{}')".format(
    "Dr. Strange", "Xavier Dell", "91231111231", 'slot3: 10:00:00'))
cursor.execute("INSERT INTO appoint_tab VALUES ('{}', '{}','{}','{}')".format(
    "Dr. Doom", "Rob Will", "91001231231", 'slot3: 10:00:00'))


class Patient:
    def __init__(self):
        # style element
        self.bg_color = "#faecc6"
        self.nav_btn_bg_color = "#333333"
        self.font_style_size = ('Times new Roman', 15)

        # patient main window
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill='both', expand=True, padx=40, pady=40)
        self.main_frame.configure(bg=self.bg_color)

        # table values varibles
        self.patient_name = None
        self.patient_num = None
        self.chosen_doctor = None
        self.chosen_slot = None

        # initilizing variable to for deleting
        self.d_patient_name = None
        self.d_patient_num = None
        self.d_chosen_slot = None

        # reusable variables
        self.doctor_lst = ["Dr. Bruce Banner",
                           "Dr. Strange", "Dr. Doom", "Dr. Who", "Dr. Fate"]
        self.start_time = '09:00'
        self.start_time = datetime.datetime.strptime(
            self.start_time, '%H:%M')
        self.slot_lst = [f"Slot{
            i+1}: {(self.start_time+(datetime.timedelta(minutes=30)*i)).time()}" for i in range(16)]

    def show_patient_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Patient form
        tk.Label(self.main_frame, text="Patient Name: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=1, column=0, padx=10, pady=10)
        self.patient_name = tk.Entry(
            self.main_frame, font=('Times New Roman', 13))
        self.patient_name.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Patient Number: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=2, column=0, padx=10, pady=10)
        self.patient_num = tk.Entry(
            self.main_frame, font=('Times New Roman', 13))
        self.patient_num.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Choose Doctor: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=3, column=0, padx=10, pady=10)
        self.chosen_doctor = ttk.Combobox(
            self.main_frame, values=self.doctor_lst, font=('Time New Roman', 13))
        self.chosen_doctor.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Choose Slot: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=4, column=0, padx=10, pady=10)
        self.chosen_slot = ttk.Combobox(
            self.main_frame, values=self.slot_lst, font=('Time New Roman', 13))
        self.chosen_slot.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.main_frame, text="Book Appointment", command=self.book_patient,
                  activeforeground='green', height=2, width=20).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.main_frame, text="Cancel Appointment", command=self.cancel_appointment,
                  activeforeground='green', height=2, width=20).grid(row=5, column=3, columnspan=2, pady=10)

    def book_patient(self):
        # geeting all values from GUI to be store in DB
        patient_name = self.patient_name.get()
        patient_num = self.patient_num.get()
        chosen_doctor = self.chosen_doctor.get()
        chosen_slot = self.chosen_slot.get()

        if not patient_name:
            tk.Label(self.main_frame, text="Invalid input", font=self.font_style_size).grid(
                row=5, column=0, columnspan=2, pady=10)
            tk.Button(self.main_frame, text="Try Again", command=self.show_patient_page,
                      activeforeground='green', height=2, width=20).grid(row=5, column=0, columnspan=2, pady=10)
        else:
            check = f"select * from appoint_tab where doctor_name = '{
                chosen_doctor}' and slot = '{chosen_slot}'"
            cursor.execute(check)
            test = cursor.fetchall()
            if len(test) == 0:
                cursor.execute("INSERT INTO appoint_tab(doctor_name, patient_name, patient_id, slot) Values('{}', '{}', '{}', '{}')".format(
                    chosen_doctor, patient_name, patient_num, chosen_slot))
                connection.commit()
                tk.Label(self.main_frame, text="Appointment Booked Successfully!!!", bg=self.bg_color,
                         font=self.font_style_size, foreground='green').grid(row=6, column=1, padx=10, pady=10)
            else:
                msg = tk.Label(self.main_frame, text="Sorry slot it already booked", bg=self.bg_color,
                               font=self.font_style_size, foreground='red').grid(row=6, column=1, padx=10, pady=10)
                tk.Button(self.main_frame, text="Select another slot", command=self.show_patient_page,
                          activeforeground='green', height=2, width=20).grid(row=5, column=0, columnspan=2, pady=10)

    def cancel_appointment(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Patient form
        tk.Label(self.main_frame, text="Patient Name: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=1, column=0, padx=10, pady=10)
        self.patient_name = tk.Entry(
            self.main_frame, font=('Times New Roman', 13))
        self.patient_name.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Patient Number: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=2, column=0, padx=10, pady=10)
        self.patient_num = tk.Entry(
            self.main_frame, font=('Times New Roman', 13))
        self.patient_num.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.main_frame, text="Choose Slot: ", bg=self.bg_color,
                 font=self.font_style_size).grid(row=4, column=0, padx=10, pady=10)
        self.chosen_slot = ttk.Combobox(
            self.main_frame, values=self.slot_lst, font=('Time New Roman', 13))
        self.chosen_slot.grid(row=4, column=1, padx=10, pady=10)

        tk.Button(self.main_frame, text="Confirm Cancel Appontment", command=self.delete_data,
                  height=2, width=30, foreground='red').grid(row=5, column=0, columnspan=2, pady=10)

    def delete_data(self):
        patient_name = self.patient_name.get()
        patient_num = self.patient_num.get()
        chosen_slot = self.chosen_slot.get()

        cursor.execute("Select patient_name, patient_id, slot from appoint_tab where patient_name is '{}' AND patient_id is '{}' AND slot is '{}'".format(
            patient_name, patient_num, chosen_slot))
        if cursor.fetchall():
            cursor.execute("DELETE FROM appoint_tab WHERE patient_name = '{}' AND patient_id = '{}' AND slot = '{}'".format(
                patient_name, patient_num, chosen_slot))
            connection.commit()

            tk.Label(self.main_frame, text="Your Appointment has been Cancelled Successfully!!!", bg=self.bg_color,
                     font=self.font_style_size, foreground='red').grid(row=6, column=1, padx=10, pady=10)

            tk.Button(self.main_frame, text="Book Appointment", command=self.book_patient,
                      activeforeground='green', height=2, width=20).grid(row=5, column=3, columnspan=2, pady=10)
        else:
            tk.Label(self.main_frame, text="No data found with such detials!!", bg=self.bg_color,
                     font=self.font_style_size, foreground='red').grid(row=6, column=1, padx=10, pady=10)
            tk.Button(self.main_frame, text="Try Again", command=self.cancel_appointment,
                      foreground='orange', height=2, width=30).grid(row=5, column=0, columnspan=2, pady=10)


class Doctor(Patient):
    def __init__(self, root):
        super().__init__()
        # main window setup
        self.root = root
        self.root.title("Appointment Booking System - Zeeshan Raza")
        self.root.geometry("850x550")
        self.root.configure(background=self.bg_color)

        # nav-bar
        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(side="bottom", fill='none')
        self.nav_frame.config(background=self.bg_color)

        # navigation button
        self.patient_btn = tk.Button(self.nav_frame, text="Patient Window", command=self.show_patient_page,
                                     height=3, width=30, foreground='orange', bg=self.nav_btn_bg_color)
        self.patient_btn.pack(side="left", padx=5, pady=5)

        self.doct_nav_btn = tk.Button(self.nav_frame, text="Booked Appointments Window",
                                      command=self.show_doctor_page, height=3, width=30, foreground='orange', bg=self.nav_btn_bg_color)
        self.doct_nav_btn.pack(side="left", padx=5, pady=5)

        self.show_patient_page()

    def show_doctor_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        columns = ("#1", "#2", "#3", "#4")

        s = ttk.Style()
        s.theme_use('clam')
        # styling tree
        s.configure('Treeview.Heading', background='#e4ffe5',
                    font=self.font_style_size)

        # Booked Window
        tree = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        tree.heading("#1", text="Patient")
        tree.column("#1", anchor="center")
        tree.heading("#2", text="Doctor")
        tree.column("#2", anchor="center")
        tree.heading("#3", text="Number")
        tree.column("#3", anchor="center")
        tree.heading("#4", text="Slot")
        tree.column("#4", anchor="center")

        cursor.execute("SELECT * FROM appoint_tab")
        data = cursor.fetchall()
        for i in range(len(data)):
            tree.insert("", "end", values=(
                data[i][1], data[i][0], data[i][2], data[i][3]))
            tree.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = Doctor(root)
    root.mainloop()
