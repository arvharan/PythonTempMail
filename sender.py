import mailtrap as mt

API_TOKEN = "<YOUR_API_TOKEN>"  # your API key here https://mailtrap.io/api-tokens

client = mt.MailtrapClient(token=API_TOKEN)

# Create mail object
mail = mt.Mail(
    sender=mt.Address(email="sender@example.com", name="John Smith"),
    to=[mt.Address(email="recipient@example.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
)

client.send(mail) 