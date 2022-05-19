# Test corrections number 2

## Conditional inside of a loop 

This question displays the following code segment 

index <-- 1

sum <-- 0

REPEAT UNTIL (index > 10)

{

  if (index MOD 3 = 0)

 {    

   sum <-- sum + index

  ]   

  index <-- index + 2
]

DISPLAY sum 

This question falls under the Algorithms and Programing section

The answers to this promblem were 

3

9

12

55

I answered that after the code segment is excuted it would return 3 this is incorrect because index starts at 1 and the condition is that we add 2 to index every time it's not greater than 10. since the index adds up by 2 this proccess will be repeated 5 times nd index will become 11. Now since the condition has been met we move onto to the next thing 

if (index MOD 3 = 0)

this checks if any of the numbers in index were a multiple of 3. 3 and 9 are the only multiples so this condition becomes true after that we move down to 

sum <-- sum + index 

now we add both 3 and 9 to sum which is equal to zero so we get 12 which is the correct answer. 

as to no get this wrong again ill make sure to pay closer attention to what the problem is asking and to the code being displayed. and ill make sure to study more.

## Sum of Dice

This question falls under the Algorithms and programming section

The following code segment is displayed 

a <-- RANDOM(1,6)

b <-- RANDOM(1,6)

return(a + b)

This question asks how many times a sum of 7 is rolled when 2 die are rolled a 100 times 

The correct answer is 

numSevens <-- 0

REPEAT 100 times 

{
   sum <-- sumOfTwoDice()
   IF(sum = 7)
   {
      numSevens <-- numSevens + 1
   ]
]
DISPLAY(numSevens)

This is correct because the code segment checks if the sum of the 2 dice is equal to seven 

IF(sum = 7)

and if that condition is true then it adds 1 to numSevens 

ill make sure to not get this question or any like it wrong again by studying and making sure i understand conditionls and loops 

## Increased Bandwidth 

This question falls under the Computer Systems and Networks section

This question asks 

A busniess recently had its network bandwidth increased from 80 megabytes per second to 100 megabytes per second 

which of the folloing will change 

the correct answer is 

The transfer of files between computer in the network will generally occur at a faster rate than before.

This answer makes sense because the larger the bandwidth the more info that can be sent That can be sent at a time.

I said that the maxium file size that can be sent between computers has increased from 80 megabytes to 100 megabytes.

that answer doesnt make sense because computers regulary send big files in smaller packets between each other so there is vitually no file size limit.

to avoid getting this question and others like it wrong again ill make sure to pay closer attention to what it is asking me and study.
