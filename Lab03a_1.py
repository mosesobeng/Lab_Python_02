userInput = int(raw_input('Enter phone number:      '))
print ''
tempVar = 0
i = 0
number=userInput

while number >= 10:
    number = number/10
    i += 1

number = userInput

while number >= 10:
  tempVar = tempVar + (number%10)*10**i
  
  number = number/10
  i -= 1

else:
      number = tempVar + number
      print 'The Encrypted number is',          number
