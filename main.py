# Author: Eric Benditt erb5623@psu.edu
# Collaborator: Kaitlyn Byrnes krb5906@psu.edu
# Collaborator: Youhyun Kim yfk5109@psu.edu
# Collaborator: Adam Henderson ayh5125@psu.edu
# Section: 4
# Breakout: 8

def sum_n(n):
  if n <= 0:
    return n
  else:
    return n + sum_n(n-1)

def print_n(s, n):
  if n<=0:
    return
  else:
    print(s) 
    print_n(s, n-1) 

def run():
  n = int(input("Enter an int: "))
  print (f"sum is {sum_n(n)}.") 
  s = input("Enter a string: ")
  print_n(s, n) 

if __name__ == "__main__":
  run() 
