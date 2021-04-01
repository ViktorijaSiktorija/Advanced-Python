# open za fajlove
file = open("/test.txt")
print(file)

# read za citanje
print(file.read())

# Pajton koristi kursor za citanje, dodamo seek
file.seek(0)
print(file.read())

# read line cita red po red
print(file.readline())
print(file.readline())

# readlines - dobije se lista koja cita sve redove
print(file.readlines())

# zatvara se rucno
file.close()
