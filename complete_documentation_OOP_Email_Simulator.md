=============================================================================
                            OOP Email Simulator
=============================================================================

Table of Contents:
------------------
1. Introduction
2. Usage
3. Class Documentation
    3.1. EmailSimulatorApp
    3.2. Email

1. Introduction:
----------------
The OOP Email Simulator is a simple application that simulates an email inbox and provides various operations such as viewing emails, marking emails as read, deleting emails, and running another script. The application is built using the Tkinter library in Python and follows the object-oriented programming (OOP) paradigm.

2. Usage:
---------
To use the OOP Email Simulator, follow these steps:
1. Run the script using a Python interpreter.
2. The application window will open, displaying a menu with several options.
3. Choose an option from the menu to perform the corresponding operation.
4. Follow the on-screen instructions or prompts, if any.
5. To exit the application, select the "Quit" option from the menu or click the window's close button (X).

3. Class Documentation:
-----------------------
3.1. EmailSimulatorApp:
    - This class represents the main application window and its functionality.
    - Attributes:
        - root: The Tkinter root window object.
        - option_var: A Tkinter StringVar to store the selected option from the menu.
        - option_menu: A Tkinter OptionMenu widget for the menu selection.
        - email_listbox: A Tkinter Listbox widget to display the emails.
        - ok_button: A Tkinter Button widget for the OK action.
    - Methods:
        - __init__(): Initializes the EmailSimulatorApp instance and creates the application window.
        - populate_inbox(): Populates the inbox with sample email instances.
        - option_selected(selected_option): Callback function for the menu selection.
        - list_emails(): Displays all emails in the email_listbox.
        - list_unread_emails(): Displays only unread emails in the email_listbox.
        - mark_email_as_read(): Marks selected emails as read or deletes them based on the selected option.
        - read_email(index): Displays the details of the selected email.
        - delete_email(index): Deletes the selected email from the inbox.
        - read_and_run_file(): Executes the OOP_Email_simulator.py script after confirming with the user.
        - quit_app(): Destroys the application window and exits the program.
        - confirm_cancel(): Displays a confirmation dialog for canceling the operation or closing the window.

3.2. Email:
    - This class represents an email message.
    - Attributes:
        - email_address: The sender's email address.
        - subject_line: The subject line of the email.
        - email_content: The content or body of the email.
        - has_been_read: A boolean flag indicating whether the email has been read.
    - Methods:
        - mark_as_read(): Marks the email as read by setting the has_been_read attribute to True.

Note: The code provided in the documentation may not include the complete implementation details. Please refer to the actual code for the complete implementation.

=============================================================================


