emptySth = '/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0'
listLines = []
setLines = set()


with open("./data.har" , 'r' , encoding="UTF8") as f:
    for line in f:
        if 'otherplayergroupname' in line:
            if emptySth in line:

                level = line.split('/')[2]
                indStart = line.index('otherplayername.r')
                indEnd = line.index('&otherplayerunitlevel')
                name = line[(indStart+18):indEnd]
                listLines.append("Level: " + level + " | Name: " + name + '\n')
setLines = [*set(listLines)]

listLines = [*list(setLines)]
listLines.sort(key = lambda x: int(x.split(' ')[1]), reverse=True)

for line in listLines:
    with open('output', 'a') as file:
        file.write(line)

