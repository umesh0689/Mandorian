from random import randint
class Objects:
    def __init__(self):
        self._type=' '
        self._arr=[]
    def creating_objects(self):
        times=randint(10,20)
        for i in range(times):
            temp=[]
            temp.append(randint(1,4))#1=slant 2=horizontal 3=vertical 4=powerup
            temp.append(randint(1,27))
            temp.append(randint(0,330))
            self._arr.append(temp)