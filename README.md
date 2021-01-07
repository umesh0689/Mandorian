# JETPACK JOYRIDE 

## Requirements    
* python3 

        sudo apt install python3
* colorama library 
        
        sudo apt install python-pip
        pip3 install colorama

## Running

    python3 main.py

## Oops concepts implementation

__Inheritance__ :
         
    Dragon(enemy) and Mandalorian inherit from the same class 'Person'
    Magnet,Powerups,Beams inherit from the same class 'Objects'
    
__Polymorphism__ :

    add function in dragon overwrites the add function in its parent class    

__Encapsulation__ :
         
    Classes and objects are used for powerups,magnets,beams

__Abstraction__ :
        
    Intuitive functions like Manget.place(),Beams.create_beams() Dragon.add() mandalorian.move_right() are used  
    


## Movement 
| Key | Function |
| -- | -- |
|a | move left|
|d| move right|
|w | move up|
|b | fire bullets|
|q | exit game|
|[space] | activate shield|
* Player cam move within the window, but can't go ouside the window


## Background
* Background keeps moving each second. The Mandalorian cannot go above sky or below ground.
* There are coins which are present and can be collected to increase the score.

## Obstacles
__Fire beams__ :
            
* Fire beams appear in the scenery which may be in horizantal, vertical or tilted shape. 
* Player looses a life when he touches one of these.
    
__Magnet__ : 
            
* A magnet appears randomly which attracts the player towards it along x-axis.

## The Boss Enemy

* The boss enemy(Dragon) appears at the end of the game. 
* The boss enemy is viserion(a dragon) which has   18 lives.
* The dragon adjusts it's position according to the player i.e; 
* It follows the player along the y-direction. 
* It looses it's lives when the player shoots bullets at it
* Player scores 10 points for each bullet fired at it. 

## Score and lives

* Score is calculated taking into account of no. of coins collected and no.of bullets fired at the boss enemy.
* Score, Time remaining, Lives of player left, Lives of boss enemy left and The state of shield are displayed at the top of the screen. 
* The score calculation is as follows :

 
| Type | Score |
| -- | -- |
| Coin | 1 |
| Bsoss | 10 |

## Power-Ups

__Speed Boost__ : 
* When this power-up is collected, the speed of the gameplay is increased.

__Shield__ : 
* The shield is activated by pressing space bar.
* It remains activated for 7 seconds and becomes available after 30 sec

## Bonus 

__Colours__ :
* Different colours are used for different objects.
* Colours are implemented using colorama library

## Additional libraries used
* Colorama