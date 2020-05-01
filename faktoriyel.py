#bunuda internetten buldum kfhskdhfsd
num = int(input("faktroriyelini almak istediginiz sayiyi girin:"))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)




#OMER ABIMIN YONTEMI nasill yontemmis be beynim curudu (kendi yontemimlede yapamadim sakjhdfkjshfjkh)
'''
def factorial(n):
    if(n == 1): return  1
    return n * factorial(n - 1)


test = factorial(3)
print(test);
'''