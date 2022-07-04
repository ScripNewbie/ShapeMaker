"""Shape Maker"""
import os

class MakeTriangle():

	def __init__(self):
		self.Triangle_maker()
		while True:
			try: WIDTH = int(input("Only odd number will work.\nSize if Rectangle: "))
			except ValueError: continue
			WIDTH = WIDTH if WIDTH%2 else WIDTH-1
			os.system("clear")
			self.Triangle_maker((WIDTH+1)//2, WIDTH, WIDTH//2)

	@staticmethod
	def Triangle_maker(HEIGHT=5, WIDTH=9, HALF=4, DESIGN="∆"):
		"""Draw the triangle"""
		for i in range(HEIGHT):
			for k in range(WIDTH):
				if (i+1 == HEIGHT or k == HALF
				or (WIDTH-1)-HALF == k): print(DESIGN, end="")
				else: print(" ", end="" if k+1!=WIDTH else "\n")
			HALF -= 1
		print(f"\nSize: {WIDTH=} {HEIGHT=}\n")

class MakeBox():

	def __init__(self, rows=10, cols=20):
		self.rows, self.cols = rows, cols
		while True:
			os.system("clear")
			self.draw_box(self.rows, self.cols)
			try: self.rows = int(input("Rows: "))
			except ValueError: continue
			try: self.cols = int(input("Cols: "))
			except ValueError: continue

	@staticmethod
	def draw_box(rows=10, cols=20, line=0):
		"""Draw the box"""
		for i in range(rows):
			print("|", end="")
			for _ in range(cols):
				print(" " if line else "-", end="")
			line = 1 if i + 2 != rows else 0
			print("|")
		print(f"size: {rows}x{cols}\n")

if __name__ == "__main__":
	MakeTriangle()
