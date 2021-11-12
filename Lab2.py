import csv
file=open('lab2.csv')
data = list(csv.reader(file))[1:]
concept=[]
target=[]
for i in data:
    concept.append(i[:-1])
    target.append(i[-1])
specific_h=['0']*len(concept[0])
general_h=[['?'for i in range (len(specific_h))] for i in range (len(specific_h))]
for i,instance in enumerate(concept):
    if target[i]=="Yes":
        for x in range (len(specific_h)):
            if specific_h[x]=='0':
                specific_h[x]=instance[x]
            elif instance [x]!= specific_h[x]:
                specific_h[x]='?'
                general_h[x][x]="?"
    if target [i] == "No":
        for x in range (len(specific_h)):
            if instance[x]!=specific_h[x]:
                general_h[x][x]=specific_h[x]
            else :
                general_h[x][x]='?'
indice =[i for i,val in enumerate(general_h)if val==['?','?','?','?','?','?']]
for i in indice:
    general_h.remove(['?','?','?','?','?','?'])
print("final specific:",specific_h)
print("final general:",general_h)
