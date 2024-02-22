def add_note(notebook):
    note_dict={}
    title=input("title bede!")
    note=input("note bede!")
    note_dict["title"]=title
    note_dict["note"]=note
    notebook.append(note_dict)
    return notebook



notebook=[]
while True:
    x=input("""what do you want
            0 for add note
            1 for end""")
    if x==0:
        notebook=add_note(notebook)
    elif x==1:
        break