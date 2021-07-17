'''

'Merge nested if statements'

#Typical style
if a:
    if b:
        print(True)

#After refactoring
if a and b:
    print(True)

------------------------------------

'Use  any instead of for loop'

#Typical style
numbers = [-1,-2,-3,-4,0,10]
has_positives = False
for n in numbers:
    if n > 0:
        has_positives = True
        break


#After refactoring
numbers = [-1,-2,-3,-4,0,10]
has_positives = any(n>0 for n in numbers)

------------------------------------

'Use variables that are not going to change out of the function as global variables'

#Typical style
buildings = ['Big Ben','Cambridge',River Thames']
addresses = []
for building in buildings:
    city = 'London'
    addresses.append([building,city])

#After refactoring
buildings = ['Big Ben','Cambridge',River Thames']
addresses = []
city = 'London'
for building in buildings:
    addresses.append([building,city])

------------------------------------

'Inline variable that is used only once'

#Typical style
def state_attributes(self):
    state_attr ={
            ATTR_CODE_FORMAT : self.code_format,
            ATTR_CHANGED_BY : self.changed_by
            }
    return state_attr

#After refactoring
def state_attributes(self):
    return  {
            ATTR_CODE_FORMAT : self.code_format,
            ATTR_CHANGED_BY : self.changed_by
            }

------------------------------------

'Replace is statement with if expression'

#Typical style
if condition:
    x = 1
else:
    x = 2

#After refactoring
x = 1 if condition else 2

------------------------------------

'Replace gaurd clause (Rather than executing a big if condition and failing somewhere, we try to run the reverse condition to avoid running through a big chunk of code)

#Typical style
def func(self,hat):
    if isinstance(hat,Hat):
        current_fashion = get_fashion()
        weather_outside = self.look_out_of_window()
        is_stylish = self.evaluate_style(hat,current_fashion)
        if weather_outside.is_raining:
            print('Damm.')
            return True
        else:
            print('Great.')
            return is_stylish
    else:
        return False

#After refactoring
def func(self,hat):
    if not isinstance(hat,Hat):
        return False
    current_fashion = get_fashion()
    weather_outside = self.look_out_of_window()
    is_stylish = self.evaluate_style(hat,current_fashion)
    if weather_outside.is_raining:
        print('Damm.')
        return True
    else:
        print('Great.')
        return is_stylish

------------------------------------

'Move assignments closer to their usage'

#Typical style
def func(self,hat):
    if not isinstance(hat,Hat):
        return False
    current_fashion = get_fashion()
    weather_outside = self.look_out_of_window()
    is_stylish = self.evaluate_style(hat,current_fashion)
    if weather_outside.is_raining:
        print('Damm.')
        return True
    else:
        print('Great.')
        return is_stylish

#After refactoring
def func(self,hat):
    if not isinstance(hat,Hat):
        return False
    current_fashion = get_fashion()
    if weather_outside.is_raining:
        print('Damm.')
        return True
    else:
        print('Great.')
        weather_outside = self.look_out_of_window()
        return self.evaluate_style(hat,current_fashion)

------------------------------------

'Simply sentence comparision'

#Typical style
nums = [1,2,3,4,5]
if len(nums)>0:
    print(True)


#After refactoring
nums = [1,2,3,4,5]
if len(nums):
    print(True)

'''

