import sys
def main():
    # Check if exactly one argument is passed (excluding the script name)
    if len(sys.argv) != 2:
        print("Usage: python helloworld.py [name]")
        return

    # Get the name from the command-line argument
    name = sys.argv[1]

    # Print the greeting
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()