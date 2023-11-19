import random
symvols="1234567890=+-_()&amp;^><?;:qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,#№!$%*{}[]"
paroll=""
lenght=0
password=0
print("введите длинну пароля")
lenght=int(input())
for i in range(lenght):
    paroll+=random.choice(symvols)
print(paroll)
