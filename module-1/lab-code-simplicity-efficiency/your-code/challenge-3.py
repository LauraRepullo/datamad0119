def my_function(X): 
  solutions = []
  solutions = [[x,y,z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if (x*x==y*y+z*z)]
  m = 0
  for solution in solutions:
 m = 0
for solution in solutions:
  if m < max(solution):
      m = max(solution)
  return m

X = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(my_function(int(X))))
