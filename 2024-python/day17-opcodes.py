from aocd import puzzle
from progressbar import progressbar

lines = puzzle.examples[0].input_data
lines = puzzle.input_data


lines = lines.split("\n")
print(lines)


class Computer:


    def __init__(self, lines):

        (self.uA, self.uB, self.uC) = [int(line.split(": ")[1]) for line in lines[:3]]
        self.program = [int(op) for op in lines[4].split(": ")[1].split(",")]

        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }


    def run(self, break_unless_selfoutputting=False, withA=None):

        self.A = self.uA
        self.B = self.uB
        self.C = self.uC

        if withA:
            self.A = withA

        self.output = []
        self.IP = 0

        while self.IP < len(self.program):
            operation = self.opcodes[self.program[self.IP]]
            operator = self.program[self.IP+1]
            # print(f"IP {self.IP}, op {operation} on {operator}")
            operation(operator)
            self.IP += 2

            if break_unless_selfoutputting:
                if not self.output == self.program[:len(self.output)]:
                    # print(self.output)
                    return False

        return self.output


    def evalcombo(self, cmb):
        match cmb:
            case 4: return self.A
            case 5: return self.B 
            case 6: return self.C
            case _: return cmb

    def adv(self, combo):
        self.A =  self.A // 2**self.evalcombo(combo)

    def bdv(self, combo):
        self.B =  self.A // 2**self.evalcombo(combo)

    def cdv(self, combo):
        self.C =  self.A // 2**self.evalcombo(combo)

    def bxl(self, litop):
        self.B = self.B^litop

    def bxc(self, _):
        self.B = self.B^self.C

    def bst(self, combo):
        x = self.evalcombo(combo) % 8
        self.B = x 

    def out(self, combo):
        outval = self.evalcombo(combo) % 8
        self.output.append(outval)

    def jnz(self, litop):
        if self.A == 0:
            return
        else:
            self.IP = litop-2



computer = Computer(lines)
output = computer.run()
print(",".join([str(i) for i in output]))

for i in progressbar(range(1_000_000_000)):
    output = computer.run(break_unless_selfoutputting=True, withA=i)
    if output == computer.program:
        print(i)
        break