from tkinter import Tk, Label, Entry, Button, Text

# TODO add colors to Entries
# TODO fix pep8 style issues
# TODO fix initialize button, make it
# TODO Add program counter pair to terminal
# TODO clear up variable naming ambiguity
# TODO add more functionality to execute statements
# TODO allow program registers to update properly and generally.


def main():
	root = Tk()
	program = Program(keys)
	window = GUI(root, program)
	window.root.mainloop()


# Keys denote the program to be executed.
keys = ["1000",
		"1012",
		"1013",
		"2014",
		"3015",
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
		"1084"]


class Program:
	""" Purely for the functionality of the program. Creates an instance
	of the program that contains all functions to be carried out. Instance
	accepts RAM input """

	instruction_dictionary = {
		# All instructions work with 4 digit op codes. The first two digits specify
		# the command. The last two specify the memory address. can be pass.

		"10": "LDA",
		"20": "LDB",
		"30": "LDC",
		"40": "LDD",
		"25": "ADD",
		"27": "SUB",
		"56": "DET",
		"60": "JMP",
		"15": "GRT",
		"16": "LSS",
		"51": "STR",
		"18": "PSH",
		"19": "POP",
		"00": "NOP",
	}

	def __init__(self, RAM):
		self.RAM = RAM
		self.REG = [0, 0, 0, 0]  # Corresponds to registers A, B, C, D.
		self.instruction_register = ''
		self.counter = 0
		self.op_1 = ""
		self.op_2 = ""

	def fetch(self):
		self.instruction_register = self.RAM[self.counter]
		print("Fetch")

	def decode(self):
		self.op_1 = self.instruction_register[0:2]  # loads first two digits
		self.op_2 = self.instruction_register[2:4]
		print("Decode")

	def execute(self):
		function_dictionary = {
			"LDA": self.LDA(),
			"LDB": self.LDB(),
			"LDC": self.LDC(),
			"LDD": self.LDD(),
			"ADD": self.ADD(),
			"SUB": self.SUB()
		}

		function_dictionary[self.instruction_dictionary[self.op_1]]
		self.counter += 1
		print("Execute")

	def LDA(self):
		self.REG[0] = int(self.instruction_register)

	def LDB(self):
		self.REG[1] = int(self.instruction_register)

	def LDC(self):
		self.REG[2] = int(self.instruction_register)

	def LDD(self):
		self.REG[3] = int(self.instruction_register)

	def ADD(self):
		# Adds the values of registeres A and B and stores in M.A. Opcode 2
		self.RAM[int(self.op_2)] = self.REG[0] = self.REG[1]

	def SUB(self):
		# Subtracts the values of registers c and d, stores in M.A. Opcode 2
		self.RAM[int(self.op_2)] = self.REG[2] - self.REG[3]

	pass


class GUI:
	""" Accepts two inputs. The first is the app/root file from Tk(). The
	second input is the program input that holds all relevant methods and
	instance variables. All gui functions are simply used to display
	the insides of the program. Should only contain gui methods and
	no procedural methods. """

	def __init__(self, root, program):
		self.program = program  # Gives the GUI the process instance methods.
		self.root = root
		self.root.geometry("400x800")

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

		# ================Terminal Section ==================
		self.terminal_label = Label(self.root, text='CMD', font='Hevectila 12 bold').grid(row=5, column=0)
		self.terminal = Text(self.root, width=28, height=20, bd=2, relief='sunken')
		self.terminal.grid(row=6, rowspan=10, column=0, sticky="")

		self.list_of_ram = [self.R1, self.R2, self.R3, self.R4, self.R5, self.R6,
							self.R7, self.R8, self.R9, self.R10, self.R11, self.R12,
							self.R13, self.R14, self.R15, self.R16]

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
		self.terminal.insert('end', self.program.instruction_dictionary[self.program.op_1])
		self.terminal.insert('end', '\n')

	def gui_execute(self):
		self.program_counter.delete(0, 'end')
		self.program.execute()
		self.program_counter.insert(0, self.program.counter)

	pass


if __name__ == "__main__":
	main()
