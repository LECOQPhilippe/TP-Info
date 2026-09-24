'''
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


moy= []

for student in classDict['class']['student']:
    moy.append(student['average'])

classDict['class']['average_grade'] = sum(moy)/len(moy) 



print(classDict)

'''



import random

def isAllUniq(collect):
    return len(set(collect)) == len(collect)

lst = []
lst_test = [1,1,2,3]
for i in range(random.randint(2,100)):
    lst.append(random.randint(0,500))

print(isAllUniq(lst_test))
print(isAllUniq(lst))

def Score(ops):
    pile = []
    for op in ops:
        if op == '+':
            if len(pile) > 1:
                pile.append(pile[-1] + pile[-2])
            else:
                pile.append(pile[-1])
        elif op == 'C':
            pile.pop()
        elif op == 'D':
            pile.append(2 * pile[-1])
        else:
            pile.append(int(op))

    return sum(pile)


print(Score(["10", "+", "2", "C", "D", "+"]))




