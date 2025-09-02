'''Saitama'''

def main():
    '''DocString'''
    day = 0

    g_push_up = int(input())
    g_sit_up = int(input())
    g_squat = int(input())
    g_run = int(input())
    push_up = int(input())
    sit_up = int(input())
    run = int(input())
    squat = int(input())
    c_push_up , c_sit_up , c_run , c_squat = 0 , 0 , 0 , 0
    
    while c_push_up < g_push_up or c_sit_up < g_sit_up or c_squat < g_squat or c_run < g_run:
        day += 1
        if c_push_up < g_push_up:
            c_push_up += push_up
        if c_sit_up < g_sit_up:
            c_sit_up += sit_up
        if c_squat < g_squat:
            c_squat += squat
        if c_run < g_run:
            c_run += run

    print(day)

main()
