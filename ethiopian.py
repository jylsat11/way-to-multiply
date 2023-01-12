def hello():
    print('Good luck!!')

if __name__ == '__main__':
    hello()



#division

def division_two(division_num:int):
  division_list = [division_num]
  while division_num!=1:
    division_list.append(division_num//2)
    division_num=division_num//2

  return division_list

