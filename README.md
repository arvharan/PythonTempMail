# PythonTempMail

A simple Python library to generate temporary email addresses and read messages using a public temp mail API.

---

## 🚀 Features

- Generate temporary email addresses instantly
- Fetch inbox messages easily
- Lightweight and simple API
- Beginner-friendly design

---

## 📦 Installation

1. Clone the repository, and enter the directory:

```ruby
git clone https://github.com/arvharan/PythonTempMail.git
cd PythonTempMail
```

2. Install Dependencies:

```ruby
pip install -r requirements.txt
```

## 🧪 Usage

```ruby
from tempmail import TempMail

mail = TempMail()

print(mail.email)
```

## 📬 Get Messages

```ruby
messages = mail.get_messages()

for msg in messages:
    print(msg)
    ```

## 📌 Example

```ruby
from tempmail import TempMail

mail = TempMail()

print("Temporary Email:", mail.email)

messages = mail.get_messages()

if messages:
    for msg in messages:
        print(msg)
```

🛠️ Requirements
1. Python 3.x
2. requests

📄 License

MIT License

