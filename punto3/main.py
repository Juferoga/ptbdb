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
