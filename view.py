import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class EmployeeView:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#2c3e50")

        self.name = StringVar()
        self.age = StringVar()
        self.doj = StringVar()
        self.gender = StringVar()
        self.email = StringVar()
        self.contact = StringVar()

        # Entries Frame
        self.entries_frame = Frame(root, bg="#535c68")
        self.entries_frame.pack(side=TOP, fill=X)
        self.title = Label(self.entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
        self.title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

        self.lblName = Label(self.entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txtName = Entry(self.entries_frame, textvariable=self.name, font=("Calibri", 16), width=30)
        self.txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lblAge = Label(self.entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txtAge = Entry(self.entries_frame, textvariable=self.age, font=("Calibri", 16), width=30)
        self.txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lbldoj = Label(self.entries_frame, text="D.O.J", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txtDoj = Entry(self.entries_frame, textvariable=self.doj, font=("Calibri", 16), width=30)
        self.txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lblEmail = Label(self.entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.txtEmail = Entry(self.entries_frame, textvariable=self.email, font=("Calibri", 16), width=30)
        self.txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        self.lblGender = Label(self.entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.comboGender = ttk.Combobox(self.entries_frame, font=("Calibri", 16), width=28, textvariable=self.gender, state="readonly")
        self.comboGender['values'] = ("Male", "Female")
        self.comboGender.grid(row=3, column=1, padx=10, sticky="w")

        self.lblContact = Label(self.entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.txtContact = Entry(self.entries_frame, textvariable=self.contact, font=("Calibri", 16), width=30)
        self.txtContact.grid(row=3, column=3, padx=10, sticky="w")

        self.lblAddress = Label(self.entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
        self.lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.txtAddress = Text(self.entries_frame, width=85, height=5, font=("Calibri", 16))
        self.txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

        self.btn_frame = Frame(self.entries_frame, bg="#535c68")
        self.btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        self.btnAdd = Button(self.btn_frame, command=self.add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                        bg="#16a085", bd=0)
        self.btnAdd.grid(row=0, column=0)
        self.btnEdit = Button(self.btn_frame, command=self.update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                        fg="white", bg="#2980b9", bd=0)
        self.btnEdit.grid(row=0, column=1, padx=10)
        self.btnDelete = Button(self.btn_frame, command=self.delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                          fg="white", bg="#c0392b", bd=0)
        self.btnDelete.grid(row=0, column=2, padx=10)
        self.btnClear = Button(self.btn_frame, command=self.clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                          bg="#f39c12", bd=0)
        self.btnClear.grid(row=0, column=3, padx=10)

        # Table Frame
        self.tree_frame = Frame(root, bg="#ecf0f1")
        self.tree_frame.place(x=0, y=480, width=1980, height=520)
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 18), rowheight=50)
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))
        self.tv = ttk.Treeview(self.tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=5)
        self.tv.heading("2", text="Name")
        self.tv.heading("3", text="Age")
        self.tv.column("3", width=5)
        self.tv.heading("4", text="D.O.B")
        self.tv.column("4", width=10)
        self.tv.heading("5", text="Email")
        self.tv.heading("6", text="Gender")
        self.tv.column("6", width=10)
        self.tv.heading("7", text="Contact")
        self.tv.heading("8", text="Address")
        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)

        self.displayAll()

    def getData(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        self.name.set(row[1])
        self.age.set(row[2])
        self.doj.set(row[3])
        self.email.set(row[4])
        self.gender.set(row[5])
        self.contact.set(row[6])
        self.txtAddress.delete(1.0, END)
        self.txtAddress.insert(END, row[7])

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        try:
            response = requests.get("http://localhost:5000/employees")  # Sending GET request to fetch all employees
            if response.status_code == 200:
                employees = response.json()
                for employee in employees:
                    self.tv.insert("", END, values=employee)
            else:
                messagebox.showerror("Error", f"Failed to fetch employees: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching employees: {str(e)}")
            print("Error:", str(e))


    def add_employee(self):
        if self.txtName.get() == "" or self.txtAge.get() == "" or self.txtDoj.get() == "" or self.txtEmail.get() == "" or self.comboGender.get() == "" or self.txtContact.get() == "" or self.txtAddress.get(1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return

        data = {
            "name": self.txtName.get(),
            "age": self.txtAge.get(),
            "doj": self.txtDoj.get(),
            "email": self.txtEmail.get(),
            "gender": self.comboGender.get(),
            "contact": self.txtContact.get(),
            "address": self.txtAddress.get(1.0, END)
        }

        response = requests.post("http://localhost:5000/employees", json=data)  # Sending POST request to add an employee
        if response.status_code == 200:
            messagebox.showinfo("Success", "Record Inserted")
            self.clearAll()
            self.displayAll()
        else:
            messagebox.showerror("Error", "Failed to insert record")

    def update_employee(self):
        if self.txtName.get() == "" or self.txtAge.get() == "" or self.txtDoj.get() == "" or self.txtEmail.get() == "" or self.comboGender.get() == "" or self.txtContact.get() == "" or self.txtAddress.get(1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return

        if not row:
            messagebox.showerror("Error", "Please select an employee to update")
            return

        data = {
            "name": self.txtName.get(),
            "age": self.txtAge.get(),
            "doj": self.txtDoj.get(),
            "email": self.txtEmail.get(),
            "gender": self.comboGender.get(),
            "contact": self.txtContact.get(),
            "address": self.txtAddress.get(1.0, END)
        }

        response = requests.put(f"http://localhost:5000/employees/{row[0]}", json=data)  # Sending PUT request to update an employee
        if response.status_code == 200:
            messagebox.showinfo("Success", "Record Updated")
            self.clearAll()
            self.displayAll()
        else:
            messagebox.showerror("Error", "Failed to update record")

    def delete_employee(self):
        if not row:
            messagebox.showerror("Error", "Please select an employee to delete")
            return

        response = requests.delete(f"http://localhost:5000/employees/{row[0]}")  # Sending DELETE request to delete an employee
        if response.status_code == 200:
            messagebox.showinfo("Success", "Record Deleted")
            self.clearAll()
            self.displayAll()
        else:
            messagebox.showerror("Error", "Failed to delete record")

    def clearAll(self):
        self.name.set("")
        self.age.set("")
        self.doj.set("")
        self.gender.set("")
        self.email.set("")
        self.contact.set("")
        self.txtAddress.delete(1.0, END)

def main():
    root = Tk()
    app = EmployeeView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
