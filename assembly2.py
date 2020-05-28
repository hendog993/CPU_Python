from tkinter import Tk, Label, Entry, Button, Text

def main():
	root = Tk()
	program = Program(keys)
	window = GUI(root, program)
	window.root.mainloop()
	return None


# Keys denote the program to be executed. Global variable
keys = ["1004",
        "2051",
        "3001",
        "4009",
        "4900",
        "9900",
        "1018",
        "1009",
        "1012",
        "1013",
        "1043",
        "1016",
        "1018",
        "1052",
        "1084",
        "1020",
        "2012",
        "1501",
        "1614",
        "6007",
        "4016",
        "1017",
        "1018",
        "1009",
        "1012",
        "1013",
        "1043",
        "1016",
        "1018",
        "1052",
        "3333",
        "1084", ]


class Program:
	""" Purely for the functionality of the program. Creates an instance
	of the program that contains all functions to be carried out. Instance
	accepts RAM input """
	
	instruction_dictionary = {
		# All instructions work with 4 digit op codes. The first two digits specify
		# the command. The last two specify the memory address.
		
		"10": "LDA",
		"20": "LDB",
		"30": "LDC",
		"40": "LDD",
		"25": "ADD",
		"60": "JMP",
		"35": "SUB",
		"12": "GRT",
		"13": "LSS",
		"49": "TLS",
		"99": "RSR"
		
	}
	
	
	def __init__(self, ram):
		self.RAM = ram
		self.REG = [0, 0, 0, 0]  # Corresponds to registers A, B, C, D.
		self.instruction_register = ''
		self.counter = 0
		self.op_1 = ""
		self.op_2 = ""
	
	def fetch(self):
		self.instruction_register = self.RAM[self.counter]
	
	
	def decode(self):
		self.op_1 = self.instruction_register[0:2]  # loads first two digits
		self.op_2 = self.instruction_register[2:4]  # loads second two digits of memory.
	
	
	def execute(self):
		if self.op_1 == "10":
			self.lda()
		elif self.op_1 == "20":
			self.ldb()
		elif self.op_1 == "30":
			self.ldc()
		elif self.op_1 == "40":
			self.ldd()
		elif self.op_1 == "25":
			self.add()
		elif self.op_1 == "35":
			self.sub()
		elif self.op_1 == "60":
			self.jmp()
		elif self.op_1 == "12":
			self.grt()
		elif self.op_1 == "13":
			self.lss()
		elif self.op_1 == "49":
			self.tls()
		elif self.op_1 == "99":
			self.rsr()
		
		
		if self.op_1 != "60":
			self.counter += 1
	
	def lda(self):
		self.REG[0] = int(self.op_2)
	
	def ldb(self):
		self.REG[1] = int(self.op_2)
	
	def ldc(self):
		self.REG[2] = int(self.op_2)
	
	def ldd(self):
		self.REG[3] = int(self.op_2)
	
	def jmp(self):
		self.counter = int(self.op_2)
		pass
	
	def add(self):
		self.RAM[int(self.op_2)] = self.REG[0] + self.REG[1]
	
	def sub(self):
		self.RAM[int(self.op_2)] = self.REG[2] - self.REG[3]
	
	def grt(self):
		self.RAM[int(self.op_2)] = self.REG[0] > self.REG[1]
	
	def lss(self):
		self.RAM[int(self.op_2)] = self.REG[0] < self.REG[1]
	
	def tls(self):
		self.RAM[int(self.op_2)] = self.REG[0] + self.REG[1] + self.REG[2] + self.REG[3]
	
	def rsr(self):
		self.REG[0] = 0
		self.REG[1] = 0
		self.REG[2] = 0
		self.REG[3] = 0





class GUI:
	""" Accepts two inputs. The first is the app/root file from Tk(). The
	second input is the program input that holds all relevant methods and
	instance variables. All gui functions are simply used to display
	the insides of the program. Should only contain gui methods and
	no procedural methods. """
	
	def __init__(self, root, program):
		self.program = program  # Gives the GUI the process instance methods.
		self.root = root
		self.root.geometry("500x700")
		
		# Instruction register section.
		self.instruction_register = Entry(self.root, width=5)
		self.instruction_register.grid(row=0, column=1)
		self.instruction_register_label = Label(self.root, text="INSTRUCTION REGISTER").grid(row=0, column=0)
		
		# Program counter section.
		self.program_counter = Entry(self.root, width=5)
		self.program_counter.grid(row=1, column=1)
		self.program_counter_label = Label(self.root, text="PROGRAM COUNTER").grid(row=1, column=0)
		
		# =================== Fetch ====================
		self.fetch_button = Button(self.root, text='FETCH', command=self.gui_fetch)
		self.fetch_button.grid(row=2, column=0, sticky="")
		
		# =================== Decode ====================
		self.decode_button = Button(self.root, text='DECODE', command=self.gui_decode)
		self.decode_button.grid(row=2, column=0, sticky="E")
		
		# =================== Execute ===================
		self.execute_button = Button(self.root, text='EXECUTE', command=self.gui_execute)
		self.execute_button.grid(row=2, column=1)
		
		# =================== Initialize =================
		self.initialize_button = Button(self.root, text='INITIALIZE', command=self.gui_initialize)
		self.initialize_button.grid(row=2, column=0, sticky="W")
		
		# ================ Program Registers ==============
		self.program_register_label = Label(self.root, text="PROGRAM REGISTER").grid(row=3, column=0, sticky='')
		self.guiR1 = Entry(self.root, width=5)
		self.guiR1.grid(row=4, column=0, sticky="W")
		self.guiR2 = Entry(self.root, width=5)
		self.guiR2.grid(row=4, column=0, sticky='')
		self.guiR3 = Entry(self.root, width=5)
		self.guiR3.grid(row=4, column=0, sticky='E')
		self.guiR4 = Entry(self.root, width=5)
		self.guiR4.grid(row=4, column=1, sticky='')
		
		self.list_of_reg = [self.guiR1, self.guiR2, self.guiR3, self.guiR4]
		
		# RAM Section
		self.RAM_Label = Label(self.root, text="RAM").grid(row=0, column=6, sticky='')
		self.R1 = Entry(self.root, width=8)
		self.R1.grid(row=1, column=6)
		self.R2 = Entry(self.root, width=8)
		self.R2.grid(row=2, column=6)
		self.R3 = Entry(self.root, width=8)
		self.R3.grid(row=3, column=6)
		self.R4 = Entry(self.root, width=8)
		self.R4.grid(row=4, column=6)
		self.R5 = Entry(self.root, width=8)
		self.R5.grid(row=5, column=6)
		self.R6 = Entry(self.root, width=8)
		self.R6.grid(row=6, column=6)
		self.R7 = Entry(self.root, width=8)
		self.R7.grid(row=7, column=6)
		self.R8 = Entry(self.root, width=8)
		self.R8.grid(row=8, column=6)
		self.R9 = Entry(self.root, width=8)
		self.R9.grid(row=9, column=6)
		self.R10 = Entry(self.root, width=8)
		self.R10.grid(row=10, column=6)
		self.R11 = Entry(self.root, width=8)
		self.R11.grid(row=11, column=6)
		self.R12 = Entry(self.root, width=8)
		self.R12.grid(row=12, column=6)
		self.R13 = Entry(self.root, width=8)
		self.R13.grid(row=13, column=6)
		self.R14 = Entry(self.root, width=8)
		self.R14.grid(row=14, column=6)
		self.R15 = Entry(self.root, width=8)
		self.R15.grid(row=15, column=6)
		self.R16 = Entry(self.root, width=8)
		self.R16.grid(row=16, column=6)
		self.R17 = Entry(self.root, width=8)
		self.R17.grid(row=1, column=7)
		self.R18 = Entry(self.root, width=8)
		self.R18.grid(row=2, column=7)
		self.R19 = Entry(self.root, width=8)
		self.R19.grid(row=3, column=7)
		self.R20 = Entry(self.root, width=8)
		self.R20.grid(row=4, column=7)
		self.R21 = Entry(self.root, width=8)
		self.R21.grid(row=5, column=7)
		self.R22 = Entry(self.root, width=8)
		self.R22.grid(row=6, column=7)
		self.R23 = Entry(self.root, width=8)
		self.R23.grid(row=7, column=7)
		self.R24 = Entry(self.root, width=8)
		self.R24.grid(row=8, column=7)
		self.R25 = Entry(self.root, width=8)
		self.R25.grid(row=9, column=7)
		self.R26 = Entry(self.root, width=8)
		self.R26.grid(row=10, column=7)
		self.R27 = Entry(self.root, width=8)
		self.R27.grid(row=11, column=7)
		self.R28 = Entry(self.root, width=8)
		self.R28.grid(row=12, column=7)
		self.R29 = Entry(self.root, width=8)
		self.R29.grid(row=13, column=7)
		self.R30 = Entry(self.root, width=8)
		self.R30.grid(row=14, column=7)
		self.R31 = Entry(self.root, width=8)
		self.R31.grid(row=15, column=7)
		self.R32 = Entry(self.root, width=8)
		self.R32.grid(row=16, column=7)
		
		self.list_of_ram = [self.R1, self.R2, self.R3, self.R4, self.R5, self.R6,
		                    self.R7, self.R8, self.R9, self.R10, self.R11, self.R12,
		                    self.R13, self.R14, self.R15, self.R16, self.R17, self.R18,
		                    self.R19, self.R20, self.R21, self.R22, self.R23, self.R24,
		                    self.R25, self.R26, self.R27, self.R28, self.R29, self.R30,
		                    self.R31, self.R32]
		
		# ================Terminal Section ==================
		self.terminal_label = Label(self.root, text='CMD', font='Hevectila 12 bold').grid(row=5, column=0)
		self.terminal = Text(self.root, width=28, height=20, bd=2, relief='sunken')
		self.terminal.grid(row=6, rowspan=10, column=0, sticky="")
	
	# File menu section: Gives tooltips, etc.
	
	def gui_initialize(self):
		self.program.counter = 0
		self.instruction_register.delete(0, 'end')
		self.instruction_register.insert(0, 0)
		self.program_counter.delete(0, 'end')
		self.program_counter.insert(0, self.program.counter)
		for x, y in enumerate(self.list_of_ram):
			y.delete(0, 'end')
			y.insert(0, self.program.RAM[x])
		for x, y in enumerate(self.list_of_reg):
			self.program.REG[x] = 0
			y.delete(0, 'end')
			y.insert(0, self.program.REG[x])
	
	# self.R1.delete(0, 'end')
	# self.R1.insert(0, self.program.RAM[0])
	# self.program.REG = [2 for x in self.program.REG]
	
	def gui_fetch(self):
		self.instruction_register.delete(0, 'end')
		self.program.fetch()
		# value = self.program.RAM[self.program.counter]
		self.instruction_register.insert(0, self.program.RAM[self.program.counter])
	
	def gui_decode(self):
		# Work with text terminal
		self.program.decode()
		self.terminal.insert('end', [self.program.counter, self.program.instruction_dictionary[self.program.op_1]])
		self.terminal.insert('end', '\n')
	
	def gui_execute(self):
		self.program_counter.delete(0, 'end')
		self.program.execute()
		self.program_counter.insert(0, self.program.counter)
		# Updates the GUI with new registers and new RAM.
		for x, y in enumerate(self.list_of_ram):
			y.delete(0, 'end')
			y.insert(0, self.program.RAM[x])
		for x, y in enumerate(self.list_of_reg):
			y.delete(0, 'end')
			y.insert(0, self.program.REG[x])
	
	pass


if __name__ == "__main__":
	main()
