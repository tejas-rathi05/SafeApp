# SafeApp
Password Manager &amp; Generator

Safe is a password manager and password generator. It is a user-friendly desktop app that generates strong complex passwords and stores it in your own database protected by a user root password. This app can only be used for personal use or for personal enterprise to save data of their employees; it is not recommended for third party use.

This project has only one module “safe.py”. All the functionalities of this project are written in the class SafeApp(MDApp) which contains the following user defined functions:

### 1. view_table(self):
view_table(self) function is used to view MDTable which stores user entered data(stored in MySQL).

### 2. hide_table(self):
hide_table(self) function is used to hide MDTable.

### 3. check_press(self, instance table, current_row):
This function helps to copy checked user’s password.

### 4. submit(self, username,email,password):
This function submits the user entered details and simultaneously saves them in the local host server of the MySQL database.

### 5. generate(self, length):
generate(self, length) is used to generate strong passwords of unlimited length.

### 6. show_pwd(self):
show_pwd(self) is used to show the generated password on screen.

### 7. copy_pwd(self):
copy_pwd(self) function is used to copy the generated password and to display a pop-up message of successfully copying the password in the clipboard.


### 8. clear_fields(self):
After the submission of all the details by the user there should be a function to remove previously entered data and this is what this clear_fields(self) rightly does.

The backend part of this project is powered by MySQL database which basically stores the user entered data in the localhost server. The created database PasswordManager has only one table “manager”, which safely stores User Name, E- mail address, and password.

