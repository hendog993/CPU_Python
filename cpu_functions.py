# import hencpunew
#
# # TKinter variables
# tkRAM = [M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15]
# tkREG = [R1, R2, R3, R4]

from tkinter import Tk, Label, Entry, Button, Text
class Process():

    count = 0

    # Programmable Section
    RAM = ["0100",
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

    REG = [0,0,0,0]

    instruction_register = ""

    instructions_dictionary = {
        "1010": "LDA",
        "2030": "LDB",
        "3043": "LDC",
        "4098": "LDD",
        "0005": "ADD",
        "0006": "SUB",
        "0006": "DET",
        "0007": "JMP",
        "0008": "GRT",
        "0009": "LSS",
        "0010": "STR",
        "0011": "PSH",
        "0012": "POP",
        "0013": "NOP",
    }

    root = Tk()
    root.geometry("500x600")

    '''================ Tkinter Section ================== '''
    Label(root, text="REGISTERS").grid(row=0, column=0, sticky="")
    R1 = Entry(root, width=8, bg="green")
    R1.grid(row=1, column=0, sticky="W")
    R2 = Entry(root, width=8, bg="green")
    R2.grid(row=1, column=0, sticky="E")
    R3 = Entry(root, width=8, bg="green")
    R3.grid(row=2, column=0, sticky="W")
    R4 = Entry(root, width=8, bg="green")
    R4.grid(row=2, column=0, sticky="E")

    # 8 byte Memory Module using unique blocks.
    Label(root, text="RAM").grid(row=0, column=3, sticky="")
    M0 = Entry(root, width=10, bg="#FFFFCC")
    M0.grid(row=1, column=3)
    M1 = Entry(root, width=10, bg="#FFFFCC")
    M1.grid(row=2, column=3)
    M2 = Entry(root, width=10, bg="lightblue")
    M2.grid(row=3, column=3)
    M3 = Entry(root, width=10, bg="lightblue")
    M3.grid(row=4, column=3)
    M4 = Entry(root, width=10, bg="#FFFFCC")
    M4.grid(row=5, column=3)
    M5 = Entry(root, width=10, bg="#FFFFCC")
    M5.grid(row=6, column=3)
    M6 = Entry(root, width=10, bg="lightblue")
    M6.grid(row=7, column=3)
    M7 = Entry(root, width=10, bg="lightblue")
    M7.grid(row=8, column=3)
    M8 = Entry(root, width=10, bg="#FFFFCC")
    M8.grid(row=9, column=3)
    M9 = Entry(root, width=10, bg="#FFFFCC")
    M9.grid(row=10, column=3)
    M10 = Entry(root, width=10, bg="lightblue")
    M10.grid(row=11, column=3)
    M11 = Entry(root, width=10, bg="lightblue")
    M11.grid(row=12, column=3)
    M12 = Entry(root, width=10, bg="#FFFFCC")
    M12.grid(row=13, column=3)
    M13 = Entry(root, width=10, bg="#FFFFCC")
    M13.grid(row=14, column=3)
    M14 = Entry(root, width=10, bg="lightblue")
    M14.grid(row=15, column=3)
    M15 = Entry(root, width=10, bg="lightblue")
    M15.grid(row=16, column=3)


    # xxxxxxxxxx Button widgets xxxxxxxxxxxxx #
    Fetch = Button(root, width=8, text="FETCH")
    Fetch.grid(row=7, column=0, sticky="W")

    Decode = Button(root, text="DECODE")
    Decode.grid(row=7, column=0, sticky="E")

    Execute = Button(root, text="EXECUTE")
    Execute.grid(row=7, column=1, sticky="W")

    Init = Button(root,text="INITIALIZE")
    Init.grid(row=8, column=0, sticky="W")

    # Instruction Registers label widgets.
    Inst_reg = Label(root, width=8, text=count)
    Inst_reg.grid(row=5, column=1, sticky="NW")
    C2 = Label(root, width=17, text="INSTRUCTION REG: ").grid(row=5, column=0, sticky="W")

    # Program counter widget
    Counter = Label(root, width=8, text=count)
    Counter.grid(row=6, column=1, sticky="NW")
    C2 = Label(root, width=11, text="COUNTER: ").grid(row=6, column=0, sticky="W")

    # Instruction help menu/dictionary widget. Can replace new function.
    Helper = Text(root, width=30, height=15)
    Label(root, text="CMD").grid(row=9, column=0, sticky="")
    Helper.grid(rowspan=10, columnspan=10, sticky="W")


    def initialize(self):
        self.root.mainloop()
        return 0

    def fetch(self):
        instruction =self.RAM[self.count]
        return instruction

    def decode(self):
        # Works with a four digit op code: seperated into two two-digit commands
        instruction = self.fetch()
        instruction_x = instruction[0:2]
        instruction_y = instruction[2:4]
        return instruction_x, instruction_y

    def execute(self):

        # Calls the appropriate function to execute from
        # the function dictionary. Stores the value in memory.
        self.count += 1
        return


    def LDA(self):
        self.REG[0] =
        return




    pass

x = Process()
print(x.decode())
