def arithmetic_arranger(x,v=False):
    # Create variables to be filled with each problem later
    l1=''
    l2=''
    l3=''
    l4='\n'

    # Validate there are not too many problems
    if len(x)>5:
        return "Error: Too many problems."

    for z in x:
        a = z.split()
        # Begin term validation
        if a[1] != '+' and a[1] != '-': # Check it is addition or subtraction
            return "Error: Operator must be '+' or '-'."
        if not a[0].isdigit() or not a[2].isdigit(): # Check both terms are numbers
            return "Error: Numbers must only contain digits."
        if len(a[0])>4 or len(a[2])>4: # Validate both terms are less than 4 digits
            return 'Error: Numbers cannot be more than four digits.'


        # All inputs are valid

        k = max(len(a[0]),len(a[2])) + 2   # How much to pad each number by

        # Write each line of each problem
        l1 += ('{:>'+str(k)+'}').format(a[0]) + '    '
        l2 += a[1] + (k-1-len(a[2]))*' ' + a[2] + '    '
        l3 += k*'-' + '    '

        if v : # If printing the solution has been requested
            if a[1]=='+':
                l4 += ('{:>'+str(k)+'}').format(int(a[0])+int(a[2])) + '    '
            else:
                l4 += ('{:>'+str(k)+'}').format(int(a[0])-int(a[2])) + '    '
        else: # If the solution should not be printed
          l4 = ''  
          
    # Take all solutions and form them into a readable string
    arranged_problems = l1.rstrip()+'\n'+l2.rstrip()+'\n'+l3.rstrip()+l4.rstrip()
    return arranged_problems

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],True))
            

            

    





