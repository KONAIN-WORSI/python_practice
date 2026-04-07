# with open("data.txt", "r") as f:
#     content = f.read()

# print(content)

# content = "Hello, World!\n" \
# "This is a sample text file.\n" \
# "Python is great for file handling.\n" \

# with open("output.txt", "w") as f:
#     f.write(content)


# with open("log.txt", 'a') as f:
#     # f.write("New log entry: This is a new log message.\n")
#     f.write("Another log entry: Logging is important for debugging.\n")



with open("file.txt", "r+") as f:
    content = f.read()
    print("Original Content:")
    print(content)
    f.seek(0)  
    f.write("start\n")