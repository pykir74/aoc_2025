f = open("day_three/data.txt")

joltage = 0

for bank in f:
    s_bank = bank.strip()
    bank = int(bank)
    battery_1 = 0
    battery_2 = 0
    for i in range(0, len(s_bank)):
        set = False
        if int(s_bank[i]) > int(battery_1) and i != len(s_bank)-1:
            battery_1 = s_bank[i]
            battery_2 = 0
            set = True
        elif int(s_bank[i]) > int(battery_2) and set == False:
            battery_2 = s_bank[i]
    jol = int(str(battery_1) + str(battery_2))
    joltage += jol
    print(jol)
print(f"final joltage: {joltage}")