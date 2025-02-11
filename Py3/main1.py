#p1 p2
import pprint as p

class Cook_book:

    def __init__(self):
        self.cook_book = {}
        self.cook_ing = {}

    def load_rec_from_file(self, filename):
        print("Загрузка файла", filename)
        step=1
        name = ''
        count_ing = 0
        one_ing={}
        arr_ing=[]

        with open(filename, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                s = line.strip()
                if s=='':
                    step = 4
                elif step==1:
                    name = s
                    step = 2
                    continue
                elif step == 2:
                    count_ing = int(s)
                    step = 3
                    if count_ing ==0:
                        step=1
                    continue
                elif step == 3:
                    arr_temp=s.split('|')
                    if len(arr_temp)>2:
                        one_ing['ingredient_name']=str(arr_temp[0]).strip()
                        one_ing['quantity'] = int(str(arr_temp[1]).strip())
                        one_ing['measure'] = str(arr_temp[2].strip())
                        arr_ing.append(one_ing.copy())
                        continue
                if step == 4:
                    if len(one_ing) > 0:
                        self.cook_book[name]=arr_ing.copy()
                    else:
                        break
                    step=1
                    name = ''
                    arr_ing.clear()
                    one_ing.clear()


def print_hi(name):
    print(f'Hello, {name}')

if __name__ == '__main__':
    print_hi('world')

    cb=Cook_book()
    cb.load_rec_from_file("recipes.txt")
    p.pprint(cb.cook_book)
