def fect_rec(n):
  if n==0 or n==1:
     return 1
  else:
      return n*fect_rec(n-1)
    
  number = 2
  res = fect_rec(number)
  
  print("The factorial of  {} is{}".format (number,res));