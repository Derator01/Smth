input = '1'*204

firstNumber = '111'
secondNumber = '222'
thirdNumber = '8883'

while (firstNumber in input) or (secondNumber in input) or (thirdNumber in input):
    if firstNumber in input:
        input = input.replace(firstNumber, '22',1)
    else: #secondNumber in input:
        input = input.replace(secondNumber, '1',1)
    #else:
    #    input = input.replace(thirdNumber, '1',1)
print(input)