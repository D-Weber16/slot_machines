#number of starting quarters
quarters = int(input())
#number of times machines have been played since last payout
mach_one = int(input())
mach_two = int(input())
mach_three = int(input())
#machine to be played next
next_machine = 0
#total number of times played
total_plays = 0


while quarters >= 1:
    quarters -= 1
    
    if next_machine == 0:
        mach_one += 1
        if mach_one == 35:
            mach_one = 0
            quarters += 30
    elif next_machine == 1:
        mach_two += 1
        if mach_two == 100:
            mach_two = 0
            quarters += 60
    elif next_machine == 2:
        mach_three += 1
        if mach_three == 10:
            mach_three = 0
            quarters += 9
    total_plays += 1
    next_machine += 1
    if next_machine == 3:
        next_machine = 0

print(f"Martha plays {total_plays} times before going broke.")