# p2
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

    # Формирование компонентов на кол-во персон
    def get_shop_list_by_dishes(self, dishes, person_count):
        arr_ing=[]
        res={}
        for el in self.cook_book :
            if el in dishes:
                arr_ing.append(self.cook_book[el])
        for elist in arr_ing:
            for el in elist:
                ing=el['ingredient_name']
                mea = el['measure']
                qua = el['quantity']
                if ing in res:
                    if res[ing]['measure']==mea:
                        k=qua+res[ing]['quantity']
                    else:
                        k=qua
                    res[ing] = {'measure': mea, 'quantity': k}
                else:
                    res[ing] = {'measure': mea, 'quantity': qua}
        if person_count > 1:
            for el in res:
                res[el]['quantity'] = res[el]['quantity'] * person_count
        self.cook_ing=res.copy()


def print_hi(name):
    print(f'Hello, {name}')

if __name__ == '__main__':
    print_hi('world')

    cb=Cook_book()
    cb.load_rec_from_file("recipes.txt")
    p.pprint(cb.cook_book)

    cb.get_shop_list_by_dishes(['Фахитос','Омлет'], 2)

    print('----')
    p.pprint(cb.cook_ing)



