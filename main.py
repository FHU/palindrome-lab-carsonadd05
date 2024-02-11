def palindrome(text):
    # Remove white spaces and convert text to lowercase
    text = text.replace(" ", "").lower()
    # Check if the text is equal to its reverse
    return text == text[::-1] and text != ""

if __name__ == "__main__":
    user_input = input("Enter a text: ")
    print(palindrome(user_input))