
for x in range(10) :

  from random import randint
  
  num1 = randint(1,10)
  num2 = randint(1,10)

  question = "What is " + str(num1) + " times " + str(num2) +"? "
  user_answer = int(input(question))
  correct_answer = num1 * num2

  if user_answer == correct_answer:
    print("thats right - well done.")
  else:
    print("No, I'm afraid that answer is " + str(correct_answer) + ".")

