# sum-of-num
num=raw_input("enter the num:")
if num<0:
   print("enter positive num")
else:
   sum=0
   while(num>0):
      sum+=num
      num-=1
      print("the sum is",sum)
