def format_name(f_name,l_name):
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    return formated_f_name,formated_l_name
print(format_name("ANna","rOSe"))


#############################################################

def function1(text):
    return text + text

def function2(text):
    return text.title()
x=function2(function1("hello"))
print(x)

