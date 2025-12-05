f = open("day_three/data.txt")

def find_greatest(s_num):
    biggest = s_num[0]
    index = 0
    for i in range(1, len(s_num)):
        if int(s_num[i]) > int(biggest):
            biggest = s_num[i]
            index = i
    return [biggest, index]

joltage = 0

for bank in f:
    s_bank = bank.strip()
    bank = int(bank)
    jol = ''
    num = 0
    index = 0
    to_find = 12
    for i in range(to_find):
        needed = to_find - i - 1
        limit = len(s_bank) - needed
        window = s_bank[index : limit]
        [num, new_index] = find_greatest(window)
        jol += str(num)
        index = index + new_index + 1
    # print(f'{bank} = {jol}')
    joltage += int(jol)
print(f"final joltage = {joltage}")