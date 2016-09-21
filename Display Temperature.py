def menu():
    print("\n1. Celsius to Farenheit")
    print("\n2. Farenheit to Celsius")  
    pick = int(input("Enter a choice: "))
    return (pick)
menu()

for c in range(0,101,5):
     print("Celsius = {}".format(c))
for f in range(0,101,5):
     print("Farenheit = {}".format(f))
def main():
    choice = menu()
    if choice == 1:
            #to convert from C to F
            c = eval(input("Enter degrees Celsius: "))
            print(str(toFarenheit(c)))
    if choice == 2:
          f = eval(input("Enter degrees Celsius: "))
          print(str(toCelsius(f)))
          print(" ")
          
    else:
            print("invalid entry")
            choice = menu ()







