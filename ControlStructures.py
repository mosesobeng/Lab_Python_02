theInput = input("Enter an integer: ")

if theInput%2 == 0:
    print 'even'
elif theInput%2 == 1:
    print 'odd'

print'-------------------------------------------------------------------------------/n'
    
primarySchAge =4
legalVotingAge=18
ageAsPresident=40
officialRetirmentAge=60

personsAge = input('Enger an age: ')


if personsAge<primarySchAge:
    print 'too young.'

elif personsAge>=legalVotingAge:
    print 'Remember to vote'
    if personsAge>=ageAsPresident:
        print 'Vote for me'
    elif personsAge<ageAsPresident:
        print 'You can’t be president'
elif personsAge>=officialRetirmentAge:
    print 'Too old.'


