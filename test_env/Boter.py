class Boter(object):
		def __init__(self):
				self.gewicht = 500

		def getGewicht(self):
				return self.gewicht
		
		def updateGewicht(self):
				self.gewicht = self.gewicht - 7.5

		def resetGewicht(self):
				self.gewicht = 500
