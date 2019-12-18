import numpy as np
import math

def runProgram(inputs , program):
    program = np.copy(program)
    inIdx = 0
    outIdx = 0
    outputs = []

    pc = 0
    while True:
        ropcode = int(program[pc])
        m3 = int((ropcode % 100_000) / 10_000)
        m2 = int((ropcode %  10_000) /  1_000)
        m1 = int((ropcode %   1_000) /    100)
        opcode = int(ropcode % 100)
        if opcode == 1:
            print(f"ADD {ropcode}: ", end="")
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = program[a]
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ", end="")
                b = program[b]
            else: 
                print(f"{b} ", end="")
            print(f"[{c}] ")
            program[c] = a + b
            pc += 4
        if opcode == 2:
            print(f"MUL {ropcode}: ", end="")
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = program[a]
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ", end="")
                b = program[b]
            else: 
                print(f"{b} ", end="")
            print(f"[{c}] ")
            program[c] = a * b
            pc += 4
        if opcode == 3:
            a = int(program[pc+1])
            print(f"INP {ropcode}: [{a}] <= {inputs[inIdx]}")
            program[a] = inputs[inIdx]
            inIdx += 1
            pc += 2
        if opcode == 4:
            a = int(program[pc+1])
            print(f"OUT {ropcode}: [{a}] ")
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = int(program[a])
            else:
                print(f"{a} ", end="")
            outputs.append(a)
            pc += 2
            print(outputs)
        if opcode == 99:
            break

    return outputs
    
data = np.loadtxt('data.txt', delimiter=',')

result = runProgram([1], data)

print(result)

