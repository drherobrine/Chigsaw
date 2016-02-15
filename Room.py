class Room:

  def isDeadly(self):
    return self.deadly

  def isAccessible(self):
    return

  def getName(self):
    return self.name

  def getText(self):
    return self.text

  def canGoOut(self):
    return True

  def getActionList(self):
    return self.extraActions
  
  def act(self, action):
    return False

  def __init__(self, name, text, deadly):
    self.name = name
    self.deadly = deadly
    self.text = text
    self.extraActions = []
  

