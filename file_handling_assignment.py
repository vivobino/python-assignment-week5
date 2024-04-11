def main():
    # Open the file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write lines of text to the file
        file.write("Hello, this is line 1.\n")
        file.write("12345 is a number.\n")
        file.write("Writing to files is fun!\n")

if __name__ == "__main__":
    main()
with open("my_file.txt", "r") as file:
        # Read and display each line
        for line in file:
            print(line.strip())
with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("The file now has more content!\n")
        file.write("Appending more text here.\n")
        
except FileNotFoundError:
        print("File not found. Please check the file path.")
except PermissionError:
        print("Permission denied. Check file permissions.")
except Exception as e:
        print(f"An error occurred: {e}")
finally:
        print("Script execution complete.")       

        