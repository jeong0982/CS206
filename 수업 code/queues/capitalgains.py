
from listqueue import Queue

class Shares():
  def __init__(self, number, cost):
    self.number = number
    self.cost = cost
  
Q = Queue()
  
def buy(number, cost):
  print("Buying %d shares at KRW%d per share" % (number, cost))
  Q.enqueue(Shares(number, cost))
  
def sell(total, cost):
  print("Selling %d shares at KRW%d per share" % (total, cost))
  number = total
  while number > 0:
    oldest = Q.front()
    if number < oldest.number:
      print("%d shares were bought for KRW%d so profit is KRW%d" %
            (number, oldest.cost, number * (cost - oldest.cost)))
      oldest.number -= number
      number = 0
    else:
      print("%d shares were bought for KRW%d so profit is KRW%d" %
            (oldest.number, oldest.cost, oldest.number * (cost - oldest.cost)))
      number -= oldest.number
      Q.dequeue()

buy(10, 20000)
buy(5, 21000)
buy(20, 19000)
sell(5, 23000)
sell(12, 22000)
buy(10, 21000)
sell(28, 22000)

