theInput = input("Enter an integer: ")

if theInput%2 == 0:
    print 'even'
elif theInput%2 == 1:
    print 'odd'

print'-------------------------------------------------------------------------------'
    
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
    
print'-------------------------------------------------------------------------------'
  

for number in range(40,-1,-1):
    if number%3==0:
        print number


print'-------------------------------------------------------------------------------'
  
for number in range (6,31):	
  
    if number%2!=0 and number%3!=0 and number%5!=0:	
  
        print number

print'-------------------------------------------------------------------------------'
 
number=1	
  
while(79*number)%97!=1:	
    number=number+1	
  
    print number	
  


 

