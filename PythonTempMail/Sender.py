import mailtrap as mt

mail = mt.Mail(
    sender=mt.Address(email="yourusename@demomailtrap.co", name="Mailtrap Test"),
    to=[mt.Address(email="recipient@example.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    category="Integration Test",
)

client = mt.MailtrapClient(token="your api token here")
response = client.send(mail)

print(response)