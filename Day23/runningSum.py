l = [1,2,3,4]
run_sum = []
curr_sum = 0


for n in l:
    curr_sum += n
    run_sum.append(curr_sum) 
print(run_sum)
