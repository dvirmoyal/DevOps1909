
current_name = input("what is your name: ")


my_file = open("name.txt", "a")
my_file.write(current_name + "\n")
my_file.close()

my_file = open("name.txt", "r")
for name in my_file.readlines():
    if "n" in name:
     print(f"hello {name}")
my_file.close()