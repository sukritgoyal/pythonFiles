def maximumSum(a, m):
    maxMod = [sum(a)%m]
    [maxMod.append(x%m) for x in a if x%m not in maxMod]
    for i in range(2,len(a)):
        for j in range(0,len(a)-i+1):
            arr = []
            for k in range(0,i):
                arr.append(a[j+k])
            maxMod.append(sum(arr)%m)
    return max(maxMod)
