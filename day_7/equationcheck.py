equations = {}
with open("equations.txt") as file:
    for line in file:
        #Remove the ":" and create dict
        data = line.strip().split()
        equations[int(data[0].replace(":",""))] = [int(data[x]) for x in range(1,len(data))]

class InvalidBranch(BaseException):
    pass

class ValidBranch(BaseException):
    pass

def value_check(test_value, current_value, extra_check: bool = False):
    # Test various conditions for current value to determine whether
    # a sum or product can be done to reach the test value

    # Check whether the current value can be multiplied by some
    # number to reach the test value
    if test_value < current_value:
        # Not operators will work, quit test
        valid_operators = None
        return valid_operators
    elif not test_value % current_value:
        # current value can fit into test value, can use sum or product
        valid_operators = ["+", "*"]
    else:
        valid_operators = ["+"]
    
    if extra_check:
        current_value_str = str(current_value)
        test_value_str = str(test_value)
        try:
            test_value_appended = test_value_str[len(test_value_str)-len(current_value_str):len(test_value_str)]
        except:
            return valid_operators
        if current_value_str == test_value_appended:
            valid_operators.append("||")
            print(valid_operators)
    return valid_operators

# Look at each dict value and test backwards for valid operations
def equation_check(test_value, numbers, extra_check: bool = False):
    # check an equation for validity
    # Loop through numbers see if there is a valid expression
    if len(numbers) > 1:
        valid_operators = value_check(test_value, numbers[-1],extra_check=extra_check)
    else:
        if test_value == numbers[0]:
            raise ValidBranch
        raise InvalidBranch


    if not valid_operators:
        raise InvalidBranch
    
    for operator in valid_operators:
        match operator:
            case "*":
                new_test_value = int(test_value/numbers[-1])
            case "+":
                new_test_value = int(test_value - numbers[-1])
            case "||":
                test_value_str = str(test_value)
                if len(test_value_str) == 1:
                    new_test_value = int(test_value_str)
                else:
                    new_test_value = int(test_value_str[0:len(test_value_str)-len(str(numbers[-1]))])

        new_numbers = [numbers[x] for x in range(0,len(numbers)-1)]
        print(f"Test Value: {new_test_value} - Numbers: {new_numbers}")
        try:
            equation_check(new_test_value, new_numbers, extra_check=extra_check)
        except InvalidBranch:
            #Bad branch, stop iterating somehow
            pass
        except ValidBranch:
            #Good branch found
            raise ValidBranch
    

valid_sum = 0
for equation in equations:
    try:
        equation_check(equation, equations[equation],extra_check=True)
    except InvalidBranch:
        pass
    except ValidBranch:
        valid_sum += equation
    print (valid_sum)


