def computegrade(score):
    try:
        if score > 1:
            score = 'NA'
        elif score < 0:
            score = 'NA'
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        elif score < 0.6:
            print('F')
    except:
        print('Bad score')