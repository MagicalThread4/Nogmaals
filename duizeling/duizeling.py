print("Hele uren van de dag")
v = 0
while v < 1:
    for i in range(0,26):
        if i % 2 == 0:
            if i in range(0,14):
                print(str(i) + " AM")
            if i in range(12,26):
                print(str(i) + " PM")
                v += 1

print("terug tellen van 20 tot 50 en allen even nummer printen")
n =  0
while n < 1:
    for x in range(20,51):
        if x % 2 == 0:
            print(x)
            n += 1

print("terug tellen van 30")
b = 0
while b < 1:
    for y in range(30, -1, -1):
        print(y)
        b += 1
  
print("Tel de cijfers vanaf 50 en doe ze plus elkaar")
count = 50
while count <= 2000:
    print(count)
    count += count

print("Herhaal een input tot het resultaat daarvan gelijk is aan quit ")
required_word = 'quit'
while True:
    number = input("Enter the word\n")
    if number == required_word:
        print ("GOT IT")
        break
    else:
        print ("Wrong word try again")

print("Vraag een dag van de week op ")
dagen = input("kies een dag: ")
z = 0
while z < 1:
    if dagen == "Ma":
        print("Ma ")
        z += 1
    if dagen == "Di":
        print("Ma ")
        print("Di ")
        z += 1
    if dagen == "Wo":
        print("Ma ")
        print("Di ")
        print("Wo ")
        z += 1
    if dagen == "Do":
        print("Ma ")
        print("Di ")
        print("Wo ")
        print("Do ")
        z += 1
    if dagen == "Vr":
        print("Ma ")
        print("Di ")
        print("Wo ")
        print("Do ")
        print("Vr ")
        z += 1
    if dagen == "Za":
        print("Ma ")
        print("Di ")
        print("Wo ")
        print("Do ")
        print("Vr ")
        print("Za ")
        z += 1
    if dagen == "Zo":
        print("Zo ")
        print("Ma ")
        print("Di ")
        print("Wo ")
        print("Do ")
        print("Vr ")
        print("Za ")
        z += 1