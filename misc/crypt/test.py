with open("input.txt") as f: inputs = [[list([(ch=='X')-0.5] for ch in f.readline()[:28]) for b in range(28)] for i in range(10)]
print(inputs)