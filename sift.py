with open('100.txt') as f, open('words7.txt', 'w') as f2:
    for line in f:
        for word in line.split('\n'):    #split the line at whitespaces
            if len(word) >= 7 and len(word) <= 15:       #if len(word) is 2 then write it to file
                f2.write(word + '\n')
