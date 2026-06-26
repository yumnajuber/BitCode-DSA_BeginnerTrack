# Python sets __name__ to "__main__" when this file is run directly.
# This condition prevents code from running if the file is imported elsewhere. It prevents the imported file from running automatically, but still allows other files to use its tools (functions, classes) whenever they want.
if __name__ == '__main__':
    print("Hello, Bitcode DSA!")

