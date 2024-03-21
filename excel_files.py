import csv

with open("week23.csv", 'w') as f: 
    pen = csv.writer(f) # object to be use to write the file pen or curseur
    header = ["Name", "Cell Phone" , "City"]
    pen.writerow(header)
    pen.writerow(["denise", "860 665 5585" , "Suffield"]) #en.writerow(["Alix" "860 665 5585", "Suffield"])
    #pen.writerow(entry1)

f.close

