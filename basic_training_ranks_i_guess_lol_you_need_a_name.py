import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
print("Select branch:")
print("1. Army")
print("2. Marine Corps")
print("3. Air Force")
print("4. Navy")
print("5. Coast Guard")
try:
    B = int(input("Enter number (1-5): "))
except ValueError:
    print("Invalid selection")
    exit()
if B < 1 or B > 5:
    print("Invalid selection")
    exit()
if B == 1 or B == 2:
    R = "Private (E-1)"
elif B == 3:
    R = "Airman Basic (E-1)"
elif B == 4 or B == 5:
    R = "Seaman Recruit (E-1)"
print("In Basic Training, your rank is " + R)