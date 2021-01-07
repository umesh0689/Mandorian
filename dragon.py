from mandalorian import Person
from mandalorian import Mandalorian
import subprocess as sp
class Dragon(Person):
    def __init__(self,firstco,secondco):
        Person.__init__(self,firstco,secondco)
        self._firstco=firstco
        self._secondco=secondco
        self.__matrix=[]
        self.__dra_bullets=[]
        self.__shape='*'
        self.__dra_bull_cnt=0
    def create_dragon(self,firstco,secondco):
        with open('dragon.txt','r') as f:
            myname=[line.strip("\n") for line in f]
        for i in range(14):
            temp=[]
            for j  in range(42):
                temp.append(" ")
            self.__matrix.append(temp)

        for i in range(14):
            cnt=0
            for j in myname[i]:
                self.__matrix[i][cnt]=j
                cnt=cnt+1


    def add(self,matrix,back):
        for i in range(14):
            for j in range(42):
                back[self._firstco+i][self._secondco+j]='l'
                matrix[self._firstco+i][self._secondco+j]=self.__matrix[i][j]
    def remove_dragon(self,matrix,back):
        for i in range(14):
            for j in range(42):
                back[self._firstco+i][self._secondco+j]=' '
                matrix[self._firstco+i][self._secondco+j]=' '


    def move_dragon(self,fco,sco,matrix,back):
        if sco > 250:
            if(fco < 30):
                self.remove_dragon(matrix,back)
                if(fco < self._firstco):
                    self._firstco= self._firstco - 1
                elif fco >  self._firstco:
                    self._firstco= self._firstco + 1
                if self._firstco > 20:
                    self._firstco = 20

                self.add(matrix,back)


    def fire_dragon_bull(self,matrix,back):
        temp=[]
        temp.append(self._firstco)
        temp.append(self._secondco-1)
        temp.append(1)
        temp.append(1)
        self.__dra_bullets.append(temp)
        temp=[]
        temp.append(self._firstco+12)
        temp.append(self._secondco-1)
        temp.append(1)
        temp.append(1)
        self.__dra_bullets.append(temp)
        back[self._firstco][self._secondco-1]="e"
        matrix[self._firstco][self._secondco-1]=self.__shape
        back[self._firstco+12][self._secondco-1]="e"
        matrix[self._firstco+12][self._secondco-1]=self.__shape
        self.__dra_bull_cnt=self.__dra_bull_cnt+2

    def dra_bull_collision(self,matrix,back,store,life):
        # print(life)
        for i in self.__dra_bullets:
            if i[2]==1:
                fco=i[0]
                sco=i[1]
                if(back[fco][sco]=='d'):
                    i[2]=0
                if(back[fco][sco]=='c'):
                    i[2]=0
                    if(life  < 2):
                        sp.call('clear',shell='True')
                        print("you lost :( \n")
                        quit()
                    life=life -1
                if(back[fco][sco]==' '):
                    i[3]=1 
                    back[i[0]][i[1]]='e'
                    matrix[i[0]][i[1]]=self.__shape

        return life


    def remove_dra_bullet(self,i,matrix,back):
        self.__dra_bullets[i][2]=0
        self.__dra_bullets[i][3]=0
        back[self.__dra_bullets[i][0]][self.__dra_bullets[i][1]]=' '
        matrix[self.__dra_bullets[i][0]][self.__dra_bullets[i][1]]=' ' 

    def move_dra_bullet(self,matrix,back,store,start,life):
        for i in range(self.__dra_bull_cnt):
            if(self.__dra_bullets[i][2]==1):
                if(self.__dra_bullets[i][3]==1):
                    back[self.__dra_bullets[i][0]][self.__dra_bullets[i][1]]=' '
                    matrix[self.__dra_bullets[i][0]][self.__dra_bullets[i][1]]=' '
                    self.__dra_bullets[i][3]=0
                self.__dra_bullets[i][1]=self.__dra_bullets[i][1]-1
                life=self.dra_bull_collision(matrix,back,store,life)
                # self.dra_bull_collision(matrix,back,store,life)
        return life


