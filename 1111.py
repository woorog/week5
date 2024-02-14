import sys

tc=int(sys.stdin.readline())

for _ in range(tc):
    first=sys.stdin.readline().strip()
    first=list(first)
    trigger=0
    lens=int(sys.stdin.readline())
    a=sys.stdin.readline().strip()

    a = a[1:-1]



    if len(a)>0:
        word = [int(x) for x in a.split(',')]
    elif len(a)==1:
        word=a
    else:
        word=[]
    now='n'

    if lens != len(word):
        trigger=1

    for i in first:
        if i=='R' and now=='R':
            # word.reverse()
            now='n'
        elif i=='R' and now=='n':
            now='R'


        if i =='D':
            if len(word) != 0 and now=='R':
                del word[len(word)-1]
            elif len(word) != 0 and now=='n':
                del word[0]
            else:
                trigger=1
                break

    if trigger == 0 and now == 'n':
        print('[' + ','.join(map(str, word)) + ']')
    elif trigger == 0 and now == 'R':
        word.reverse()
        print('[' + ','.join(map(str, word)) + ']')
    else:
        print('error')

