# Function to count the number of words in the input text
def count_words(text):
    # Split the input text into words and return the length of the resulting list
    words = text.split()
    return len(words)

def main():
    while True:
        try:
            # Tell the user to enter a sentence or paragraph
            user_input = input("Enter a sentence or paragraph: ")
        
            # Check if the input is not empty (after stripping any whitespace)
            if user_input.strip():
                # Count the number of words in the input
                word_count = count_words(user_input)
            # Display the word count to the user
                print(f"Word count: {word_count}")
            # Break the loop if a valid input is provided
                break
            else:
            # Display an error message if the input is empty
                print("Error: Empty input. Please enter some text.")
        except Exception as e:
            # Display a general error message for any unexpected errors
            
            print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
