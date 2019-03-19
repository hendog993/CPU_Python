from tkinter import Tk, Label, Entry, Button, Text


def main():
    root = Tk()
    program = Program(keys)
    window = GUI(root, program)
    window.root.mainloop()
    return None


# Keys denote the program to be executed.
keys = ["0100",
        "1010",
        "1010",
        "2010",
        "3010",
        "4010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",
        "1010",]


class Program:
    """ Purely for the functionality of the program. Creates an instance
    of the program that contains all functions to be carried out. Instance
    accepts RAM input """

    instructions_dictionary = {
        # All instructions work with 4 digit op codes. The first two digits specify
        # the command. The last two specify the memory address. can be pass.

        "10": "LDA",
        "20": "LDB",
        "30": "LDC",
        "40": "LDD",
        "00": "ADD",
        "00": "SUB",
        "00": "DET",
        "00": "JMP",
        "00": "GRT",
        "00": "LSS",
        "00": "STR",
        "00": "PSH",
        "00": "POP",
        "00": "NOP",
    }

    function_dictionary = {
        "LDA": LDA(),
        "LDB": LDB(),
        "LDC": LDC(),
        "LDD": LDD(),
        "ADD": ADD(),
        "SUB": SUB()
    }


    def __init__(self, RAM):
        self.RAM = RAM
        self.REG = [0, 0, 0, 0]    # Corresponds to registers A, B, C, D.
        self.instruction_register = ''
        self.counter = 0
        self.inst_decoded = ' '


    def fetch(self):
        self.instruction_register = self.RAM[self.counter]
        print("Fetch")



    def decode(self):
        self.inst_decoded = self.instruction_register[0:2]   # loads first two digits
        print("Decode")


    def execute(self):


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
        sum = self.REG[0] = self.REG[1]
        return sum

    def SUB(self):
        diff = self.REG[2] - self.REG[3]
        return diff

    pass


class GUI:
    """ Accepts two inputs. The first is the app/root file from Tk(). The
    second input is the program input that holds all relevant methods and
    instance variables. """


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
        self.execute_button = Button(self.root, text='EXECUTE')
        self.execute_button.grid(row=2, column=1)

        # =================== Initialize =================
        self.initialize_button = Button(self.root, text='INITIALIZE')
        self.initialize_button.grid(row=2, column=0, sticky="W")

        # RAM Section
        self.RAM_Label = Label(self.root,text="RAM").grid(row=0, column=6, sticky='')
        self.R1 = Entry(self.root, width=8).grid(row=1, column=6)
        self.R2 = Entry(self.root, width=8).grid(row=2, column=6)
        self.R3 = Entry(self.root, width=8).grid(row=3, column=6)
        self.R4 = Entry(self.root, width=8).grid(row=4, column=6)
        self.R5 = Entry(self.root, width=8).grid(row=5, column=6)
        self.R6 = Entry(self.root, width=8).grid(row=6, column=6)
        self.R7 = Entry(self.root, width=8).grid(row=7, column=6)
        self.R8 = Entry(self.root, width=8).grid(row=8, column=6)
        self.R9 = Entry(self.root, width=8).grid(row=9, column=6)
        self.R10 = Entry(self.root, width=8).grid(row=10, column=6)
        self.R11 = Entry(self.root, width=8).grid(row=11, column=6)
        self.R12 = Entry(self.root, width=8).grid(row=12, column=6)
        self.R13 = Entry(self.root, width=8).grid(row=13, column=6)
        self.R14 = Entry(self.root, width=8).grid(row=14, column=6)
        self.R15 = Entry(self.root, width=8).grid(row=15, column=6)
        self.R16 = Entry(self.root, width=8).grid(row=16, column=6)

        self.terminal_label = Label(self.root, text='CMD', font='Hevectila 12 bold').grid(row=3, column=0)
        self.terminal = Text(self.root, width=28, height=20, bd=2, relief='sunken')
        self.terminal.grid(row=4, rowspan=10, column = 0, sticky="")


    # Make the GUI update with static methods and run the Process commands at the same time.

    def gui_fetch(self):
        self.program.fetch()
        # value = self.program.RAM[self.program.counter]
        self.instruction_register.insert(0, self.program.RAM[self.program.counter])
        return None


    def gui_decode(self):
        self.program.decode()
        return None


    def gui_execute(self):
        return None


    pass

if __name__ == "__main__":
    main()
