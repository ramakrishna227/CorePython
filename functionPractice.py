def function(n=-5):
    if n > 0:
        print(n, end=' ')
        function(n - 1)
    else:
        print(n)


function(3)
x = function()
print(x)


# python has a maximum recursion depth of 996

def doubler(y=1):
    return y * 2


z = doubler(10)
print(z)
