# ovo je standard za citanje
with open('/test.txt', mode='a') as file1:

    # pisanje
    # difolt parametar mode="r", to je read
    # za pisanje mode="w"
    # "r+" za citanje i pisanje
    # mode="a" apenduje/doda na kraj fajla, zbog kursora
    text1 = file1.write('cao it\'s me')
    print(file1)

# za pravljenje fajla mode='w' i overrajtuje ako vec postoji
with open('/test2.txt', mode='w') as file2:
    text2 = file2.write('lalal')
    print(text2)

# ako ne moze da nadje, try except i FileNotFoundEror
try:
    with open('./test2.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('ne postoji')
    raise err

# IOError
