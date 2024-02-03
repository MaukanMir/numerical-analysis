import math

def check_function_output(a,p):
  
  return [
    a**3 + 2*a - 6,
    p**3 + 2*p - 6,
    ]
def bi_section_method(a,b, tolerance, limit):
  iterations =0

  while iterations <= limit:
    iterations +=1
    p = (a+b)/2.0
    fa,fp = check_function_output(a,p)
    
    print(f"p = {p}")
    print(f"f(p) = {fp}")
    print(f"f(a) = {fa}")
    print(f"a = {a}")
    
    if fp ==0 or (b-a)/ 2.0 < tolerance:
      print(f"The number of iterations: {iterations}")
      print(f"Current interval is [{a}, {b}]")
      return print("root is here : " + str(p))

    elif (fa <0 and fp>0 ) or (fa>0 and fp<0):
      b = p
      print("b change " + str(b))
    else:
      a = p
      
    print(f"Current interval is [{a}, {b}]")
    print(f"The number of iterations: {iterations}")
    print("---------------------------------------")
  
  return print(f"Does not converge within estimated iterations of: {iterations}")

bi_section_method(1,2, 10**-2, 20)