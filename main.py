"""print("hello, \nworld")
print("hello, \tworld")
print("      /|   ")
print("     / | ")
print("    /  |  ")
print("   /   |  ")
print("  /    | ")
print(" /     |  ")
print("/______| ")
age = 10#integervalue

age +=  1
cash = 100.5#float value
print(age)

name = "john"
print(name +str(10) )
 ar shegvizlia da mateba ricxvebis romlic ar aris stringi stringebistvis mara stringis dawerit shetvizlia

number = [10, 20, 30 ]# [] es nishnavs rom es litsia da amshi ragaciscahwera gvinda

print(number[0])# indeqsebit shegvizlia gamovizaxot is ricxvebi rac chven gvinda


names = ["jhon", "johnny"]

mylist = [10, "jhnn",  30]

mylist[1] = "johnny"
print(mylist)

numbers = (10, 20, 30)
umbers = (10, 200, 30)# ase sheizleba amis hecvla mara ise ver shecvli

print(numbers)

ages = {"jhon": 10, "johnny":20}# gasagebi am ageshi aris jhone da jhone iaxebs 10 ts rogc gavige

eys = list(ages.keys())# es gvazlevs objects roca win uwert lists rac ar unda chavwerot listshi gadaiwereba
vals = list(ages.values())
print(keys)# ase shegvizlia valuebis gamozaxeba
print(vals)


sleeping = True

print(sleeping)

print("hello, world")# prints hello world


age = 10

if age == 11:# aq shegvizlia dvwerot metia>,naklebia<,metia an toli>=,nakelbia an toli<= udris ar udris da ashe.
    print("the age is 10")
elif age== 12:
#es igive if aris mara tu if ar gamoizaxa mashin elifs gamoizaxebs
    print("the age is 12.")# ramdenime elif statmenti shegvizlia gvqondes
elif age== 13:
    # es rogor moqmdebeds orogr da pythoni yvelas chekavs da romelic emtxveva imas printavs
    print("the age is 13 ")
else:
    print("unknown age")# aq ar sheizleba rames chawera elsshi marar elifshi sheizleba

index = 0#

while index < 10:# aq shegvizlia rac gvinda is davwerot anu stringi bollenan tipi da asehe shevadarot gamovalkot dashe

    print(index)
    index += 1# es while loop igive rogorc java scriptshi mara ragaceebi gansxvavdeba

numbers = [1, 2, 3] # <(esaa is nuber klasi) aq ra moxda pythonma aigo yvela elementi da cahwere inini element jgufshi rac qemot gviweria
# mere es elementebi darinta elementebi aigo number clasidan romelic mocemuli gvaqvs zemot
for element in numbers:
    print(element)

name = "jhon"

for char in name:
    print(char )

age = 10

if age == 10:
    pass#amit shegvizlia gamovtvot es moqmedeba amis gamoyeneba yvela moqmedebashi sheizleba for-shi els=shi elif-shi da if-sic"""





#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#for i in numbers:
   # print(i)#ase printavs 1 dan 10mde da
   # if i == 10:
     #   print(i)# ase printavs marto ats ragan yvela ricxvs naxulobs da marto 10ts tovebs

      #  break

#text = input("enter something:")# es su strings daabrunebs romc ricxvi dawero mainc daabrunebs strings da ro inti gavaketot ase vaketebt

#text = int(text)# exlac mivigebt rocxvs roca chavwert mara exla matematukuri operaciebis gakketebac sheizleba radgan exla ricxvebi integeris saxit chaiwereba
#print(text + 1 )



#num = input("Enter a number:")

#try:# es gaaketebs imas ro rac weria aq magas chartavs marar rasac ara mere except blokshi gadava

  #num = int(num)
#except:
    #pass

#print(num)


#num = 10
#bignum = 10
#while num < 1000 :

    #print(num*num)

 #   if num == bignum:

     #   break



#def square(num):
   # return num ** 2


#print(square(5))

#mylist = [1, 1, 2, 3, 4, 5]

#def print_elements(list1):
    #for e in list1:
     #   print(e)

#print_elements(mylist)

#def fib(n):
   # a = 0
   # b = 1
   # print(a)
  #  print(b)
   # for i in range(2, n):
    #    c = a + b
     #   a = b
      #  b = c
       # print(a+b)

#fib(5)

#with open("data.txt", "r") as file:
    #filereader = file.read()


#with open("data.txt", "a") as data:
    #data.writelines(filereader)





class rectangle:
    def __init__(self , width, length):
        self.width = width
        self.length = length

    def area(self):
     print(f"{self.width} * {self.length} = {self.width * self.length}" )
    def perimeter(self):
        print  (f"({self.width } + {self.length} * 2) = {(self.width + self.length) * 2 } ")
    def print_info(self):
        print(f"the area of rectangle is {self.area()}, the perimeter of the rectangele is {self.perimeter()} and the width and length of rectangle is {self.width} , {self.length}")





class Calculator:

    def __init__(self, first_num, second_num):
        self.first_num, self.second_num = first_num, second_num

    def addition(self):
        print(f'{self.first_num} + {self.second_num} = {self.first_num + self.second_num}')

    def subtract(self):
        print(f'{self.first_num} - {self.second_num} = {self.first_num - self.second_num}')

    def multiplication(self):
       print(f'{self.first_num} * {self.second_num} = {self.first_num * self.second_num}')

    def division(self):
       print(f'{self.first_num} / {self.second_num} = {self.first_num / self.second_num}')

if __name__ == '__main__':
   calculate = Calculator(6, 5)
   calculate.addition()
   calculate.subtract()
   calculate.multiplication()
   calculate.division()






class Employee:
    def __init__(self, name, surname, age, salary):
        self.name, self.surname, self.age, self.salary = name, surname, age, salary

    def info(self):
        return f'name {self.name}, surname {self.surname}, age {self.age}, salary {self.salary}'


employees = []

with open("dataset1.csv", "r") as dataset:
    data = [line.split(",") for line in dataset.read().split("\n")][1:-1]
    employees = [Employee(name, surname, age, salary) for [name, surname, age, salary] in data]

print(f'lowest salary employee - {min(employees, key=lambda employee: employee.salary).info()}')
print(f'highest salary employee  - {max(employees, key=lambda employee: employee.age).info()}')




class rectangle():
    def __init__(self , width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    def perimeter(self):
        return (self.width + self.length) * 2
    def print_info(self):
        print(f"the area of rectangle is {self.area()}, the perimeter of the rectangele is {self.perimeter()} and the width and length of rectangle is {self.width} , {self.length}")

if __name__ == '__main__' :
    print(rectangle(20, 30))