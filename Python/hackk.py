if __name__ == '__main__':
    full_record = []    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        full_record.extend([[name,score]])
    i = 0
    lowest = min(full_record, key=lambda x: x[1])
    possibleLsecond = [x for x in full_record if x[1] != lowest[1]]
    print(possibleLsecond)
    lastSecond = []
    while i < len(possibleLsecond):
        if possibleLsecond[i][1] == min(possibleLsecond, key=lambda x: x[1])[1]:
            lastSecond.append(possibleLsecond[i])
        i+=1    
    for name in sorted(lastSecond):
        print(name[0])    
