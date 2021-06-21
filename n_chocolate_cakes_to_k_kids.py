"""
3 bowls 6 kids

[3, 2, 1]
-> [1,1,1,1,1,1]

calories : each intake ^2

[19], 4
[5,5,5,4]

20 bowls, 40 kids


10
3
3 3 4

8 
3
3 3 2

19
4
4 4 4 4

"""
def k_kids_distribute(n_bowls:list, k_kids:int):
    total_cakes = sum(n_bowls)
    if total_cakes % k_kids == 0:
        return (total_cakes // k_kids)**2 * k_kids
    
    else:
        each, mod = divmod(total_cakes, k_kids)
        return (each+1)**2 * mod + each**2 * (k_kids-mod)


print(k_kids_distribute([3,2,1],6)) # 6
print(k_kids_distribute([19],4)) # 19

