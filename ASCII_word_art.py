import pyfiglet
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Accept input from the user for the text
text = input("Enter the text you want to display: ")

# Check if input is empty
if not text.strip():
    print("You must enter some text!")
else:
    # Generate the ASCII art
    ascii_art = pyfiglet.figlet_format(text)

    # Print the ASCII art in blue color
    print(Fore.BLUE + ascii_art)

    # Save the ASCII art to a file
    output_file = "ascii_art_output.txt"
    with open(output_file, "w") as file:
        file.write(ascii_art)
    
    print(f"ASCII art has been saved to {output_file}")
