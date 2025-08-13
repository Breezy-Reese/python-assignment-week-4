def modify_content(content):
    """
    Example modification: convert text to uppercase.
    You can change this logic to any transformation you want.
    """
    return content.upper()

try:
    # Ask the user for the file name to read
    input_file = input("Enter the name of the file to read: ")

    # Try opening and reading the file
    with open(input_file, "r") as file:
        original_content = file.read()

    # Modify the file content
    modified_content = modify_content(original_content)

    # Ask for the output file name
    output_file = input("Enter the name of the new file to write to: ")

    # Write the modified content to the new file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"✅ File has been read from '{input_file}' and written to '{output_file}' successfully!")

except FileNotFoundError:
    print("❌ Error: The file you entered does not exist. Please check the file name and try again.")

except PermissionError:
    print("❌ Error: You do not have permission to read or write this file.")

except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
