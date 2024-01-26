# #string concatenation (aka how to put strings together)
# #suppose we want to create a sting that says "subscribe to "
# youtuber = "i am kushal" #some string varibale

# # a few ways to do this 
# print ("subscribe to "+ youtuber)
# print ( "subscribe to {}".format (youtuber))
# print(f"subscribe to {youtuber}")

adj =input("adjective: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
famous_person = input("famous_person: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time beacuse \
I love {verb1}. stay hydrated and {verb2} Like you are {famous_person}!"

print(madlib) 