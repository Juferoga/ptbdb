s = 7

def modify_list_in_place(data, s):
  """
  Modifies a list of numbers in-place by removing digits greater than or equal to 's'
  and preserving the order, including leading zeros.

  Args:
      data: A list of integers.
      s: The threshold for digit removal.
  """
  write_index = 0 
  for num in data:
    new_num_str = ""  # Almacenamos el nuevo número como cadena para preservar ceros a la izquierda
    for digit_str in str(num):
      digit = int(digit_str)
      if digit < s:
        new_num_str += digit_str
    if new_num_str:  # Si la cadena no está vacía, convertimos a entero y agregamos
      data[write_index] = int(new_num_str)
      write_index += 1

  del data[write_index:]

def reverse_array(array): 
  """
  Reverses an array in place.

  Args:
    array: A list of integers.
  """
  left = 0
  right = len(array) - 1
  while left < right:
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1


data =  [
  [1, 2, 3, 4, 5, 7],
  [10, 20, 30, 40],
  [17],
  [77, 3],
  [75],
  [7, 2, 1],
  [70, 7, 5, 4, 3, 2, 8, 8, 29, 1] 
] 

i=0
for array in data:
  if len(array) <= 100:
    print(f"]----------[Test {i}]------------[")
    
    print("Array original")
    print(array)

    print("Función modify_list_in_place y resultado")
    modify_list_in_place(array, s)
    print(array)

    print("Función reverseArray y resultado")
    reverse_array(array)
    print(array)
  i+=1
