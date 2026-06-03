# Ask the user to enter a word until the word contains the letter "h".
# Both lowercase "h" and uppercase "H" should be accepted.
# The loop should not stop if the entered word does not contain "h" or "H".

user_word = input("Please enter a word: ")

while "h" not in user_word.lower():
    user_word = input("Please try again: ")
else:
    print("krasav4ik")

# The loop stops automatically when the condition becomes False,
# so an else block is not required here.