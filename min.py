def sort_inputs(input_mass): # из полученных данных формируем список
    mass=[]
    for i in input_mass:
        split_inputs=(i.replace("\n", '')).split(',')
        mass.append({"car":split_inputs[0], "year":split_inputs[1],'color':split_inputs[2],"price":split_inputs[3]})
    return mass

class masth(object):
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

    def returner_all_parametrs(self):
        car=[]
        year=[]
        color=[]
        price=[]
        for i in self.lib:
            car.append(i['car'])
            year.append(i['year'])
            color.append(i['color'])
            price.append(i['color'])

        return {"car":set(car),'year':set(year),"color":set(color),"price":set(price)}




c=masth()
print("выбирите параметры")
print(c.returner_all_parametrs())
par=input()
val=input()
print(c.sort(par,val))