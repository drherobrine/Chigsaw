from Room import *
from BossRoom import *

name = raw_input('Whats your name? ') 

print 'Welcome to Chigsaw, ' + name + '.'
print 'Sorry for no graphics, its my first game after all=)'


rooms = [[0 for x in range(3)] for x in range(3)]

rooms[0][0] = Room('Room 0.0','You must have used cheats!', False)
rooms[0][1] = Room('Spiky Wheely Room', 'You were killed by rolling spiked wheels. R.I.P.', True)
rooms[0][2] = Room('Room 0.2', 'This room is still kinda in development.', False)
rooms[1][0] = Room('Bear Room', 'You were eaten by a bear. R.I.P.', True)
rooms[1][1] = Room('Start Room', 'This is the room you start in.', False)
rooms[1][2] = Room('Room 1.2', 'This room is still kinda in development.', False)
rooms[2][0] = BossRoom('Boss Room', 'Kill the boss and win the game!', False)
rooms[2][1] = Room('Room 2.1', 'The right is the right way to go!', False)
rooms[2][2] = Room('Room 2.2', 'This room is still kinda in development.', False)

x = 1
y = 1 

dead = 0
mandatoryActions = ['quit']
actionList = ['forward', 'back', 'left', 'right']

while not dead:
  print ' = = = = = = = = = = = = = = = = = = = = = = = = = = = = = '
  print 'Current room: ' + rooms[x][y].getName()
  print rooms[x][y].getText()
  print ''
  
  tmpActionList = mandatoryActions

  if rooms[x][y].canGoOut():
    tmpActionList = tmpActionList + actionList + rooms[x][y].getActionList()
  else:
    tmpActionList = tmpActionList + rooms[x][y].getActionList()


  dead = rooms[x][y].isDeadly()

  if dead:
    continue

  action = raw_input('Type your action (%s): ' % ', '.join(tmpActionList))

  actionProcessed = rooms[x][y].act(action)
  
  dead = rooms[x][y].isDeadly()

  if not actionProcessed and rooms[x][y].canGoOut():
    if action == "forward":
      if y > 0:
        y = y-1
        actionProcessed = True
    elif action == "left":
      if x > 0:
        x = x-1
        actionProcessed = True
    elif action == "right":
      if x < 2:
        x = x+1
        actionProcessed = True
    elif action == "back": 
      if y < 2:
        y = y+1
        actionProcessed = True

  if action == "quit":
    dead = True
    actionProcessed = True
    continue

  if not actionProcessed:
   print 'Sorry, I did not get you.'
  
print 'Game over!'
