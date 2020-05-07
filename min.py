def sort_inputs(input_mass): # из полученных данных формируем список
    mass=[]
    for i in input_mass:
        split_inputs=(i.replace("\n", '')).split(',')
        mass.append({"car":split_inputs[0], "year":split_inputs[1],'color':split_inputs[2],"price":split_inputs[3]})
    return mass

def numbers(mass):
    j=0
    if int(len(mass))>1:
        myiter = iter(mass)
        print('\n')
        while j<int(len(mass))-1:
            print(next(myiter))
            print("press enter to next")
            input()
            j+=1
        print(next(myiter))
        print('ALL')
    else:
        print(mass)

class car_sort(object):
    def __init__(self):
        self.lib = []
        with open("input.txt",'r',encoding="UTF-8'") as file_in: # получаем из файла данные
            for i in file_in.readlines():
                self.lib.append(i)
        self.lib=sort_inputs(self.lib)


    def __str__(self):
        return str(self.lib)

    def sort(self,parameter,value): # сортировка
        mass_out=[]
        j=0
        for i in self.lib:
            if i[parameter]==value:
                j+=1
                i.update({'number': j})
                mass_out.append(i)
        return mass_out

    def count_cars(self,par,name): # колличество по параметрам
        out=0
        for i in self.lib:
            if str(i[str(par)])==str(name):
                out+=1
        return out

    def returner_all_parametrs(self): #  все параметры для сортировки
        car=[]
        year=[]
        color=[]
        price=[]
        for i in self.lib:
            car.append(i['car'])
            year.append(i['year'])
            color.append(i['color'])
            price.append(i['price'])

        return {"car":set(car),'year':set(year),"color":set(color),"price":set(price)}

    def sort_(self,par,reverse_): # сортировка с параметрами(возрастание или убывание)
        mass=[]
        for i in self.lib:
            mass.append(i[par])

        if reverse_== False:
            mass=sorted(mass)

        else:
            mass=sorted(mass,reverse=reverse_)
        out_mass=[]
        for i in mass:
            for j in self.lib:
                if i==j[par]:
                    out_mass.append(j)
                    break
        return out_mass


try:
    c=car_sort()
    print('1 - поиск по значению и параметру\n'
          '2 - сортировка в порядке возрастания.убывания\n'
          '3 - колличество автомобилей заданного параметра')
    j=input('введите вид сортировки ')
    if j=='1':
        print("выбирите параметры")
        print(c.returner_all_parametrs())
        par=input('введите параметр, например "car" ')
        val=input('введите значение, например "lada" ')
        print(c.sort(par,val))
        numbers(c.sort(par,val))

    if j=='2':
        print(c.returner_all_parametrs())
        par = input('введите параметр, например "car" ')
        print("отоброзить в обратном порядке?")
        rev=input("1-yes/0-No ")
        if rev=="1":
            print(c.sort_(par,True))
        else:
            print(c.sort_(par, True))
    if j=='3':
        print(c.returner_all_parametrs())
        par = input('введите параметр, например "car" ')
        val = input('введите значение, например "lada" ')
        print("Count: "+str(par)+' / '+str(val)+" = "+str(c.count_cars(par,val)))

except Exception as e:
    print(e)

