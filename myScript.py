myList = [];
with open("./Data/w59Test.har" , 'r') as f:
        for line in f:
            if 'otherplayergroupname' in line:
                with open('Data/output', 'a') as file:
                    file.write(line)
