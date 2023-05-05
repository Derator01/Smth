input = '0'+ '1'

firstNumber = '01'
secondNumber = '02'
thirdNumber = '03'

while (firstNumber in input) or (secondNumber in input) or (thirdNumber in input):
    input = input.replace('11', '1',1)
    
    if '21' in input:
        input = input.replace(firstNumber, '30',1)
    elif secondNumber in input:
        input = input.replace(secondNumber, '101',1)
    else:
        input = input.replace(thirdNumber, '202',1)
print(input)

#12