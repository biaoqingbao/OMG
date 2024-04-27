with open("dow.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    dowgro = f.readlines()

with open('dow.gro', "w") as f:
    # newdow=[]
    for i in dowgro:
        new = i.replace("MOL", "DOW")
        f.write(new)


with open("upp.gro", "r") as f:
    # Read the contents of the second text file into a list of lines
    dowgro = f.readlines()

with open('upp.gro', "w") as f:
    # newdow=[]
    for i in dowgro:
        new = i.replace("MOL", "UPP")
        f.write(new)


with open("dow.itp", "r") as f:
    # Read the contents of the second text file into a list of lines
    dowgro = f.readlines()

with open('dow.itp', "w") as f:
    # newdow=[]
    for i in dowgro:
        new = i.replace("MOL", "DOW")
        f.write(new)


with open("upp.itp", "r") as f:
    # Read the contents of the second text file into a list of lines
    dowgro = f.readlines()

with open('upp.itp', "w") as f:
    # newdow=[]
    for i in dowgro:
        new = i.replace("MOL", "UPP")
        f.write(new)
