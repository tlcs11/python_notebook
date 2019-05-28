from datetime import date

"""
Note Book app


Notes will have three parts an 
ID
Content
Date/Time
"""
counter = 1
notebook = []
now = date.today()

while True:
    user_response = input ("What would you like to do? \n"
                            "1. Add a note\n"
                            "2. Print a note\n"
                            "3. Exit\n>")
    if user_response == "1":
        content = input("What is the note \n> ")
        note_id = counter
        note = (note_id, str(now), content)
        notebook.append(note)
        counter += 1
    elif user_response == "2":
        for note in notebook:
            print(f"Id: {note[0]}| {note[2]}")
    elif user_response == "3":
        exit()  
    else:
        print("Invalid input")    

# print(notebook)
# user_response = input ("Would you like to make a note? \n Y, N >").lower()
# if user_response == "y":


# while counter <= 5:
#     content = input("What is the note \n> ")
#     note_id = counter
#     note = (note_id, str(now), content)
#     notebook.append(note)
#     counter += 1
#     print(notebook)

