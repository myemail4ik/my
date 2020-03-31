# обучение корабля(не нейронка :(:(---)
class Learn_war_ship(object):
	def __init__(self,massive_ob,massive_ob_point,path_learn_file):
		self.path_learn_file = str(path_learn_file)
		self.massive_ob_point=massive_ob_point
		self.hod_number=1
		self.massive_ob=massive_ob

	def in_game(self,point):
		self.position=point
		self.massive_ob[self.position[0]][self.position[1]]=self.hod_number
		self.massive_ob_point[self.position[0]][self.position[1]]=point
		self.hod_number = self.hod_number + 1

	def numbers_lower(self):
		printMatrix(self.massive_ob)
		self.point=([])
		status=0
		while status <16:
			for j in range(4):
				for g in range(4):
					if self.massive_ob[j][g]==status and self.massive_ob[j][g]!=0:
						self.point.append([j,g])
						self.massive_ob[j][g]=0
			status=status+1

	def pop_massive_function(self):
		line=0
		try:
			file_output = open(self.path_learn_file, 'w')
			for i in self.point:
				if line<3:
					file_output.write(str(convert_to_number(i))+"\n")
					line=line+1
			file_output.close()
		except:
			pass

	def cleaner(self):
		print("Clean...")
		self.massive_ob_point=([[None,None,None,None],
					[None,None,None,None],
					[None,None,None,None],
					[None,None,None,None]])
		self.massive_ob=([[0,0,0,0],
				  [0,0,0,0],
				  [0,0,0,0],
				  [0,0,0,0]])
		self.hod_number = 1
		self.position=[None,None]
		self.point=None
