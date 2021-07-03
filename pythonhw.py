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

#P1
# x = input('Enter a letter to check for vowel or consonant: ').lower()

# if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
#   print(x, "it's a vowel!")
# else:
#   print(x, "it's a consonant!")
#Done!

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

#P2

# x = input('Sentence Char Length Checker: ')

# if x == 'quit':
#   print('bye!')
#   quit()

# print(len(x))

# Done

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

# var1 = 10
# var2 = 20
# var3 = 27
# var4 = 34
# var5 = 41
# var6 = 48

# print(var1/2)
# print(var2/2)
# print(var3/2)
# print(var4/2)
# print(var5/2)
# print(var6/2)

# x = input('doggie age: ')
# y = ''

# if float(x) == 0:
#   print('your doggie is a newborn!')
# elif float(x) <= 2:
#   print((float(x)/10) * 100, 'years old') 
# elif float(x) > 2:
#   y = 20 + (float(x) -2) * 7
#   print(y)

#Done
