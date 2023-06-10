def sum(x,y):
    print(x + y)
def minus(x,y):
    print(x - y)
def umn(x,y):
    print(x * y)
def delit(x,y):
    if y != 0:
        print(x / y)
    
x = int(input())
y = int(input())
print("Напишите одну из команд:\n+ * / - Выход")
data = input()
while (data != "Выход"):
    if data == "+":sum(x,y)
    elif data == "*":umn(x,y)
    elif data == "/":delit(x,y)
    elif data == "-":minus(x,y)
    else: print("Введена неправильная команда")
    data = input("Напишите одну из команд:\n+ * / - Выход\n")