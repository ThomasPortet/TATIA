with open("examiner-date-text.csv", "r") as f:
    searchlines = f.readlines()[1:]

with open("cleanedSource.txt", "w") as o:
    for l in searchlines:
        lSplitted = l.split("\"")
        o.write(lSplitted[1]+"\n") 
        
