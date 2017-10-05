class Bike(object):
   def __init__(self, price, max_speed):
      self.price = price
      self.max_speed = max_speed
      self.miles = 0
   def displayInfo(self):
      print str(self.price)
      print str(self.max_speed)
      print str(self.miles)
      return self
   def drive(self):
      print 'Driving'
      self.miles += 10
      return self
   def reverse(self):
      print "Reverse"
      if self.miles >= 5:
         self.miles -= 5
      return self

bike1 = Bike(2500, 55)
bike2 = Bike(3500, 75)
bike3 = Bike(4500, 85)

bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayInfo()

bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()


bike11 = Bike(2500, 55)
bike22 = Bike(3500, 75)
bike33 = Bike(4500, 85)

bike11.drive().drive().drive().reverse().displayInfo()

bike22.drive().drive().reverse().reverse().displayInfo()

bike33.reverse().reverse().reverse().displayInfo()

