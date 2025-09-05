import math 
from polysolve.solver import quadratic 

def quad(a, b, c, x):
  return 
  
 def test_roots():
   params = (3.0, 0.0, -1.0)
   roots = quadratic(params)
   
   assert all(math.isclose(quad(params, root), 0.0) for root in roots)
