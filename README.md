## Robotic
#### **Create and use a bot in a python _CLI_**

To use Robotic, enter the command:

* ####  **_If you want to code with the library_**:
`import robotic`

* #### But, we already have a function that let you play and experiment with it.

**_Just use :_**

`from robotic import bot`

In that function you can place walls and move your bot in the 18x18 map:
```Instructions:
  - Enter 'w' to place a wall
  - Enter 'up', 'down', 'left', or 'right' to move the robot
  - Enter 'q' to quit
[['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '#' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' 'R' '#' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '#' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']
 ['~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~' '~']]
Enter command:
```
1. [ ] Soon, there will be a challenge system that gives you a specific patern to replicate

## Commands : 
Create your own Bot:  `nameOfYourBot = Bot(engineStatus{on / off}, positionX, positionY)`

***The bot will only move if the engine is on***

Move your bot: `nameOfYourBot.move(direction{up / down / right / left})`

Place a wall: `nameOfYourBot.place_wall(positionX, positionY)`

Change engine status: `nameOfYourBot.self_engine = 'off'`