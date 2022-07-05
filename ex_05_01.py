# ex_05_01
# write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect thier mistake using 'try' and 'except' and print an error message and skip to the next number.
count = 0
sum = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == "done" :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid input')
        continue
    #print(fval)
    count = count + 1
    sum = sum + fval

#print('All Done!')
print(sum, count, sum/count)