import math

L = 10
r =1
V = 11.5

def volume_of_water(h):
    # This is the given volume formula for water in a semicircular trough
    return L * ((0.5 * math.pi * (r**2) )- (r**2 * math.asin(h/r)) - (h * ((r**2) - (h**2))**0.5))

def check_function_output(a,p):
  
  return [
    volume_of_water(a) - V,
    volume_of_water(p) - V
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
      print(f"The depth of the water is: {1}-{p}")
      print(f"The number of iterations: {iterations}")
      return "root is here : " + str(p)
    elif (fa <0 and fp>0 ) or (fa>0 and fp<0):
      b = p
      print("b change " + str(b))
    else:
      a = p
      
    print(f"Current interval is [{a}, {b}]")
    print(f"The number of iterations: {iterations}")
    print("---------------------------------------")
  
  return f"Does not converge within estimated iterations of: {iterations}"

bi_section_method(0,r, 10**-2,20)

