from Room import Room
from Player import Player

class BossRoom(Room):

  INITIAL_STATE = 0
  FIGHT_STATE   = 1
  WIN_STATE     = 2

  BOSS_RECHARGE = 0
  BOSS_SHOOT    = 1

  def isDeadly(self):
    return self.deadly

  def getActionList(self):
    return self.extraActions

  def canGoOut(self):
    return self.canExit

  def act(self, action, player):
    if self.state == self.INITIAL_STATE and action == 'fight':
      self.setState(self.FIGHT_STATE)
      return True
    elif self.state == self.INITIAL_STATE and action == 'goaway':
      self.canExit = True
      return True
    elif self.state == self.FIGHT_STATE and action == 'attack':
      if self.bossState == self.BOSS_RECHARGE:

        if player.gotArtifact():
          self.bossHp = self.bossHp - 2
        else:
          self.bossHp = self.bossHp - 1

        self.flipBossState()
        if self.bossHp == 0:
          self.setState(self.WIN_STATE)
      else:
        self.deadly = True

      return True
    elif self.state == self.FIGHT_STATE and action == 'dodge':
      self.flipBossState()
      return True
    else:
      return False

  def __init__(self, name, text, deadly, artifact):
    self.name = name
    self.initialText = text
    self.artifact = artifact
    self.setState(self.INITIAL_STATE)
    self.bossHp = 20

  def setState(self, state):
    if state == self.INITIAL_STATE:
      self.text = self.initialText
      self.extraActions = ['fight', 'goaway']
      self.canExit = False
      self.deadly = False
    elif state == self.FIGHT_STATE:
      self.extraActions = ['attack', 'dodge']
      self.canExit = False
      self.deadly = False
      self.setBossState(self.BOSS_RECHARGE)
    elif state == self.WIN_STATE:
      self.extraActions = []
      self.canExit = False
      self.deadly = False
      self.text = 'You won the game! Thanks for playing! Game plans by drherobrine.'

    self.state = state

  def setBossState(self, state):
    if state == self.BOSS_RECHARGE:
      self.text = 'Boss has %d HP. He is recharging fireballs. What do you do?' % self.bossHp
    elif state == self.BOSS_SHOOT:
      self.text = 'Boss is shooting you'
    else:
      return

    self.bossState = state

  def flipBossState(self):
    if self.bossState == self.BOSS_RECHARGE:
      self.setBossState(self.BOSS_SHOOT)
    else:
      self.setBossState(self.BOSS_RECHARGE)
