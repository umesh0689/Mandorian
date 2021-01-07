from colorama import Fore,Back,Style
from alarmexception import AlarmException
from getinp import _getChUnix as getChar
import time
import os
import signal
from background import Background
import subprocess
from magnet import Magnet
# from dragon import Dragon
class Person:
    def __init__(self,firstco,secondco):
        self.__firstco=firstco
        self.__secondco=secondco
        # self.__lives=5
    
    def add(self,matrix,back):
        for i in range(3):
            for j in range(3):
                back[self._firstco+i][self._secondco+j]='l'
                matrix[self._firstco+i][self._secondco+j]=self.__matrix[i][j]
    
class Mandalorian(Person):
    def __init__(self,firstco,secondco):
        Person.__init__(self,firstco,secondco)
        self.__shape1=[[' ',Fore.GREEN+'o'+Style.RESET_ALL,' '],
        [Fore.GREEN+'/'+Style.RESET_ALL,Fore.GREEN+'|'+Style.RESET_ALL,Fore.GREEN+'\\'+Style.RESET_ALL],
        [Fore.GREEN+'^'+Style.RESET_ALL,' ',Fore.GREEN+'^'+Style.RESET_ALL]]
        self.__shape=[[' ',Fore.CYAN+'o'+Style.RESET_ALL,' '],
        [Fore.CYAN+'/'+Style.RESET_ALL,Fore.CYAN+'|'+Style.RESET_ALL,Fore.CYAN+'\\'+Style.RESET_ALL],
        [Fore.CYAN+'^'+Style.RESET_ALL,' ',Fore.CYAN+'^'+Style.RESET_ALL]]
        self.__bul_shape='~'
        self.__time=180
        self.score=0
        self.__shield_time=30
        # self.tp=0
        self.__shield=0
        self.__screen_time=1
        self.__count=7
        self.__powerup_time = 4
        self.__power_up =1
        self.__bullets=[]
        self.__bul_cnt=0
        self.__verserion_life=18
        self.__lives=5
        self.__tm=1
    def remove_mandalorian(self,matrix,back):
        for i in range(3):
            for j in range(3):
                back[self.__firstco+i][self.__secondco+j]=' '
                matrix[self.__firstco+i][self.__secondco+j]=' '
    
    def check_powerup(self,matrix,back):
        for i in range(3):
            for j in range(3):
                if back[self.__firstco+i][self.__secondco+j] == 'p':
                    self.__power_up=2
                    back[self.__firstco+i][self.__secondco+j]=' '        

    def check_coins(self,matrix,back):
        self.check_powerup(matrix,back)
        for i in range(3):
            for j in range(3):
                if back[self.__firstco+i][self.__secondco+j] == 'm':
                    self.score = self.score+1
                    back[self.__firstco+i][self.__secondco+j]=' '  


    def add_mandalorian(self,firstco,secondco,matrix,back,start):
        self.__firstco=firstco
        self.__secondco=secondco
        # self.__shield_time=0
        # self.__shield=1
        for i in  range(3):
            for j in range(3):
                back[firstco+i][secondco+j]='c'
                if(self.__shield==0):
                    matrix[firstco+i][secondco+j]=self.__shape[i][j]
                else:
                    matrix[firstco+i][secondco+j]=self.__shape1[i][j]
                
                self.check_coins(matrix,back)
                # self.check_collision(matrix,back,start)
    def fire_bullet(self,matrix,back):
        temp=[]
        temp.append(self.__firstco)
        temp.append(self.__secondco+3)
        temp.append(1)
        temp.append(1)
        self.__bullets.append(temp)
        back[self.__firstco][self.__secondco+3]="d"
        matrix[self.__firstco][self.__secondco+3]=self.__bul_shape
        self.__bul_cnt= self.__bul_cnt+1

    def bullet_collision(self,matrix,back,store):
        for i in self.__bullets:
            if i[2]==1:
                fco=i[0]
                sco=i[1]
                # print(str(fco)+',,,,,,,'+str(sco))
                if(back[fco][sco]=='b'):
                    i[2]=0
                    self.remove_beam(fco,sco,matrix,back,store)
                    return
                if(back[fco][sco]=='l'):
                    i[2]=0
                    self.__verserion_life = self.__verserion_life-1
                    self.score = self.score+10
                if(back[fco][sco]==' '):
                    i[3]=1 
                    back[i[0]][i[1]]='d'
                    matrix[i[0]][i[1]]=self.__bul_shape               

    def remove_bullet(self,i,matrix,back):
        self.__bullets[i][2]=0
        self.__bullets[i][3]=0
        back[self.__bullets[i][0]][self.__bullets[i][1]]=' '
        matrix[self.__bullets[i][0]][self.__bullets[i][1]]=' '

    def get_shield_val(self):
        return self.__shield

    def set_shield_val(self,val):
        self.__shield=val
    
    def set_shield_time(self,val):
        self.__shield_time=val
    
    def get_veserion_life(self):
        # print("lol")
        return self.__verserion_life

    def get_screen_time(self):
        return self.__screen_time

    def set_screen_time(self,val):
        self.__screen_time=val

    def get_powerup_value(self):
        return self.__power_up

    def set_powerup_value(self,val):
        self.__power_up=val

    def get_firstco(self):
        return self.__firstco

    def get_secondco(self):
        return self.__secondco      

    def set_secondco(self,val):
        self.__secondco=val

    def get_life(self):
        return self.__lives

    def set_life(self,val):
        self.__lives=val
    

    def move_bullet(self,matrix,back,store,start):
        for i in range(self.__bul_cnt):
            if(start-2 < self.__bullets[i][1]):
                    self.remove_bullet(i,matrix,back)
            if(self.__bullets[i][2]==1):
                if(start-2 < self.__bullets[i][1]):
                    self.__bullets[i][2]==0
                if( self.__bullets[i][1] > 397):
                    self.__bullets[i][2]==0
                if(self.__bullets[i][2]==1):
                    if(self.__bullets[i][3]==1):
                        back[self.__bullets[i][0]][self.__bullets[i][1]]=' '
                        matrix[self.__bullets[i][0]][self.__bullets[i][1]]=' '
                        self.__bullets[i][3]=0
                    self.__bullets[i][1]=self.__bullets[i][1]+1
                    self.bullet_collision(matrix,back,store)
                    # self.__bullets[i][1]=self.__bullets[i][1]+1
                    # self.bullet_collision(matrix,back,store)



    def dec_time(self,matrix,back):
        # self.move_bullet(matrix,back)
        self.__time= self.__time - 1
        if(self.__shield == 1):
            self.__count = self.__count - 1
            self.__shield_time=0
            if self.__count == 0:
                self.__shield=0
                self.__shield_time=30
        elif self.__shield == 0:
            if self.__shield_time > 0 :
                self.__shield_time = self.__shield_time - 1
                self.__count = 10
        if self.__power_up ==2:
            if self.__powerup_time > 0:
                 self.__powerup_time =self.__powerup_time -1
            else :
                self.__power_up = 1
                self.__powerup_time= 4

    def print_the_information(self):
        print('\033[%d;%dH' % (0,0))
        print('lives remaining='+str(self.__lives))
        if(self.__time > 99):
            print('Time remaining='+str(self.__time))
        elif self.__time > 9:
            print('Time remaining=0'+str(self.__time))

        elif(self.__time > 0):
            print('Time remaining=00'+str(self.__time))


        if(self.__time == 0):
            subprocess.call('clear',shell="True")
            print("Time completed")
            quit()

        print('Score='+str(self.score))
        if(self.__shield==0):
            print('shield status : inactive')
        else:
            print('shield status :   active')
        if(self.__shield_time >9):
            print("shield time remaining:="+str(self.__shield_time))
        else:
            print("shield time remaining:=0"+str(self.__shield_time))
        if(self.__verserion_life >99):
            print("Dragon power="+str(self.__verserion_life))
        elif self.__verserion_life > 9:
            print("Dragon power=0"+str(self.__verserion_life))
        elif self.__verserion_life >0:
            print("Dragon power=00"+str(self.__verserion_life))


    def remove_beam(self,firstco,secondco,matrix,back,store):
        like=store[firstco][secondco][0]
        fco=store[firstco][secondco][1]
        sco=store[firstco][secondco][2]
        if(like==1):
            for k in range(6):
                for l in range(6):
                    matrix[fco+k][sco+l]=' '
                    back[fco+k][sco+l]=' '

        if(like==2):
            for l in range(5):
                matrix[fco][sco+l]=' '
                back[fco][sco+l]=' '


        if(like==3):
            for l in range(5):
                matrix[fco+l][sco]=' '
                back[fco+l][sco]=' '

          
    def check_collision(self,matrix,back,start,store):
        if self.__shield==0:  
            for i in range(3):
                for j in range(3):
                    if back[self.__firstco+i][self.__secondco+j] == 'b':
                        if self.__lives > 0:
                            self.__lives= self.__lives-1
                            self.__shield=1
                            self.__shield_time=0
                            self.__count=3
                            self.add_mandalorian(31,start,matrix,back,start)
                        if self.__lives==0:
                            print('you lost :(\n')
                            quit()
        if self.__shield==1:
            for i in range(3):
                for j in range(3):
                    if back[self.__firstco+i][self.__secondco+j] == 'b':
                        self.remove_beam(self.__firstco+i,self.__secondco+j,matrix,back,store)
                        return 



    def move_mandalorian(self,matrix,start,back,store):
        ''' Moves mandalorian'''
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''
        inp=user_input()    
        if inp=='q':
            quit()
        if inp=='d' and self.__secondco+3 < start+110:
            self.remove_mandalorian(matrix,back)
            self.__secondco=self.__secondco+(1*self.__power_up)
        if inp=='a' and self.__secondco > start:
            self.remove_mandalorian(matrix,back)
            self.__secondco=self.__secondco-(1*self.__power_up)
        if inp=='w' and self.__firstco > 1:
            self.remove_mandalorian(matrix,back)
            self.__firstco=self.__firstco-(1*self.__power_up)
        if self.__firstco==0:
            self.__firstco=1
        if self.__secondco<start+1:
            self.__secondco=start
        if self.__secondco>start+107:
            self.__secondco=start+108
        
        self.check_collision(matrix,back,start,store)
        self.add_mandalorian(self.__firstco,self.__secondco,matrix,back,start)
        if self.__firstco==31:
                self.__tm=1
        if inp!='w' and self.__firstco<31 :
            self.remove_mandalorian(matrix,back)
            self.__firstco=self.__firstco+1*self.__tm
            self.__tm=self.__tm+1
            if self.__tm > 3:
                self.__tm=3
            if self.__firstco >31:
                self.__firstco=31
            self.check_collision(matrix,back,start,store)
            self.add_mandalorian(self.__firstco,self.__secondco,matrix,back,start)
        if inp!='a' and inp!='d':
            sco=Magnet.check_field(self.__firstco,self.__secondco,start+110)
            self.remove_mandalorian(matrix,back)
            self.__secondco=sco
            if self.__firstco==0:
                self.__firstco=1
            if self.__secondco<start+2:
                self.__secondco=start
            if self.__secondco > start+106:
                self.__secondco=start+106
            self.check_collision(matrix,back,start,store)
            self.add_mandalorian(self.__firstco,self.__secondco,matrix,back,start)
        if inp==' ':
            if(self.__shield_time == 0):
                self.__shield=1

        if inp=="b":
            self.fire_bullet(matrix,back)