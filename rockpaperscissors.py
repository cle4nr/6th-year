
def rollrps(userchoice):
    import random as r
    rps = ['rock','paper','scissors']
    npcchoice = r.choice(rps)
    print(f'npc chose {npcchoice}')
    if userchoice == npcchoice:
        print('draw')
    elif userchoice == rps[0]:
        if npcchoice == rps[2]:
            print('win')
        else:
            print('lose')
    elif userchoice == rps[1]:
        if npcchoice == rps[0]:
            print('win')
        else:
            print('lose')
    elif userchoice == rps[2]:
        if npcchoice == rps[1]:
            print('win')
        else:
            print('lose')
            
rps = ['rock','paper','scissors']
urchoice = input('enter rps: ')
if urchoice == 'r':
    print(f'you chose {rps[0]}')
    rollrps(rps[0])
elif urchoice == 'p':
    print(f'you chose {rps[1]}')
    rollrps(rps[1])
elif urchoice == 's':
    print(f'you chose {rps[2]}')
    rollrps(rps[2])
else: print('only rps valid')