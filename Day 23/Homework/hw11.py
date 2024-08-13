def even_sum(even):
    sum = 0
    for i in range(len(even)):
        if i % 2 == 0:
            sum += even[i]
    print(sum)
even_sum([1,2,3,4,5,6,7,8,9,10])