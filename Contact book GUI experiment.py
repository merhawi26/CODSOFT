# Task 5: Contact Book

import tkinter as tk
from tkinter import messagebox, simpledialog, font as tkfont
import csv
import re


class ContactBook:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contact Book")
        self.root.geometry("500x600")
        self.root.configure(bg="#2A2A2A")

        # Font Styles
        header_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
        button_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        # Header Label
        self.header_label = tk.Label(
            self.root,
            text="My Contact Book",
            font=header_font,
            fg="#FFD700",
            bg="#2A2A2A",
        )
        self.header_label.pack(pady=(10, 10))

        # Display Box
        self.text_box = tk.Text(
            self.root,
            height=15,
            width=50,
            bg="#FFF8DC",
            fg="#000000",
            font=("Helvetica", 10),
            relief="sunken",
            bd=2,
        )
        self.text_box.pack(pady=(10, 10))

        # Buttons
        buttons_frame = tk.Frame(self.root, bg="#2A2A2A")
        buttons_frame.pack(pady=20)

        # Initializing Buttons
        self.create_button(
            "Add Contact", self.add, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "View Contacts", self.view, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Search Contact", self.search, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Update Contact", self.update, buttons_frame, button_font, "#4682B4"
        )
        self.create_button(
            "Delete Contact", self.delete, buttons_frame, button_font, "#FF6347"
        )
        self.create_button(
            "Exit", self.root.destroy, buttons_frame, button_font, "#FF6347"
        )

        # Load contacts from file
        self.contact_book = self.read_from_file()

        self.root.mainloop()

    def create_button(self, text, command, frame, font, color):
        button = tk.Button(
            frame,
            text=text,
            command=command,
            font=font,
            bg=color,
            fg="#FFFFFF",
            relief="flat",
            width=15,
        )
        button.pack(pady=5, padx=5)

    # Load contacts from file
    def read_from_file(self, filename="Contact Book.csv"):
        contacts = []
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:  # Ensure the row has all four fields
                        contact = {
                            "name": row[0],
                            "phone": row[1],
                            "email": row[2],
                            "address": row[3],
                        }
                        contacts.append(contact)
        except FileNotFoundError:
            pass
        return contacts

    # Write the contacts into file
    def write_to_file(self, contacts, filename="Contact Book.csv"):
        with open(filename, "w") as file:
            writer = csv.writer(file)
            for contact in contacts:
                writer.writerow(contact.values())

    # Function that checks duplicate name
    def duplicate_name(self, name):
        if any(
            contact["name"].lower() == name.lower() for contact in self.contact_book
        ):
            return True
        return False

    # Function that checks duplicate phone numbers
    def duplicate_phone(self, phone):
        if any(contact["phone"] == phone for contact in self.contact_book):

            return True
        return False

    # Function that accept new contacts from the user and write them into file
    def add(self):
        # Checks user input name is null
        while True:
            name = simpledialog.askstring("Input", "Enter the name(*):")
            if name == "":
                messagebox.showwarning("Input Error", "Name is required.")
                continue
            break
        # Checks user input phone number whether it is null and starts with +251
        while True:
            phone = simpledialog.askstring("Input", "Enter the phone number(*):")
            if phone == "":
                messagebox.showwarning("Input Error", "Phone number is required.")
                continue
            if not re.match(r"^\+251[0-9]{9}$", phone):
                messagebox.showwarning(
                    "Warning",
                    "Invalid Ethiopian phone number format, It should start with '+251' and have 9 digits.",
                )
                continue
            break
        # Checks user input email
        while True:
            email = simpledialog.askstring("Input", "Enter the email:")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showwarning(
                    "Warning", "Invalid email format (Ex : example@gmail.com)."
                )
                continue
            break

        address = simpledialog.askstring("Input", "Enter the address (optional):")

        # Checks (name and phone) whether the contact added already exists or not
        if self.duplicate_name(name):
            messagebox.showwarning(
                "Warning", "A contact with this name already exists."
            )
            return
        if self.duplicate_phone(phone):
            messagebox.showwarning(
                "Warning", "A contact with this phone number already exists."
            )
            return
        # To add contacts name and phone are required
        if name and phone:
            contact = {
                "name": name.strip().title(),
                "phone": phone.strip(),
                "email": email.strip().lower(),
                "address": address.strip().title(),
            }
            # Add contact dictionary into a list
            self.contact_book.append(contact)
            # Write the contacts into a file
            self.write_to_file(self.contact_book)
            messagebox.showinfo("Success", "Contact added successfully!")
            # Display added contact and the rest on textbox
            self.view()
            return
        else:
            messagebox.showwarning("warning", "Name and phone number are required.")

    # Function that display contacts list
    def view(self):
        self.text_box.delete(1.0, tk.END)
        if not self.contact_book:
            self.text_box.insert(tk.END, "No contacts found.\n")
        else:
            for contact in self.contact_book:
                self.text_box.insert(tk.END, f"Name: {contact['name']}\n")
                self.text_box.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.text_box.insert(tk.END, f"Email: {contact['email']}\n")
                self.text_box.insert(tk.END, f"Address: {contact['address']}\n\n")

    # Function that used to search specific contact name from contacts
    def search(self):
        search_name = simpledialog.askstring("Search", "Enter the name to search:")
        search_name = search_name.strip().title()
        found = False
        self.text_box.delete(1.0, tk.END)
        for contact in self.contact_book:
            if contact["name"] == search_name:
                self.text_box.insert(tk.END, f"Contact Found:\n")
                self.text_box.insert(tk.END, f"Name: {contact['name']}\n")
                self.text_box.insert(tk.END, f"Phone: {contact['phone']}\n")
                self.text_box.insert(tk.END, f"Email: {contact['email']}\n")
                self.text_box.insert(tk.END, f"Address: {contact['address']}\n\n")
                found = True
                break
        if not found:
            messagebox.showwarning("warning", "Contact Not Found")

    # Function that used to update contact details
    def update(self):
        name_to_update = simpledialog.askstring(
            "Update", "Enter the name of the contact to update:"
        )
        name_to_update = name_to_update.strip().title()
        for contact in self.contact_book:
            if contact["name"] == name_to_update:
                new_name = simpledialog.askstring(
                    "Update", "Enter new name (leave blank to keep current):"
                )
                new_phone = simpledialog.askstring(
                    "Update", "Enter new phone (leave blank to keep current):"
                )
                new_email = simpledialog.askstring(
                    "Update", "Enter new email (leave blank to keep current):"
                )
                new_address = simpledialog.askstring(
                    "Update", "Enter new address (leave blank to keep current):"
                )
                # Here also we use both functions (validate name and validate phone)
                if self.duplicate_name(new_name):
                    messagebox.showwarning(
                        "Warning", "A contact with this name already exists."
                    )
                    return
                if self.duplicate_phone(new_phone):
                    messagebox.showwarning(
                        "Warning", "A contact with this phone number already exists."
                    )
                    return
                # Updating the contacts with new ones
                contact["name"] = (
                    new_name.strip().title() if new_name else contact["name"]
                )
                contact["phone"] = new_phone.strip() if new_phone else contact["phone"]
                contact["email"] = (
                    new_email.strip().lower() if new_email else contact["email"]
                )
                contact["address"] = (
                    new_address.strip().title() if new_address else contact["address"]
                )
                # Writing these updated contacts into a file
                self.write_to_file(self.contact_book)
                messagebox.showinfo("Success", "Contact updated successfully!")
                # Display contacts with updates
                self.view()
                return
        messagebox.showwarning("Not Found", "Contact Not Found")

    # Function that helps us to specific contact from contacts
    def delete(self):
        delete_name = simpledialog.askstring(
            "Delete", "Enter the name of the contact to delete:"
        )
        delete_name = delete_name.strip().title()
        for contact in self.contact_book:
            # Checks the name that will be removed
            if contact["name"] == delete_name:
                # Remove the contact from contact book or list
                self.contact_book.remove(contact)
                # Then write into a file after removal of the contact to update the contact book
                self.write_to_file(self.contact_book)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                self.view()
                return
        messagebox.showwarning("Not Found", "Contact Not Found")


ContactBook()
