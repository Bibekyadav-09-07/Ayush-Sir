
import emoji

# Ask for the user's name
name = input("Enter your name: ")

# Display a welcome message
print(f"Hello {name}! {emoji.emojize(':smiling_face_with_smiling_eyes:')}")

# Ask for the favorite activity
activity = input("Enter your favorite activity: ")

# Display a personalized greeting
print(f"Your favorite activity is {activity}! ❤️")
print(f"Keep learning Python! {emoji.emojize(':thumbs_up:')}")
