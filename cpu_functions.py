from tkinter import Tk, Label, Entry, Button, Text

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
        "1010", ]


def main():
    root = Tk()
    master = Program(keys)
    GUI(root, master)
    root.geometry("450x760")
    root.mainloop()


class Program:
    instructions_dictionary = {
        "1010": "LDA",
        "2030": "LDB",
        "3043": "LDC",
        "4098": "LDD",
        "0005": "ADD",
        "0006": "SUB",
        "0003": "DET",
        "0007": "JMP",
        "0008": "GRT",
        "0009": "LSS",
        "0010": "STR",
        "0011": "PSH",
        "0012": "POP",
        "0013": "NOP",
    }

    # Programmable Section
    def __init__(self, RAM):
        self.RAM = RAM
        self.REG = [0, 0, 0, 0]
        self.instruction_register = ''
        self.counter = 0

    def initialize(self):
        return 0

    def fetch(self):
        print("Fetch")
        return None

    def decode(self):
        # Works with a four digit op code: seperated into two two-digit commands
        print("Decode")

    def execute(self):
        print("Execute")
        # Calls the appropriate function to execute from
        # the function dictionary. Stores the value in memory.
        self.counter += 1
        print(self.counter)
        return

    def LDA(self):
        self.REG[0] = self.instruction_register

    def LDB(self):
        self.REG[1] = self.instruction_register

    def LDC(self):
        self.REG[2] = self.instruction_register

    def LDD(self):
        self.REG[3] = self.instruction_register

    def ADD(self):
        sum = self.REG[0] = self.REG[1]

    pass


class GUI:
    """ Pass the root/master variable into  master/root = Tk(), and program = the
        instance created from the program class. """

    def __init__(self, app, program):
        self.program = program  # Gives the GUI the process instance methods.

        # Instruction register section.
        self.instruction_register = Entry(app, width=5, state='readonly')
        self.instruction_register.grid(row=0, column=1)
        self.instruction_register_label = Label(app, text="INSTRUCTION REGISTER").grid(row=0, column=0)

        # Program counter section.
        self.program_counter = Entry(app, width=5, state='readonly')
        self.program_counter.grid(row=1, column=1)
        self.program_counter_label = Label(app, text="PROGRAM COUNTER").grid(row=1, column=0)

        # ========= Fetch ==========
        self.fetch_button = Button(app, text='FETCH')
        self.fetch_button.grid(row=2, column=0, sticky="")

        # ========= Decode ==========
        self.decode_button = Button(app, text='DECODE', command=GUI.sup)
        self.decode_button.grid(row=2, column=0, sticky="E")

        # ========= Execute =========
        self.execute_button = Button(app, text='EXECUTE')
        self.execute_button.grid(row=2, column=1)

        # ========= Initialize =======
        self.initialize_button = Button(app, text='INITIALIZE')
        self.initialize_button.grid(row=2, column=0, sticky="W")

        # RAM Section
        self.RAM_Label = Label(app, text="RAM").grid(row=0, column=6, sticky='')
        self.R1 = Entry(app, width=8).grid(row=1, column=6)
        self.R2 = Entry(app, width=8).grid(row=2, column=6)
        self.R3 = Entry(app, width=8).grid(row=3, column=6)
        self.R4 = Entry(app, width=8).grid(row=4, column=6)
        self.R5 = Entry(app, width=8).grid(row=5, column=6)
        self.R6 = Entry(app, width=8).grid(row=6, column=6)
        self.R7 = Entry(app, width=8).grid(row=7, column=6)
        self.R8 = Entry(app, width=8).grid(row=8, column=6)
        self.R9 = Entry(app, width=8).grid(row=9, column=6)
        self.R10 = Entry(app, width=8).grid(row=10, column=6)
        self.R11 = Entry(app, width=8).grid(row=11, column=6)
        self.R12 = Entry(app, width=8).grid(row=12, column=6)
        self.R13 = Entry(app, width=8).grid(row=13, column=6)
        self.R14 = Entry(app, width=8).grid(row=14, column=6)
        self.R15 = Entry(app, width=8).grid(row=15, column=6)
        self.R16 = Entry(app, width=8).grid(row=16, column=6)

        self.terminal_label = Label(app, text='CMD', font='Hevectila 12 bold').grid(row=3, column=0)
        self.terminal = Text(app, width=28, height=20, bd=2, relief='sunken')
        self.terminal.grid(row=4, rowspan=10, column = 0, sticky="")


    # Make the GUI update with static methods and run the Process commands at the same time.

    @staticmethod
    def sup():
        print('sup')

if __name__ == "__main__":
    main()
