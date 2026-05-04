# PythonTempMail
Hi guys
Here you can use this python code for your temp email.

Ignore bad temp websites like temp-mail.

# Receiving E-Mails

## 1. To use, first clone the repository and enter the directory.
```ruby
git clone https://github.com/arvharan/PythonTempMail.git
cd PythonTempMail
```
## 2. Install Dependencies
   ```ruby
   pip install -r requirements.txt
```
## 3. Edit Receiver.py at line number 10 to make your username.

username rules:

  1.username must be more then 3 letters long

  2.username must contain number.

## 4. Make a password for email at line number 12
Password rules:

1.Make password strong by using al least 8 digits.

2.Dont share your pwd with anyone.

### Notes: If a username is not availble it will change your number + 1.


 ## 5. To run your py file:
 ```ruby
    python Receiver.py
 ```

# Sending Mails

## 1. Create a Mailtrap API key.
To create A Mailtrap API key.
1. Go to https://mailtrap.io and sign up.
2. You will get a API key at the starting of a account. Copy it and paste it in Receiver.py Line Number 11.

## 2. Enter Details
1. Enter the UserName in line 4 and recipient at line 5.
2. Enter the subject at line 6, text at line 7, and category(The Main Topic Of your email) at line 8.

## 3. To Run your Python File
```ruby
python Sender.py
```
