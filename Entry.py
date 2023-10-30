from Methods import *

def gradientX(x, y):
    x = max(x, 0.001)
    x = min(x, 0.999)
    y = max(y, 0.001)
    y = min(y, 0.999)
    return -y*(-2*x-y+1)/8
    
def gradientY(x, y):
    x = max(x, 0.001)
    x = min(x, 0.999)
    y = max(y, 0.001)
    y = min(y, 0.999)
    return -x*(-2*y-x+1)/8

def originalFunction(x, y):
    # guide towards valid values
    if (x <= 0):
        return 1 + abs(x) + abs(y)
    if (y <= 0):
        return 1 + abs(x) + abs(y)
    return -((1 - x - y) * x * y) / 8

steps, result = gradient_descent((0, 0), gradientX, gradientY, 10)
print(len(steps))
print(result)
show_graph(steps)

steps, result = fastest_descent((0, 0), gradientX, gradientY, originalFunction)
print(len(steps))
print(result)
show_graph(steps)

steps, result = nelder_mead((0, 0), originalFunction)
print(len(steps))
print(result)
show_graph(steps)
