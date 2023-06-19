import tkinter as tk            # imports tkinter and sets it's name as tk 
from tkinter import messagebox  # imports message box from tkinter library
import subprocess               # a powerful tool for executing external commands and interacting with the underlying operating system from within Python code
from PIL import ImageTk, Image  # using pillow to import an image used for background

class EmailSimulatorApp:
    """
    A class representing the OOP Email Simulator application.
    """

    def __init__(self):
        """
        Initializes the EmailSimulatorApp class.
        """
        self.root = tk.Tk()
        self.root.title("OOP Email Simulator")

        # Set the default window size
        self.root.geometry("450x275")

        self.root.bind("<Configure>", self.resize_background)

        # Load the background image
        self.original_image = Image.open("OIP.png")
        self.background_image = ImageTk.PhotoImage(self.original_image)

        # Create a Label widget with the background image
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.protocol("WM_DELETE_WINDOW", self.confirm_cancel)
        """
        create an OptionMenu widget (self.option_menu) within the root window (self.root)
        position the OptionMenu widget within the root window, place in center, and color of widget is red.
        """
        self.option_var = tk.StringVar()
        self.option_menu = tk.OptionMenu(self.root, self.option_var, "Inbox", "View Unread Emails", "Delete Email", "Quit", "Read and Run OOP_Email_simulator.py", command=self.option_selected)
        self.option_menu.place(relx=0.2, rely=0.1, anchor=tk.CENTER)
        self.option_menu.configure(bg="red")
        """
        Listbox widget within the root window (self.root). The Listbox is used to display a list of emails.
        place method is used to position the Listbox widget within the root window.
        """
        self.email_listbox = tk.Listbox(self.root, width=50)
        self.email_listbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.email_listbox.configure(bg="light blue")
        """"
        Button widget (self.ok_button) within the root window (self.root). 
        The button is labeled "OK" and has the command self.mark_email_as_read assigned to it.
        """
        self.ok_button = tk.Button(self.root, text="OK", command=self.mark_email_as_read)
        self.ok_button.place(relx=0.8, rely=0.10, anchor=tk.CENTER)

        self.populate_inbox()

    def resize_background(self, event):
        """
        Resizes the background image to fit the window.
        """
        if event.widget == self.root:
            width = event.width
            height = event.height
            resized_image = self.original_image.resize((width, height), Image.LANCZOS)
            self.background_image = ImageTk.PhotoImage(resized_image)
            self.background_label.configure(image=self.background_image)

    def populate_inbox(self):
        """
        Populates the inbox with sample emails.
        """
        email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Email content 1")
        email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Email content 2")
        email3 = Email("sender3@example.com", "Your excellent marks!", "Email content 3")
        Inbox.extend([email1, email2, email3])

    def option_selected(self, selected_option):
        """
        Handles the selection of options from the menu.
        
        Args:
            selected_option (str): The selected option from the menu.
        """
        if selected_option == "Inbox":
            self.list_emails()
            self.ok_button.config(state=tk.NORMAL)
        elif selected_option == "View Unread Emails":
            self.list_unread_emails()
            self.ok_button.config(state=tk.DISABLED)
        elif selected_option == "Delete Email":
            self.list_emails()
            self.ok_button.config(state=tk.NORMAL)
        elif selected_option == "Quit":
            self.quit_app()
        elif selected_option == "Read and Run OOP_Email_simulator.py":
            self.read_and_run_file()

    def list_emails(self):
        """
        Lists all emails in the inbox.
        """
        self.email_listbox.delete(0, tk.END)
        for i, email in enumerate(Inbox):
            read_status = "Read" if email.has_been_read else "Unread"
            self.email_listbox.insert(tk.END, f"{i} {email.subject_line} [{read_status}]")

    def list_unread_emails(self):
        """
        Lists only the unread emails in the inbox.
        """
        self.email_listbox.delete(0, tk.END)
        for i, email in enumerate(Inbox):
            if not email.has_been_read:
                self.email_listbox.insert(tk.END, f"{i} {email.subject_line}")

    def mark_email_as_read(self):
        """
        Marks the selected email as read and displays its details.
        """
        selected_email_indices = self.email_listbox.curselection()
        if not selected_email_indices:
            messagebox.showerror("Error", "Please select an option from the menu list and select OK.")
            return

        if self.option_var.get() == "Inbox":
            for index in selected_email_indices:
                self.read_email(int(index))
        elif self.option_var.get() == "Delete Email":
            response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected email(s)?")
            if response == tk.YES:
                selected_email_indices = sorted(selected_email_indices, reverse=True)
                for index in selected_email_indices:
                    self.delete_email(int(index))
            else:
                messagebox.showinfo("Deletion Canceled", "Deletion of selected email(s) canceled.")
            self.list_emails()

    def read_email(self, index):
        """
        Reads the details of the selected email and marks it as read.
        
        Args:
            index (int): The index of the selected email.
        """
        email = Inbox[index]
        if not email.has_been_read:
            email.mark_as_read()
        messagebox.showinfo("Email Details", f"Subject: {email.subject_line}\nFrom: {email.email_address}\nContent: {email.email_content}")
        self.list_emails()

    def delete_email(self, index):
        """
        Deletes the selected email.
        
        Args:
            index (int): The index of the selected email.
        """
        del Inbox[index]

    def read_and_run_file(self):
        """
        Reads and runs the OOP_Email_simulator.py file.
        """
        response = messagebox.askokcancel("Confirmation", "Are you sure you want to read and run OOP_Email_simulator.py?")
        if response:
            custom_message = '''This will execute OOP_Email_simulator.py in your python terminal:
                            \nThis file was the original and was intended to show the use of OOP,lists,functions
                            \nI fully implemented this code into email.py and gave it: \nVery basic UI design: \nMenu options with basic functionality: \nError handling:
                            \nThis was my last coding challenge for HyperionDev '''
            messagebox.showinfo("Custom Message", custom_message)
            subprocess.run(["python", "OOP_Email_simulator.py"])

    def quit_app(self):
        """
        Quits the application.
        """
        self.root.destroy()

    def confirm_cancel(self):
        """
        Asks for confirmation before canceling the application.
        """
        response = messagebox.askyesno("Confirmation", "Are you sure you want to cancel?")
        if response:
            self.root.destroy()

class Email:
    """
    A class representing an email.
    """

    def __init__(self, email_address, subject_line, email_content):
        """
        Initializes the Email class.

        Args:
            email_address (str): The email address of the sender.
            subject_line (str): The subject line of the email.
            email_content (str): The content of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """
        Marks the email as read.
        """
        self.has_been_read = True

# Global Inbox list
Inbox = []

# Create and run the EmailSimulatorApp instance
app = EmailSimulatorApp()
app.root.mainloop()

"""
this simple app was made with the help of some handy resources.
Also my lecturers yolandi and armand have coached me very well with the understanding of OOP and other concepts
never done this before, just wanted to give it a try and made use of some resources for imports and documentation skills

ref: https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/
ref: https://www.geeksforgeeks.org/python-gui-tkinter/
"""


