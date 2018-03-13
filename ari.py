def rec_sum(a_1, d, n):
if n == 0:
return 0
return a_1 + rec_sum(a_1 + d, d, n-1)
print rec_sum(2, 2, 4)
