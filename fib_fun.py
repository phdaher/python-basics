def fibonacci(termo):
  t1 = 0
  t2 = 1
  cont = 3
  print(t1, t2, end=' ')
  while cont <= termo:
    t3 = t1 + t2
    print(t3, end=" ")
    t1 = t2
    t2 = t3
    cont += 1
print(fibonacci(20))