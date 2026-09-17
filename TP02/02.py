import copy

a = ['A']
b = a 
b[0] = 1


classDict = {
    "class": {
         "student": {
             "name": "Mike",
                 "marks": {
                     "physics": 70,
                         "history": 80
             }
         }
     }
}


#1
print(classDict["class"]["student"]["name"])

#2
classDict["class"]["student"]["marks"]["physics"] = 89
print(classDict["class"]["student"]["marks"]["physics"])

#3
average = sum(classDict["class"]["student"]["marks"].values())/len(classDict["class"]["student"]["marks"])
print("La note average est de : ",average,".")



classDict["class"]["student"] = [{
             "name": "Mike",
                 "marks": {
                     "physics": 70,
                         "history": 80
             }
         }]


classDict["class"]["student"].append({
    "name": "Ted",
    "marks": {
        "physics": 34,
        "history": 99
    }
})

print(classDict["class"]["student"])













