from pythonBasic.A import A


class B(A):
    def __init__(self):
        A.__init__(self,10,10)

    def result(self):
        print(A.add(self))

obj=B()
obj.result()
