def problems(N,P):
    time=240
    available_time=time-P
    problems_solved=0
    time_spent=0
    for i in range(1,N+1):
        time_to_solve=5*i
        if time_spent+time_to_solve<=available_time:
            problem_solved+=1
            time_spent+=time_to_solve
        else:
            break
    return problems_solved
N=int(input())
P=int(input())
print(problems(N,P))