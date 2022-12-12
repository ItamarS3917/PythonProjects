def reversed_string(s):
    if len(s) == 0:
        return s
    else:
        return reversed_string(s[1:]) + s[0]


with open("py.txt", mode="r") as file:
    c = file.readlines()
    count = 0
    for l in c:
        count += 1

    file.seek(0)

    for i in range(count):
        e = file.readline()
        print(reversed_string(str(e)))
