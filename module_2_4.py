numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [] #содержит простые числа
not_primes = [] #содержит не простые числа

for i in numbers: #перебираем числа из списка
  is_prime = True 

  if i < 2: #числа меньше 2 не являются простыми
    is_prime = False
  else: #выбираем делители от 2 до корня из числа
    for j in range(2,int(i**0.5) + 1):
      if i % j == 0:#если число делится на делитель без остатка, то оно не  простое
        is_prime = False
        break

  if is_prime: #если число простое, то вывод в primes
    primes.append(i)
  else:
    not_primes.append(i)

print('Простое число: ', primes)
print('Не простое число: ', not_primes)