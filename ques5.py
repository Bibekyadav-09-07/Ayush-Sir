
import qrcode

# Ask for name and message
name = input("Enter your name: ")
message = input("Enter a short message: ")

# Generate a personal QR code
personal_text = f"Name: {name}\nMessage: {message}"
personal_qr = qrcode.make(personal_text)
personal_qr.save("personal_qrcode.png")

print("✅ Personal QR code saved as personal_qrcode.png")

# Ask for a favorite website
website = input("Enter your favorite website URL: ")

# Add https:// if needed
if not website.startswith(("http://", "https://")):
    website = "https://" + website

# Generate and save the website QR code
website_qr = qrcode.make(website)
website_qr.save("favorite_website_qrcode.png")

print("✅ Website QR code saved as favorite_website_qrcode.png")
print("📱 Scan the QR codes using your phone.")
