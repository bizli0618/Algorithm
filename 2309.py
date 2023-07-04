#2309 일곱난쟁이
#브루트포스, 수학?

dwarf = []
height_sum = 0
real = []
for _ in range(9):
    dwarf.append(int(input()))

dwarf.sort()
height_sum = sum(dwarf)
    
for i in range(9):
    tmp1 = height_sum
    tmp1 -= dwarf[i]
    for j in range(9):
        if(j != i):
            tmp2 = tmp1
            tmp2 -= dwarf[j]
            if(tmp2 == 100):
                a, b = dwarf[i], dwarf[j]
                dwarf.remove(a)
                dwarf.remove(b)
                for _ in dwarf:
                    print(_)
                exit()
            else:
                tmp2 = tmp1
            continue

#9C2라서 총 36가지만 해보면 되지만, 굳이 이렇게 해야 했나? 너무 복잡하다.
