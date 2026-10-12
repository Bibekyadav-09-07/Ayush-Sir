# Import the pyjokes library
import pyjokes
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Display three different jokes
print("😄 Welcome to the Python Joke Generator! 🤖")

for i in range(3):
    joke = pyjokes.get_joke()
    print(f"\n😂 Joke {i + 1}:")
    print(f"💬 {joke}")

# Ask the user whether they want another joke
choice = input("\n😊 Do you want another joke? (yes/no): ").strip().lower()

# Display another joke if the user enters yes
while choice == "yes":
    print("\n🎉 Here is another joke:")
    print(f"💬 {pyjokes.get_joke()}")

    choice = input("\n😊 Do you want another joke? (yes/no): ").strip().lower()

print("👋 Thank you for using the Joke Generator! 😄")