print("Hele uren van de dag")
for i in range(0,26):
    if i % 2 == 0:
        if i in range(0,14):
            print(str(i) + " AM")
        if i in range(12,26):
            print(str(i) + " PM")
print("terug tellen van 20 tot 50 en allen even nummer printen")
for x in range(20,51):
    if x % 2 == 0:
        print(x)
print("terug tellen van 30")
for y in range(30, -1, -1):
    print(y)
       
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


day = input("kies een dag: ")
d = 1
while d < 2:
    print("Ma")
    print("Di")
    print("Wo")
    print("Do")
    print("Vr")
    print("Sa")
    print("Zo")
if input("Ma"):
    d = d + 1
if input("Di"):
    d = d + 1
if input("Wo"):
    d = d + 1
if input("Do"):
    d = d + 1
if input("Vr"):
    d = d + 1
if input("Sa"):
    d = d + 1
if input("Zo"):
    d = d + 1 
