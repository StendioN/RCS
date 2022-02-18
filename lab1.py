t = [233, 303, 81, 129, 200, 82, 115, 228, 64, 17,
     67, 648, 29, 39, 210, 10, 94, 465, 135, 312,
     606, 698, 15, 764, 32, 45, 54, 13, 116, 24,
     477, 16, 841, 95, 3, 79, 118, 208, 9, 59, 171,
     295, 78, 67, 38, 57, 91, 18, 39, 324, 416,
     270, 114, 25, 675, 287, 374, 119, 227, 5,
     109, 94, 171, 226, 183, 350, 27, 64, 433, 88,
     167, 152, 159, 319, 8, 162, 36, 488, 65, 77,
     307, 522, 140, 65, 355, 482, 180, 29, 342,
     233, 117, 182, 184, 113, 86, 630, 476, 136,
     397, 66]
gamma = 0.62
probability_time = 275
lambda_time = 648
t.sort()
N = len(t)
k = 10
h = (t[-1] - 0) / k

# Середній наробіток до відмови Tср
avg = sum(t) / len(t)
print(f"Середній наробіток до відмови Tср = {avg}")

intervals = [0 + i * h for i in range(k + 1)]
temp = []
temp_1 = []
count = [0 for i in range(k + 1)]
for i in range(len(t)):
    for j in range(len(intervals)):
        if intervals[j - 1] < t[i] <= intervals[j]:
            count[j] += 1
fi = [i / (N * h) for i in count]
pi = [0 for i in range(k + 1)]
adder = 0
for i in range(len(fi)):
    adder += fi[i]
    pi[i] = round(1 - h * adder, 2)

# γ-відсотковий наробіток на відмову Tγ
T_1 = 0
for i in range(len(pi)):
    if pi[i - 1] >= gamma >= pi[i]:
        d_1 = (pi[i] - gamma) / (pi[i] - pi[i - 1])
        T_1 = h - h * d_1
        break
print(f"γ-відсотковий наробіток на відмову Tγ: {T_1}")

# Ймовірність безвідмовної роботи
P_1 = 0
for i in range(len(intervals)):
    if intervals[i - 1] <= probability_time <= intervals[i]:
        P_1 = 1 - (h * sum(fi[0:i:1]) + fi[i] * (probability_time - intervals[i - 1]))
        break
print(f"Ймовірність безвідмовної роботи на час {probability_time}: {P_1}")

# Інтенсивність відмов
P_2 = 0
lambda_1 = 0
for i in range(len(intervals)):
    if intervals[i - 1] <= lambda_time <= intervals[i]:
        P_2 = 1 - (h * sum(fi[0:i:1]) + fi[i] * (lambda_time - intervals[i - 1]))
        lambda_1 = fi[i] / P_2
        break
print(f"Інтенсивність відмов на час {lambda_time}: {lambda_1}")
