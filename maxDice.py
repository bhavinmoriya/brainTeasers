import random

trials = 1_000_000
s = sum(max(random.randint(1, 6), random.randint(1, 6)) for _ in range(trials))
print(s / trials)           # ≈ 4.472
