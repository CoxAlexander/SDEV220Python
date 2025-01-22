#Alexander Cox
#GPA.py
#Gets the students name and GPA and then says if they in Deans list or honor roll

DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
SENTINEL: str = "ZZZ"

last_name = input("Please enter student last name: (ZZZ to quit)")
while (last_name != SENTINEL):
    first_name = input("Please enter student first name: ")
    GPA = input("Please enter the student GPA")
    
    if (GPA >= DEANS_LIST):
        print(f"{first_name} {last_name} has made the Dean's List")
    elif (GPA >= HONOR_ROLL):
        print(f"{first_name} {last_name} has made Honor Roll")
    last_name = input("Please enter student last name: (ZZZ to quit)")
        