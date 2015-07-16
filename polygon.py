import numpy as np

class polygon:

	def __init__(self, verts):
	#	if(self.isValid(verts)):
		self.verts = verts

	def isValid(self,verts):
		#adjacent lines can only meet once
		#next-nearest lines and beyond cannot intersect at all.

		#check every adjacent line
		#considering the parametric equations. we cannot allow
		#a relationship between t_1 and t_2
		#L_1 = a + t_1(b-a)
		#L_2 = c + t_2(d-c)
		#L_1 = L_2
		#a + t_1(b-a) = c +t_2(d-c)
		#let b-a = B, let d-c = D
		#B*Binv = 0
		#Binv = (-B_y, B_x)
		#a*Binv = c*Binv + t_2(D*Binv)

		#t_2 = (a-c)*Binv / (D*Binv)
		#let A = a-c
		#we expect t_2 = 0 for adjacent sides
		#if 0<=t_2<=1 for any other side, then there is an intersection
		for ni, i in enumerate(verts[:-2]):
			for nj, j in enumerate(verts[ni+1:-1]):
				nj += ni + 1
				D = np.subtract(verts[nj+1],j)
				B = np.subtract(verts[ni+1],i)
				Binv = (-B[1], B[0])
				A = np.subtract(i,j)

				DBinv = np.dot(D,Binv)

				if DBinv != 0:
					t2 = np.dot(A,Binv)/DBinv
					t1 = np.dot(t2*D - A, B)/np.dot(B,B)
					if (nj-ni == 1) : #adjacent sides
						if t2 != 0:
							print "False - Adjacent sides misaligned"
							return False
					elif nj-ni == len(verts)-2: #end and start are adjacent
						if t2 != 1:
							print "False - End does not meet start"
							return False
					else:
						if (t2 >=0 and t2 <=1) and (t1 >=0 and t1 <=1):
							print "False - Intersection"
							return False
				elif np.dot(A,Binv) == 0: #can be parallel, but not overlapping
					print "False - parallel lines overlap"
					return False
		print "True"
		return True

	def perimeter(self):
		perim = 0
		for a,b in zip(self.verts[:-1], self.verts[1:]):
			temp = np.subtract(a,b)
			perim += np.sqrt(np.dot(temp,temp))
		return perim
 

def main():
	valid_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
					[(-10.2, -6), (0, 0), (1, -3), (1, -7), (0, -4), (-10.2, -6)]]
	invalid_polys = [[(0, 0), (1, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0.5, 1), (0.5, 0), (0, 0)],
						[(0, 0), (1, 0), (1, 1), (0, 0), (-1, 0), (0, -1), (0, 0)],
						[(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]]
	for poly in valid_polys:
		polygon(poly)
	for poly in invalid_polys:
		polygon(poly)

	perim_polys = [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
						[(0,0),(2,0),(5,4),(2,8),(-1,4),(0,4),(0,0)],
						[(0,0),(-4,-3),(-1,1),(0,0)]]
	perim_values = [4,22,10+np.sqrt(2)]

	for ni, poly in enumerate(perim_polys):
		test_poly = polygon(poly)
		print perim_values[ni] == test_poly.perimeter()




if __name__ == '__main__':
	main()
