from colorama import Fore,Back,Style
from random import randint
class Scenery:
    def __init__(self):
        self.__land=Back.RED+'G'+Style.RESET_ALL
        self.__sky=Back.BLUE+'S'+Style.RESET_ALL
        self.__coins=Fore.YELLOW+'$'+Style.RESET_ALL
    
    def creating_sky(self,matrix,back):
        for i in range(400):
            back[0][i]='s'
            matrix[0][i]=self.__sky

    def creating_land(self,matrix,back):
        for i in range(400):
            back[34][i]='g'
            matrix[34][i]=self.__land

    def create_coins(self,matrix,back):
        times=randint(10,30)
        for i in range(times):
            size=randint(3,7)
            like=randint(1,2) # 1=horizontal  2=group_printing
            firstco=randint(1,31)
            secondco=randint(0,330)
            if(like==1):
                for i in range(size):
                    back[firstco][secondco+i]='m'
                    matrix[firstco][secondco+i]=self.__coins
            if(like==2):
                back[firstco+1][secondco+0]='m'
                back[firstco+0][secondco+1]='m'
                back[firstco+1][secondco+1]='m'
                back[firstco+2][secondco+1]='m'
                back[firstco+1][secondco+2]='m'
                matrix[firstco+1][secondco+0]=self.__coins
                matrix[firstco+0][secondco+1]=self.__coins
                matrix[firstco+1][secondco+1]=self.__coins
                matrix[firstco+2][secondco+1]=self.__coins
                matrix[firstco+1][secondco+2]=self.__coins