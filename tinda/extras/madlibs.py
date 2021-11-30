# string concatenation = putting strings together
# string interpolation = putting variables into strings

# for example:
variable_one = "Mango"
variable_two = "Orange"
string_one = f"I like to eat {variable_one} and {variable_two}."
# print(string_one)


# older ways of doing it:
string_two = "I like to eat " + variable_one + " and " + variable_two + "."
string_three = "I like to eat %s and %s." % (variable_one, variable_two)
string_four = "I like to eat {} and {}.".format(variable_one, variable_two)

# print(string_two)
# print(string_three)
# print(string_four)
# print("All of the strings are essentially doing the same thing, just written in a diffrent way.")

adjective_one = input("Enter an adjective: ")
adjective_two = input("Enter another adjective: ")
verb_one = input("Enter a verb: ")
verb_two = input("Enter another verb: ")
famous_person = input("Enter a famous person: ")

mablib = f"Computer programming is so {adjective_one}! It makes me so {adjective_two} all the time because, \
I love to {verb_one}. Stay hydated and {verb_two} like you are {famous_person}!"


print(mablib)
