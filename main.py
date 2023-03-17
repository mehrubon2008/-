''' @avtor ---nabiev--mehrubo--'''
from random import * 
def main():
  n = int(input('количество цифр: '))
  v = []
  for i in range(n):
    v.append(randint(0,9))
  print(*v, sep = '')
if __name__ == '__main__':
  while True:
    main()
  
