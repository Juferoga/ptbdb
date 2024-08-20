---
title: Fase de implementación
author: Juferoga
date: 2023-02-05
category: Jekyll
layout: post
---

## Implementación Python

---

## Reto 1

```python
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
  [7],
  [77],
  [75],
  [7, 2, 1],
  [70, 7, 5, 4, 3, 2, 8, 8, 29, 1] 
] 

i=0
for array in data:
  if len(array) >= 100:
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

```

## Reto 2

```python
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

```

## Reto 3

```python
def minimum_addition_unreachable(coins):
  """
  Find the minimum addition to be unreachable.

  Args:
    array: A list of integers (coins).
  """
  addition_reachable = 0 # La minima suma alcanzable
  for coin in coins:
    if coin > addition_reachable + 1:
      return addition_reachable + 1 # Si la moneda es mayor a la suma alcanzable + 1, retornamos la suma alcanzable + 1
    addition_reachable += coin # Suma la moneda a la suma alcanzable
  return addition_reachable + 1 # Si no se cumple la condición anterior, retornamos la suma alcanzable + 1

data = [
  [5, 7, 1, 1, 2, 3, 22],
  [1, 1, 1, 1, 1],
  [1, 5, 1, 1, 1, 10, 15, 20, 100]
]

i=0
for coins in data:
  print(f"]----------[Test {i}]------------[")
  
  print("Original")
  print(coins)
  
  coins = sorted(coins)
  print("Organized", sorted(coins))
  
  print("Minimum addition to be unreachable")
  print(minimum_addition_unreachable(coins))
  
  i+=1
```
