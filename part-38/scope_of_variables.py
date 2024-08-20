# num = 1
# def hello():
    
#     message = "good morning!"
#     print(num)

# hello()

var0 = "global var"

def fun1():
    var1 = "local var 1"
    print(var0)


def fun2():
    var2 = "local var 2"
    print(var0)

fun1()
fun2()
print(var0)