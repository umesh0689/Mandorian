from scenery import Scenery
from background import Background
import subprocess as sp
from mandalorian import Mandalorian
from alarmexception import AlarmException
from getinp import _getChUnix
from beams import Beams
from magnet import Magnet
import time
from dragon import Dragon
sp.call('clear',shell='True')
start=0
background=Background()
background.create_matrix()
background.create_store()
scenery=Scenery()
matrix=background.get_matrix()
back=background.get_back()
store=background.get_store()
scenery.creating_sky(matrix,back)
scenery.creating_land(matrix,back)
scenery.create_coins(matrix,back)
beams=Beams()
beams.get_beams()
beams.creating_objects()
beams.create_beams(matrix,back,store)
magnet=Magnet()
magnet.creating_mag_shape()
magnet.creating_magnet(matrix,back)
magnet.place_mag(matrix,back)
mandalorian=Mandalorian(31,0)
# mandalorian.__shield=1
# mandalorian.__shield_time=0
mandalorian.set_shield_val(1)
mandalorian.set_shield_time(0)
mandalorian.add_mandalorian(31,start,matrix,back,start) #need to add start
mandalorian.check_coins(matrix,back)
mandalorian.print_the_information()
dragon=Dragon(20,355)
dragon.create_dragon(20,355)
dragon.add(matrix,back)
background.printing_the_matrix(start)
starting=time.time()
s_time=time.time()
d_time=time.time()
b_time=time.time()
while True:
    magnet.place_mag(matrix,back)
    print('\033[%d;%dH' % (0,0))
    mandalorian.move_mandalorian(matrix,start,back,store)
    screen_time=mandalorian.get_screen_time()
    if screen_time == 0:
        mandalorian.set_screen_time(1)
        if start + 110 < 399:
            start= start+1
            secondco=mandalorian.get_secondco()
        if secondco < start:
            mandalorian.remove_mandalorian(matrix,back)
            mandalorian.set_secondco(start)
            firstco=mandalorian.get_firstco()
            secondco=mandalorian.get_secondco()
            mandalorian.add_mandalorian(firstco,secondco,matrix,back,start)
    mandalorian.print_the_information()
    background.printing_the_matrix(start)
    if(time.time()- d_time > 0.2):
        firstco=mandalorian.get_firstco()
        secondco=mandalorian.get_secondco()
        dragon.move_dragon(firstco,secondco,matrix,back)
    power_up=mandalorian.get_powerup_value()
    if(time.time()- s_time > (0.5/(2*power_up))):
        s_time=time.time()
        mandalorian.set_screen_time(0)
    if(time.time()-starting > 1):
        starting=time.time()
        mandalorian.dec_time(matrix,back)
    mandalorian.move_bullet(matrix,back,store,start+110)
    if start > 250:
        if(time.time()-b_time > 1.1):
            dragon.fire_dragon_bull(matrix,back)
            b_time=time.time()
        life=mandalorian.get_life()
        life=dragon.move_dra_bullet(matrix,back,store,start,life)
        mandalorian.set_life(life)
    veserion_life=mandalorian.get_veserion_life()
    if(veserion_life == 0):
        sp.call('clear',shell='True')
        print("You Rescued baby yoda")
        quit()
