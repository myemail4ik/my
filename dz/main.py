input_file_name='input.txt'
output_file_name='Оutput.txt'
#---------------------------------------------------
parametrs=['car','year','color','price']
parametrs_ru=['Марки',"Года выпуска","Цвета","Цены"]
def show_parametrs():# русификатор
    j=0
    for i in parametrs_ru:
        j+=1
        print(str(j)+' - '+str(i))

def number_to_parametr(input):#русификатор
    if int(input)==1:
        return parametrs[0]
    elif int(input)==2:
        return parametrs[1]
    elif int(input)==3:
        return parametrs[2]
    elif int(input)==4:
        return parametrs[3]
    else:
        print('err')
        exit(0)

def sort_inputs(input_mass):  # из полученных данных формируем список
    mass = []
    for i in input_mass:
        split_inputs = (i.replace("\n", '')).split(',')
        mass.append(
            {"car": split_inputs[0], "year": split_inputs[1], 'color': split_inputs[2], "price": split_inputs[3]})
    return mass


def long_tab(lib): # находим колл-во символов в каждом эллементе
    tab={'car':1,'year':1,'color':1,'price':1,'all':1}
    for p in parametrs:
        for i in lib:
            if int(len(i[p]))>tab[p]:
                tab[p]=int(len(i[p])+1)
    tab['all']=int(tab['car'])+int(tab['year'])+int(tab['color'])+int(tab['price'])
    return tab

def conver_to_table(lib): # конвертируем данные в таблицу
    #print(lib)
    long_tab_ = long_tab(lib)
    output_string = ''
    for i in parametrs:
        tab_now = ''
        for tn in range(int(long_tab_[i]) - int(len(i))):
            tab_now += ' '
        output_string += str(i) + tab_now + '| '
    output_string += '\n'

    for i in lib:
        for t in parametrs:
            tab_now = ''
            for tn in range(int(long_tab_[t]) - int(len(i[t]))):
                tab_now += ' '
            output_string += i[t] + tab_now + '| '
        output_string += '\n'
    return output_string


class car_sort(object):
    def __init__(self):
        self.lib = []
        with open(input_file_name,'r',encoding="UTF-8'") as file_in: # получаем из файла данные
            for i in file_in.readlines():
                self.lib.append(i)
        self.lib=sort_inputs(self.lib)
        #print(self.lib)

    def __str__(self):# return_all_table
        return conver_to_table(self.lib)

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

        #return {"car":set(car),'year':set(year),"color":set(color),"price":set(price)}
        return  'Марки: {} | Года выпуска: {} | Цвета: {} | Цены: {}'.format(set(car),set(year),set(color),set(price))

    # _____________Сортировки______________
    def sort(self,parameter,value): # сортировка
        mass_out=[]
        j=0
        for i in self.lib:
            if i[parameter]==value:
                j+=1
                i.update({'number': j})
                mass_out.append(i)
        return mass_out

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

    def sort_with_comparison(self,par,val,direction,reverse_):
        mass = []
        for i in self.lib:
            if direction==True:
                if int(i[par]) >= int(val):
                    mass.append(i[par])
            else:
                if int(i[par]) <= int(val):
                    mass.append(i[par])

        if reverse_ == True:
            mass = sorted(mass)

        else:
            mass = sorted(mass, reverse=True)


        out_mass = []
        for i in mass:
            for j in self.lib:
                if i == j[par] and not j in out_mass:
                    out_mass.append(j)
                    break
        return out_mass

    def sort_price_in_year(self,year_chek,reverse_): # 6 сортировка по году и марке (отфильтровать по цене машины конкретного год)
        mass = []
        for i in self.lib:
            if int(i['year'])==year_chek:
                mass.append(int(i['price']))


        if reverse_ == True:
            mass = sorted(mass)

        else:
            mass = sorted(mass, reverse=True)


        out_mass = []
        for i in mass:
            for j in self.lib:
                if i == int(j['price'])and not j in out_mass:
                    out_mass.append(j)
                    break
        return out_mass


def numbers(mass):
    j=0
    myiter = iter(mass)
    while j<int(len(mass))-1:
        n=next(myiter)
        print('Марка: {} | Год выпуска: {} | Цвет: {} | Цена: {} | В списке: {}'.format(n['car'],n['year'],n['color'],n['price'],n['number']))
        print("press enter to next".upper())
        input()
        j+=1
    n = next(myiter)
    print('Марка: {} | Год выпуска: {} | Цвет: {} | Цена: {} | В списке: {}'.format(n['car'], n['year'], n['color'], n['price'], n['number']))
    print('ALL')



try:
    car=car_sort()
    print(car)
    with open('Table_all.txt', 'w',encoding='UTF-8') as file:
       file.write(str(car))
    print(
        '1 - поиск по значению и параметру\n'
        '2 - сортировка в порядке возрастания/убывания\n'
        '3 - колличество автомобилей заданного параметра\n'
        '4 - отфильтровать автомобили по дате\n'
        '5 - отфильтровать автомобили по цене\n'
        '6 - отфильтровать по цене машины конкретного года\n'
        )
    j=input('Введите вид сортировки: ')

    if j=='1':
        print("выбирите параметры")
        print(car.returner_all_parametrs())
        show_parametrs()
        par=number_to_parametr(input('введите параметр, например "Марки": '))
        val=input('введите значение, например "lada": ')
        out = (car.sort(par, val))
        if int(len(out)) > 1:
            numbers(out)
        print(conver_to_table(out))


    if j=='2':
        print(car.returner_all_parametrs())
        show_parametrs()
        par = number_to_parametr(input('введите параметр, например "Марки": '))
        print("отоброзить в обратном порядке?")
        rev=input("1-yes/Enter-No: ")
        if rev=="1":
            out=car.sort_(par,True)
        else:
            out=car.sort_(par, False)
        print(conver_to_table(out))

    if j=='3':
        print(car.returner_all_parametrs())
        show_parametrs()
        par = number_to_parametr(input('введите параметр, например "Марки": '))
        val = input('введите значение, например "lada": ')
        print("Count: "+str(par)+' / '+str(val)+" = "+str(car.count_cars(par,val)))

    if j=="4":
        print(car.returner_all_parametrs())
        val = int(input('Ведите дату отсчета: '))
        direction = int(input("Введите 1-Страше: "+str(val)+"/ 2- Моложе: "+str(val)+': '))
        par = 'year'
        reverse_ = False
        if direction == 1:
            out=car.sort_with_comparison(par, val, True, reverse_)
        else:
            out=car.sort_with_comparison(par, val, False, reverse_)
        print(conver_to_table(out))

    if j=="5":
        print(car.returner_all_parametrs())
        val = int(input('Ведите цену '))
        direction = int(input("Введите 1-Дороже: "+str(val)+"/ 2- Дешевле: "+str(val)+': '))
        par = 'price'
        reverse_ = False
        if direction == 1:
            out=car.sort_with_comparison(par, val, True, reverse_)
        else:
            out=car.sort_with_comparison(par, val, False, reverse_)
        print(conver_to_table(out))

    if j=="6":
        year=int(input("Ведите год "))
        direction=int(input("Введите 1-От Большего к меньшему / 2- От Меньшего к большему "))
        if direction == 1:
            out=car.sort_price_in_year(year,False)
        else:
            out = car.sort_price_in_year(year, True)

        if int(len(out))>0:
            print(conver_to_table(out))
        else:
            print('Машин этого года не найдено!!!')

    if int(len(out))>0:
        direction = input('Сохранить в файл?\n'
                          '2-Yes/1-No: ')
        if direction=='2':
            with open(output_file_name,'w',encoding='UTF-8') as file:
                file.write(conver_to_table(out))
        else:
            pass

except Exception as e:
    print(e)
