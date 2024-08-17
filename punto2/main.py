s=str(7)
range = int(s+s)

def square_array(array):
  """
  Modify the array in place squaring each element.

  Args:
    data: Array to modify.
  """
  [i**2 for i in array]

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

def modify_list_in_place(array):
  """
  Modify the array in place removing the elements greater than the range.

  Args:
      data: Array to modify.
  """
  for i in range(len(array)):
    if array[i] > range:
      array.pop(i)

data = [
  [1, 2, 3, 5, 6, 8, 9],
  [-2, -1],
  [-6, -5, 0, 5, 6],
  [-10, 10]
]

i=0
for array in data:
  print(f"]----------[Test {i}]------------[")
  
  print("array original")
  print(array)
  
  #! Las funciones no modifican el array original (arreglar)
  
  # print("Función square_array y resultado")
  # square_array(array)
  # print(array)
  
  # print("Función ascending_order_array y resultado")
  # ascending_order_array(array)
  # print(array)
  
  # print("Función modify_list_in_place y resultado")
  # modify_list_in_place(array)
  # print(array)
  
  i+=1