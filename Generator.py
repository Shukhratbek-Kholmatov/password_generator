import random
upper_letters=list ("ABCDEFGHIJKLMNOPQRSTUVXYZ")
lower_letters=list("abcdefghijklmnopqrstuvxyz")
symbols=list("+-/*!$#?@=<>&")
print(f"Parol darajasini tanlang⬇️")
request=input("Murakkab(m)\nO'rta(o)\nSodda(s)\n>>>")
password_len=int(input("Parol uzunligini kiriting\n>>>"))
text=" "
if request=="m":
     while password_len>len(text):
                random.shuffle(upper_letters)
                random.shuffle(lower_letters)
                random.shuffle(symbols)
                choice1=random.choice(upper_letters)
                choice2=random.choice(lower_letters)
                choice3=random.randint(1,100)
                choice3=str(choice3)
                choice4=random.choice(symbols)
                text=text+choice1
                text=text+choice2
                text=text+choice3
                text=text+choice4
     print(f"{password_len} uzunlikdagi murakkab parol tayyor:\n{text}")
elif request=="o":
     while password_len>len(text):
                    random.shuffle(upper_letters)
                    random.shuffle(lower_letters)
                    choice1=random.choice(upper_letters)
                    choice2=random.choice(lower_letters)
                    text=text+choice1
                    text=text+choice2
     print(f"{password_len} uzunlikdagi o'rta darajadagi parol tayyor:\n{text}")
elif request=="s":
     a=" "
     b=" "
     while password_len>len(a) and len(b):
                    random.shuffle(upper_letters)
                    random.shuffle(lower_letters)
                    choice1=random.choice(upper_letters)
                    choice2=random.choice(lower_letters)
                    a=a+choice1
                    b=b+choice2
     print(f"{password_len-1} ta katta harfdan iborat sodda parol:\n1.{a}\n2.{a.lower()}\n{password_len-1} ta kichik harfdan iborat sodda parol:\n{b}")
else:
    print("Bunday kalit so'z yo'q")



