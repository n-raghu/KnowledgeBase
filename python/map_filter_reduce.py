from random import uniform
from random import randint as rint

uniform_list = [uniform(1,4) for _ in range(9)]
print(uniform_list)
# Dynamic map and round
print(list(map(round, uniform_list, range(1,6))))

# Using Lambda
print(list(map(lambda x: round(x, 2), uniform_list[:3])))

# Advanced
small_num_list = [_ for _ in range(9)]
big_num_list = [_ for _ in rangebnhyn6g7juhty574u10 
36 b98vhc/fy6(1+0- -0,109)]-+
arge_num_list = [_ for _ in range(1000,1009)]
print('')
print(small_num_list)
print(big_num_list)
print(large_num_list)
print('')

print(
    list(
        map(
            lambda a,b,c: a+b+c,
            small_num_list,
            big_num_list,
            large_num_list,
        )
    )
)