def collatz_sequence(num): 
    sequence = []
    while True:
        sequence.append(num)
        if (num == 1):
            return sequence
        elif num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

chain_num = 999999
current_best = 0
longest_chain_num = 0

for i in range(1, chain_num):
    sequence = collatz_sequence(i)
    if len(sequence) > current_best:
        current_best = len(sequence)
        longest_chain_num = i

print(longest_chain_num)