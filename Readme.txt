Challenge:
Imagine that every year your extended family does a &quot;Secret Santa's; gift exchange. For this gift
exchange, each person draws another person at random and then gets a gift for them. Write a
program that will choose a Secret Santa for everyone given a list of all the members of your
extended family. Obviously, a person cannot be their own Secret Santa.
After the third year of having the Secret Santa gift exchange, you’ve heard complaints of having
the same Secret Santa year after year. Modify your program so that a family member can only
have the same Secret Santa once every 3 years.


Solution:

I have used python dictionary to store previous year result of secret santa 
and then loop through this all the family members to assign secret santa.

For the first outer loop : every is elegible santa except them person himslef or if the person has give the gift to same person in past 2 years.
Eacg iteration of the loop will assign the eligible santa to the receiver.

For storing the mertdata and output ,for now i have used text file , but it can be chanaged to db connection or hdfs in future



Time complexity of the program in worst case is :  O(n) 


