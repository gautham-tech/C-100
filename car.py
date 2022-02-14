class Car(object):
	def __init__(self,model,color,company,speed_limit):
		self.model = model
		self.color = color
		self.company = company
		self.speed_limit = speed_limit
    

bob = Car("Phantom","Black","Rolls Royce",200)


print(bob.color)