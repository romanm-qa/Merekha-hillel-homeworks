# Вложенные циклы (nested loops).
# На каждой итерации внешнего цикла внутренний цикл выполняется полностью.
for i in range(3):
    print(f"Outer loop: {i}")

    for j in range(2):
        print(f"    Inner loop: {j}")

    print()