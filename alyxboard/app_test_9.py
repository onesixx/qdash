import alyxdash

# Get the absolute path to the "midsummer.txt" file in the data directory
file_path = alyxdash.__path__[0] + "/data/midsummer.txt"

# Open the file and read its contents
with open(file_path, 'r') as file:
    text = file.read()

# Print the contents of the file
print(text)
