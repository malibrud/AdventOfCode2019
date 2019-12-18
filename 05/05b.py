import numpy as np
import math

def runProgram(inputs , program):
    program = np.copy(program)
    inIdx = 0
    outIdx = 0
    outputs = []

    pc = 0
    while True:
        print(f"{pc}: ", end="")
        ropcode = int(program[pc])
        m3 = int((ropcode % 100_000) / 10_000)
        m2 = int((ropcode %  10_000) /  1_000)
        m1 = int((ropcode %   1_000) /    100)
        opcode = int(ropcode % 100)

        # Add
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

        # Multiply
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
        
        # Input
        if opcode == 3:
            a = int(program[pc+1])
            print(f"INP {ropcode}: [{a}] <= {inputs[inIdx]}")
            program[a] = inputs[inIdx]
            inIdx += 1
            pc += 2

        # Output
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

        # Jump-if-true
        if opcode == 5:
            a = int(program[pc+1])
            b = int(program[pc+2])
            print(f"JPT {ropcode}: ", end="")
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = int(program[a])
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ")
                b = int(program[b])
            else:
                print(f"{b} ")
            if a != 0:
                pc = b
            else:
                pc += 3

        # Jump-if-false
        if opcode == 6:
            a = int(program[pc+1])
            b = int(program[pc+2])
            print(f"JPF {ropcode}: ", end="")
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = int(program[a])
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ")
                b = int(program[b])
            else:
                print(f"{b} ")
            if a == 0:
                pc = b
            else:
                pc += 3

        # Less-than
        if opcode == 7:
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            print(f"LT  {ropcode}: ", end="")
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = int(program[a])
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ", end="")
                b = int(program[b])
            else:
                print(f"{b} ", end="")
            print(f"[{c}] ")
            if a < b:
                program[c] = 1
            else:
                program[c] = 0
            pc += 4

        # Equals
        if opcode == 8:
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            print(f"EQ  {ropcode}: ", end="")
            if m1 == 0:
                print(f"[{a}] ", end="")
                a = int(program[a])
            else:
                print(f"{a} ", end="")
            if m2 == 0:
                print(f"[{b}] ", end="")
                b = int(program[b])
            else:
                print(f"{b} ", end="")
            print(f"[{c}] ")
            if a == b:
                program[c] = 1
                print(f"    [{c}] <= 1")
            else:
                program[c] = 0
                print(f"    [{c}] <= 0")
            pc += 4

        # End program
        if opcode == 99:
            print(f"END {ropcode}: ")
            break

    return outputs

TEST = False

if TEST:
    data = np.loadtxt('test.txt', delimiter=',')
    print(data)
    result = runProgram([7], data)
    print(result)
    result = runProgram([8], data)
    print(result)
    result = runProgram([9], data)
    print(result)
else:
    data = np.loadtxt('data.txt', delimiter=',')
    result = runProgram([5], data)
    print(result)

