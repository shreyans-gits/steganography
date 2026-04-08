import SecretText


cmd = str(input("Encode/Decode?: "))
if cmd == "E":
    SecretText.encode()
elif cmd == "D":
    f = input("Filename: ")
    cmd2 = input("Do you want to print to file?: ")
    if cmd2 == "Y":
        f2 = open("output.txt", "w")
        f2.write(SecretText.decode(f))
        f2.close()
    else:
        print(SecretText.decode(f))
else:
    print("Error 42069")