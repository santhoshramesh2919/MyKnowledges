class stack:
  def __init__(self):
    self.l=[]
  def isempty(self,l):
    if len(self.l)==0:
      return True
    else:
      return False
  def push(self,data):
    self.l.insert(len(self.l),data)
    print(self.l)
  def pop(self):
    if(self.isempty(self.l)):
      print("Stack Empty")
    else:
      self.l.remove(self.l[len(self.l)-1])
      print(self.l)
s=stack()
s.push(20)
s.push(30)
s.push(32)
s.pop()
s.pop()
s.pop()
s.pop()
