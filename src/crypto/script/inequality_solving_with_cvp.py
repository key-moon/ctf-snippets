# HEADER
# name: Inequality Solving with CVP
# prefix: ["rkm", "inequality-solving-with-cvp"]
# description: https://github.com/rkm0959/Inequality_Solving_with_CVP
# author: rkm0959

# BODY
from sage.modules.free_module_integer import IntegerLattice

def Babai_CVP(mat, target):
  M = IntegerLattice(mat, lll_reduce=False).LL()
  # M = IntegerLattice(mat, lll_reduce=False).BKZ(block_size=10)
  G = M.gram_schmidt()[0]
  diff = target
  for i in reversed(range(G.nrows())):
    diff -=  M[i] * ((diff * G[i]) / (G[i] * G[i])).round()
  return target - diff

def solve(M, lbounds, ubounds, weight = None, super_weight=None):
  mat, lb, ub = copy(M), copy(lbounds), copy(ubounds)
  num_var  = mat.nrows()
  num_ineq = mat.ncols()

  if weight == None:
    max_element = 0 
    for i in range(num_var):
      for j in range(num_ineq):
        max_element = max(max_element, abs(mat[i, j]))
    weight = num_ineq * max_element

    # sanity checker
  if len(lb) != num_ineq:
    print("Fail: len(lb) != num_ineq")
    return

  if len(ub) != num_ineq:
    print("Fail: len(ub) != num_ineq")
    return

  for i in range(num_ineq):
    if lb[i] > ub[i]:
      print("Fail: lb[i] > ub[i] at index", i)
      return

  # scaling process begins
  max_diff = max([ub[i] - lb[i] for i in range(num_ineq)])
  applied_weights = []

  for i in range(num_ineq):
    ineq_weight = (weight if lb[i] == ub[i] else max_diff // (ub[i] - lb[i]))
    applied_weights.append(ineq_weight)
    for j in range(num_var):
      mat[j, i] *= ineq_weight
    lb[i] *= ineq_weight
    ub[i] *= ineq_weight

  # Solve CVP
  target = vector(ZZ, [(lb[i] + ub[i]) // 2 for i in range(num_ineq)])
  result = Babai_CVP(mat, target)

  for i in range(num_ineq):
    if (lb[i] <= result[i] <= ub[i]) == False:
      print("Fail: inequality does not hold after solving")
      break
    
  # recover x
  fin = None

  if num_var == num_ineq:
    mat = mat.transpose()
    fin = mat.solve_right(result)
  
  ## recover your result
  return result, applied_weights, fin
