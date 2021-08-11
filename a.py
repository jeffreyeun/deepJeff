import numpy as np
from numpy.core.numeric import outer

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output
    def forward(self, in_data):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x**2

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

data = np.array(2.0)
x = Variable(data)
f = Square()
y = f(x)
print(type(y))
print(y.data)