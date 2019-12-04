import numpy as np
import math

def runProgram(noun, verb, program):
    program = np.copy(program)
    program[1] = noun
    program[2] = verb

    pc = 0
    while True:
        opcode = program[pc]
        if opcode == 1:
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            program[c] = program[a] + program[b]
        if opcode == 2:
            a = int(program[pc+1])
            b = int(program[pc+2])
            c = int(program[pc+3])
            program[c] = program[a] * program[b]
        if opcode == 99:
            break
        pc = pc + 4
    return program[0]
    
data = np.loadtxt('data.txt', delimiter=',')

for n in range(100):
    for v in range(100):
        result = runProgram(n, v, data)
        if result == 19690720:
            print(n * 100 + v)

