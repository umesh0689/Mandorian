from random import randint
from colorama import Fore,Back,Style
from objects import Objects
class Beams(Objects):
    def __init__(self):
        Objects.__init__(self)
        self._mat=[]
        self.__shape1=[Fore.RED+'o'+Style.RESET_ALL,Fore.RED+'='+Style.RESET_ALL,Fore.RED+'='+Style.RESET_ALL,Fore.RED+'='+Style.RESET_ALL,Fore.RED+'o'+Style.RESET_ALL]
        self.__shape2=[Fore.RED+'o'+Style.RESET_ALL,Fore.RED+'|'+Style.RESET_ALL,Fore.RED+'|'+Style.RESET_ALL,Fore.RED+'|'+Style.RESET_ALL,Fore.RED+'o'+Style.RESET_ALL]
        self.__power=['>']
    def get_beams(self):    
        with open('beam.txt','r') as f:
            myname=[line.strip('\n') for line in f]
        self.__mat=[]
        for i in range(6):
            temp=[]
            for j  in range(6):
                temp.append(' ')
            self.__mat.append(temp)
        for i in range(6):
            cnt=0
            for j in myname[i]:
                self.__mat[i][cnt]=Fore.RED+j+Style.RESET_ALL
                cnt=cnt+1
    def create_beams(self,matrix,back,store):
        for cnt in self._arr:
            like=cnt[0]
            firstco=cnt[1]
            secondco=cnt[2]
            if (like==1):
                for i in range(6):
                    for j in range(6):
                        back[firstco+i][secondco+i]='b'
                        matrix[firstco+i][secondco+j]=self.__mat[i][j]
                        store[firstco+i][secondco+j][0]=like
                        store[firstco+i][secondco+j][1]=firstco
                        store[firstco+i][secondco+j][2]=secondco


            if(like==2):
                for i in range(5):
                    back[firstco][secondco+i]='b'
                    matrix[firstco][secondco+i]=self.__shape1[i]
                    store[firstco][secondco+i][0]=like
                    store[firstco][secondco+i][1]=firstco
                    store[firstco][secondco+i][2]=secondco

            if(like==3):
                 for i in range(5):
                    back[firstco+i][secondco]='b'
                    matrix[firstco+i][secondco]=self.__shape2[i]
                    store[firstco+i][secondco][0]=like
                    store[firstco+i][secondco][1]=firstco
                    store[firstco+i][secondco][2]=secondco

            if(like==4):
                for i in range(1):
                    back[firstco+i][secondco]='p'
                    matrix[firstco][secondco+i]=self.__power[i]
