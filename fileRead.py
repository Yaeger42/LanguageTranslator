#Vars
tagList = []
instructionList = []
commentList = []
opList = []
f = open('text.txt', 'r')
x = f.read()
listofLines = x.split(" ")

for i in range(0, len(listofLines)):
    if listofLines[i].endswith(":\n") and not listofLines[i].startswith(";"):
        tagList.append(listofLines[i])

    elif listofLines[i].startswith(";"):
        commentList.append(listofLines[i])

    elif listofLines[i+1] is not None  and  (listofLines[i-1].endswith('\n')  or   listofLines[i] == listofLines[0]) or listofLines[i-1] == '':
        if listofLines[i] == '':
            pass
        else:
            instructionList.append(listofLines[i])

    elif listofLines[i-1] is not None and listofLines[i].endswith('\n') or listofLines[i+1].startswith(';'):
        opList.append(listofLines[i])
f.close()
print(f'Tag: {tagList}')
print(f'instructions: {instructionList}')
print(f'comments: {commentList}')
print(f'Operator: {opList}')
wr = open('new.txt', 'w')
for t in tagList:
    if t:
        wr.write(f'Tags: {t} \n')
    else:
        wr.write("Tags: \n")

for i in instructionList:
    if i:
        wr.write("Mnemonic: " +i+'\n')
    else:
        wr.write("Mnemonic: \n")

for o in opList:
    if o:
        wr.write(f'Values: {o} \n')
    else:
        wr.write("Values: \n")

for c in commentList:
    if c:
        wr.write(f'Comments: {c}\n')
    else:
        wr.write("Comments: \n")

wr.close()