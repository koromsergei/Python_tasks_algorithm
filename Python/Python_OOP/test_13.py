def get_data_fig(*args, **kwargs):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_, kwargs.values()

def foo(s, sep="-"):
    s = s.lower()
    lst = [sep if i == " " else t[i] for i in s]
    return "".join(lst)


s = input().split()
temp = []
for i in s:
    if set(i.lower()) & set(t.keys()) != 0:
        temp.append(foo(i.lower()))
    else:
        temp.append(i.lower())

print(temp)
#print(foo(s, sep="+"))
