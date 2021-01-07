from colorama import *
from random import randint
from objects import Objects
class Magnet(Objects):
    def __init__(self):
        Objects.__init__(self)
        self.__magarr=[]
        Magnet.__address=[]
        self.__times=0
    def creating_mag_shape(self):
        with open('magnet.txt','r') as f:
            myname=[line.strip('\n') for line in f]
        for i in range(5):
            temp=[]
            for j  in range(7):
                temp.append(' ')
            self.__magarr.append(temp)
        for i in range(5):
            cnt=0
            for j in myname[i]:
                self.__magarr[i][cnt]=Fore.GREEN+j+Style.RESET_ALL
                cnt=cnt+1

    def creating_magnet(self,matrix,back):
        self.__times=randint(2,2)
        for i in range(self.__times):
            self.__temp=[]
            for j in range(3):
                self.__temp.append(' ')
            Magnet.__address.append(self.__temp)

        firstco=randint(1,1)
        self.__temp=[]
        self.__temp.append(randint(25,75))
        self.__temp.append(randint(150,200))
        for i in range(self.__times):
            Magnet.__address[i][0]=1
            Magnet.__address[i][1]=self.__temp[i]
            Magnet.__address[i][2]=self.__times

    def place_mag(self,matrix,back):    
        firstco=1
        for i in range(self.__times):
            secondco=self.__temp[i]    
            for j in range(5):
                for k in range(7):
                    back[firstco+j][secondco+k]="a"
                    matrix[firstco+j][secondco+k]=self.__magarr[j][k]

    # def remove_mag(self,matrix,back):
    #     firstco=1
    #     for i in range(self.times):
    #         secondco=self.temp[i]    
    #         for j in range(5):
    #             for k in range(7):
    #                 back[firstco+j][secondco+k]=" "
    #                 matrix[firstco+j][secondco+k]=" "



    def check_field(firstco,secondco,start):
        if(secondco<102):
            sco=Magnet.__address[0][1]
            fco=Magnet.__address[0][0]
            if(secondco > sco-24):
                if(secondco < sco+2):
                    return secondco+1
                elif secondco < sco+26:
                    return secondco-1

        elif secondco < 227:
            sco=Magnet.__address[1][1]
            fco=Magnet.__address[1][0]
            if sco < start:
                if secondco > sco-24:
                    if secondco < sco+2:
                        return secondco+1
                    elif secondco < sco+26 :
                        return secondco-1
        return secondco
    