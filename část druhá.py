import matplotlib.pyplot as plt
class DynamicTermination(object):
	def __init__(self, file):
		super(DynamicTermination, self).__init__()
		self.file = file
		self.data = open(self.file, "r")

	def get_data(self):
		self.data = list(self.data.readlines())[3:]
		result = []
		for i in self.data:
			fraction = float(i.strip().split()[0])
			time = float(i.strip().split()[1])
			if fraction < 0.5:
				result.append(fraction)
				if min(result) - max(result) < 0.1:
					print(f"Time: {time}")

if __name__ == '__main__':
	res = DynamicTermination("alpha.water")
	res.get_data()