

my_file = open("input.txt", "r")


with open("name.txt", "r") as myfile:
    names = myfile.read().splitlines()
    for name in names:
        print(name)


with requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)") as response:
     response.raise_for_status()