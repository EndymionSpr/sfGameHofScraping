emptySth = '/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0'
with open("./Data/output" , 'r') as f:
        for line in f:
            if emptySth in line:
                level = line.split('/')[2]
                with open('output', 'a') as file:
                    file.write("Level: " + level)
                
                indStart = line.index('otherplayername.r')
                indEnd = line.index('&otherplayerunitlevel')
                name = line[(indStart+18):indEnd]

                with open('output', 'a') as file:
                    file.write(" | Name: " + name + '\n')
