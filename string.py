def my_function(x):
  return x[::-1]
mystring = my_function("Nitesh mero sakyo")
print(mystring)

def while_loop_reverse(a):
    str = ""
    for i in a:
       str = i + str
    return(str)
strings = while_loop_reverse("hellohello")
print(strings)




def while_loop_reverse(a):
    str2 = ''
    i = len(a) - 1
    while(i >= 0):
        str2 = str2 + a[i]
        i = i - 1
    return(str2)
string = while_loop_reverse("hello")
print(string)

