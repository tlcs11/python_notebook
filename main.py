from datetime import date

"""
Note Book app


Notes will have three parts an 
ID
Content
Date/Time
"""
notebook = []

counter = 1
note_id = counter

counter += 1

now = date.today()

content = "This is content"

note = (note_id, now, content)

notebook.append(note)
print(notebook)


