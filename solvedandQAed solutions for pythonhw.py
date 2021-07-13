from decimal import Decimal

# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

# letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
# if type(letter) == type('str') and len(letter) == 1:

#   if letter in 'a e i o u':
#     print(f'The letter {letter} is a vowel uwu')
#   else:
#     print(f'The letter {letter} is a consonant uwu')
# else:
#   print(f"Are you sure that's {letter} IS LETTER? ):<")
# git commit -m "LGTM!!!"

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# phrase = ''
# while phrase != 'quit':
#   phrase = input('Please enter a word or phrase: ')
#   print(f'What you entered is {len(phrase)} characters long')
# LGTM!!!


# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
# try:

#   human_years = float(input("Input a dog's age in human years: "))

#   if human_years < 0:

#     print(f'{human_years} is less than 0, how2calculate):')

#   elif human_years < 3:  
 
#     dog_years = human_years * 10

#   elif human_years > 3 and human_years < 30:

#     dog_years = 20 + (human_years - 2) * 7
#     print(f"The dog's age in dog years is {dog_years}")

#   elif human_years >= 30:

#     print(f"C'mon you have a {human_years} years old dog? You can do the math yourself, first two years equals 10 each, after that each years equals 7. https://www.online-calculator.com/ glhf!")

# except ValueError:
#   print('if you want me to do math give me some numbers!')

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# try:
#   a = Decimal(input('Enter Side A: '))
#   b = Decimal(input('Enter Side B: '))
#   c = Decimal(input('Enter Side C: '))

#   if a == b == c:
#     print(f"A triangle with sides of {a}, {b} & {c} (All Equal) is a equalateral triangle!")
#   elif a != b != c:
#     print(f"A triangle with sides of {a}, {b} & {c} (All Unequal) is a scalene triangle!")
#   elif a == b or b == c or c == a:
#     print(f"A triangle with sides of {a}, {b} & {c} (Two Equal) is a isosceles triangle!")
#   else: 
#     print('Idk uwu')
# except ValueError:
#   print('give me numbers please uwu')


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

# try:
#   term = 0
#   a = 0
#   b = 1
#   fib = Decimal(input('Enter a number to calc fib to :D : '))
#   while term < fib:
#     if term < 2:
#       print(f'term: {term} / number: {term}')
#     else:
#       num = a + b
#       print(f'term: {term} / number: {num}')
#       a = b
#       b = num
#     term += 1
# except ValueError:
#   print(f"Bro you sure {fib} is a number?")    



# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.



# try:

#   mo = input('Enter the month of the season (Jan - Dec): ').lower()
#   day = int(input('Enter the day of the month: '))

#   if mo in ('jan', 'feb', 'mar'):
#     season = 'Winter'
#   elif mo in ('apr', 'may', 'jun'):
#     season = 'Spring'
#   elif mo in ('jul', 'aug', 'sep'):
#     season = 'Summer'
#   else:
#     season = 'Fall'
#   if mo == 'mar' and day > 19:
#     season = 'Spring'
#   elif mo == 'jun' and day > 20:
#     season = 'Summer'
#   elif mo == 'sep' and day > 21:
#     season = 'Fall'
#   elif mo == 'dec' and day > 20:
#     season = 'Winter'
#   print(f'{mo} {day} is in {season}')
# except ValueError:
#   print("please give me the correct input, month e.g. 'Jan' and day as e.g. '10'")
