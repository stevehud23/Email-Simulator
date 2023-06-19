### --- OOP Email Simulator --- ###

# --- Email Class --- #

class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Initializes a new Email object.

        Parameters:
        - email_address (str): The email address of the sender.
        - subject_line (str): The subject line of the email.
        - email_content (str): The contents of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Class variable to track if the email has been read

    def mark_as_read(self):
        """
        Marks the email as read by setting the 'has_been_read' variable to True.
        """
        self.has_been_read = True

# --- Lists --- #

Inbox = []  # Empty list to store email objects

# Create 3 sample emails and add them to the Inbox list

def populate_inbox():
    """
    Populates the Inbox list with three sample email objects.
    This function is called at program startup.
    """
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Email content 1")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Email content 2")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Email content 3")
    Inbox.extend([email1, email2, email3])

# Display the email options with their subject lines and read status

def list_emails():
    """
    Lists the emails in the Inbox with their corresponding subject lines and read status.
    """
    print("\nInbox:")
    for i, email in enumerate(Inbox):
        read_status = "Read" if email.has_been_read else "Unread"
        print(f"{i} {email.subject_line} [{read_status}]")
    print()

# Read and display a selected email, and mark it as read

def read_email(index):
    """
    Reads and displays the email at the specified index in the Inbox.
    Marks the email as read if it hasn't been read already.

    Parameters:
    - index (int): The index of the email in the Inbox list.
    """
    if 0 <= index < len(Inbox):
        email = Inbox[index]
        if not email.has_been_read:
            email.mark_as_read()
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        print("Email marked as read.\n")
    else:
        print("\nInvalid email index.\n")

# Delete a selected email from the Inbox

def delete_email(index):
    """
    Deletes the email at the specified index from the Inbox.

    Parameters:
    - index (int): The index of the email in the Inbox list.
    """
    if 0 <= index < len(Inbox):
        del Inbox[index]
        print("Email deleted successfully.\n")
    else:
        print("\nInvalid email index.\n")

# Populate the Inbox with sample email objects
populate_inbox()

# Main program loop
while True:
    print("Email Simulator Menu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Delete an email")
    print("4. Quit application")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        list_emails()
        index = int(input("\nEnter the email index you want to read: "))
        read_email(index)
    elif choice == "2":
        list_emails()
    elif choice == "3":
        list_emails()
        index = int(input("\nEnter the email index you want to delete: "))
        delete_email(index)
    elif choice == "4":
        print("\nExiting the application...")
        break
    else:
        print("\nInvalid choice. Please try again.\n")