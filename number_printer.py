def say(max_number):
    for i in range(1, max_number +1):
        print(i)

while True:
    num = input("Kaça Kadar Symak İstersin?\nÇıkmak İçin q'ya Bas:\n")

    if num.lower() == "q":
     print("Program Kapatıldı.")
     break

    if num.isdigit():
       say(int(num))
    else:
       print("Lütfen Bir Sayı Gir!")   