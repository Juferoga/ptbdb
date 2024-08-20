s=str(7)
range_limit = int(s+s)

def square_array(array):
  """
  Modify the array in place squaring each element.

  Args:
    data: Array to modify.
  """
  return [i**2 for i in array]
  

def ascending_order_array(array):
  """
  Modify the array in place ordering the elements in ascending order.

  Args:
    data: Array to modify.
  """
  for i in range(len(array)):
    for j in range(i+1, len(array)):
      if array[i] > array[j]:
        array[i], array[j] = array[j], array[i]
  return array

def modify_list_in_place(array):
  """
  Modify the array in place removing the elements greater than the range.

  Args:
      data: Array to modify.
  """
  aux_array = []
  for i in array:
    if i < range_limit and i >= 0:
      aux_array.append(i)
  return aux_array

data = [
  [1, 2, 3, 5, 6, 8, 9],
  [-2, -1],
  [-6, -5, 0, 5, 6],
  [-10, 10]
]

i=0
for array in data:
  if len(array) >= 100:
    print(f"]----------[Test {i}]------------[")
    
    print("array original")
    print(array)
    
    print("Función square_array y resultado")
    array=square_array(array)
    print(array)
    
    print("Función ascending_order_array y resultado")
    array = ascending_order_array(array)
    print(array)
    
    print("Función modify_list_in_place y resultado")
    array = modify_list_in_place(array)
    print(array)
  i+=1