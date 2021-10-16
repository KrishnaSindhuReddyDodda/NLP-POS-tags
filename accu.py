def accuracy(gold,output):
    correct=0
    total=0
    assert(len(gold) == len(output))
    for i in range(len(gold)):
        assert(len(gold[i])) == (len(output[i]))
        total = total + (len(gold[i]))
        for j in range(len(gold[i])):
            if gold[i][j] == output[i][j]:
                correct=correct+1
    print("ACCURACY:", (correct*100)/total,"%")
                
