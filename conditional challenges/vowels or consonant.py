# in english litrature vowels are: a , e , i , o , u and consonants are except vowels
letter = input("Enter the Letter: ")

if( letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" ):
    print("Vowels ")
else:
    print("Consonants")




#Every student must score greater than 45 to pass  , max marks are 100
# if not score then student is failed  in every subject

math = int(input("Enter the Math marks : "))
physics = int(input("Enter the Physics marks : "))
chemistry = int(input("Enter the Chemistry marks : "))

if (math >=45 and physics >= 45 and chemistry >= 45):
    print("You Passed the Exam ")
else:
    print("You Failed the Exam ")
