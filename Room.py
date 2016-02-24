from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

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

  def hasArtifact(self):
    return self.artifact != None

  def getArtifact(self):
    artifact = self.artifact
    self.artifact = None
    return artifact

  def act(self, action, player):
    return False

  def __init__(self, name, text, deadly, artifact):
    self.name = name
    self.deadly = deadly
    self.text = text
    self.artifact = artifact
    self.extraActions = []
