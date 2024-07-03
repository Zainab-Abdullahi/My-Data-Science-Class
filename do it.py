LGAs = ['ilorin west', 'ekiti', 'oke-ero', 'ifelodun', 'barutee', 'asa', 'ilorin south', 'kaima', 'saare']
# LGA in the even position
length = len (LGAs)

def double(x):
    print(x*2)

# for i in range (1,length,2):
#     print(LGAs[i])

# for i in range(length):
#     if i % 2 == 1:
#         print(LGAs[i])
# print("the odd positions")
# for i in range(length):
#     if i % 2 == 0:
#         print(LGAs[i])
# print("first")
# for i in range (0,length,2):
#     print(LGAs[i])
# PRINTS ALL THE LGAs THAT STARTS WITH VOWEL

# vowels = 'aeiou'

# for i in range (length):
#     if LGAs[i][0] in vowels:
#         print(LGAs[i])
# print("second method")
# for lg in LGAs:
#     if lg[0] in vowels:
#         print(lg)

# def double(x):
#     print(x*2)

# double(5)
# double(100)    
# double(9)

# def greeting ():
#     print('good morning zaynab')
# greeting()                                                        

# def greeting(country, name='user'):
#     print('good morning' , name, ',how is', country)
#     print('good morning ' + name + ', how is ' + country)
#     print(f'good morning {name}, how is {country}')
#     return 'we are done'

# def power2():
# a = greeting('USA')
# print()
# print(greeting('Canada', 'Tosin'))
# print()
# a = greeting('Korea', 'Kabira')

# print('this is the result of greeting user:', a)



# greeting('USA', 'Zaynab')     
                                                   
# def power(number,index):
#     print(number**index)
# power(3,5) 
# print()
# def power(number,power):
#     print(number**power)  
# power(2,9)     
# print()
# var1= 2
# var2= 5

# power(var1, var2)
# print()
# power(4, 3)
# print()

# def Total_Price(items,tax_percentage):
#     total = items + (items * tax_percentage/100)
#     print(total)  
#     return(total)
# Total_Price(1000, 15)
# print()
# Ans=Total_Price(1000, 15)
# print(Ans)
# print(Ans + 2500)
# print(Ans * 0.9)
# print('second one')

# def pluraliseItems(itemsList):
#     for item in itemsList:
#         if item[-1] == 'e' and item[-2] == 'f':
#             print(item[0:-2]+ 'ves')
#         else:



# amount = '20,000'
# amount = amount.split(',')
# print(amount)
# amount = ''.join(amount)
# print(amount)
# val = int(amount)
# print()
# print(val/2)
# print()

# def age(birth_year,discurrent_year):
#     years = discurrent_year - birth_year
#     print(years)
#     return(years)

# age(2017, 2024)
# print(f"My child's age is {years}")

# write a function that adds it argument to the end of a list
# def add_to_list(lst, element):
#     lst.append(element)
#     return(lst)

# my_list = [2,3,4]
# new_number = 5
# new_version = add_to_list(my_list, new_number)
# print(new_version)

# print()

# #write a f (x) to change the first element of your list to ABU

# def change_the_first_element(lsts):
#     if lsts:
#         lsts[0] = "ABU"
#         return(lsts)
    
# my_list = ["cat", "dog", "fish", "hat"]
# new_list = change_the_first_element(my_list) 
# print(new_list)   
 


# def add_weights(weights):
#     total = 1
#     for weight in weights:
#         strVal = weights.strip('kg')
#         numVal = int(strVal)
#         total = total + numVal
#     return total
     
# goods = ['200kg', '500kg', '700kg'] 
# ans = add_weights(goods)
# print(ans)
# print('average is:', ans/3)
# print(f'average is: {ans/3}')

def add_number(number):
    total = 0
    for number in number:
        total = total + number
    return total 
   
values = [3,4,5,6,7,8]
ans = add_number(values)
print(ans) 
print('average is:', ans/6)   
print(f'The average is {ans/6}')



