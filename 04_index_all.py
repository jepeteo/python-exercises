def index_all(tValue, tList) :
  indices = []

  for i, value in enumerate(tList):
    if isinstance(value, list):
      # Recursive call for sublists
      sub_indices = index_all(tValue, value)
      for sub_index in sub_indices:
          indices.append([i] + sub_index)
    else:
        if value == tValue:
          indices.append([i])
  return indices
  

tExample = [[[1,2,3],2,[1,3]],[1,2,3]]
print(index_all(2, tExample)) # should return [[0,0,1],[0,1],[1,1]]