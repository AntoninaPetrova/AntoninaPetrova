# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

check = True
for X in True, False:
    for Y in True, False:
        for Z in True, False:
            print(f"{X = } {Y = } {Z = }      RESULT: {not(X or Y or Z) == (not X and not Y and not Z)}")