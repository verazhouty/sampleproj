import re #to search Each number (operand) should only contain digits

def arithmetic_arranger(problems, display=False):
#First, define all error message situations:

  #If there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
  if len(problems)>5:
    return "Error: Too many problems."


  #note:try enumerate later

  line1=line2=line3=line4=""
  space4="    "
  for problem in problems:
    first=problem.split(" ")[0]
    op=problem.split(" ")[1]
    second=problem.split(" ")[2]
    if op not in "-+":
      return "Error: Operator must be '+' or '-'."
    #Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: Error: Operator must be '+' or '-'.
    if (re.search("[^\s0-9.+-]",problem)):
      return "Error: Numbers must only contain digits."
    #Each number (operand) should only contain digits. Otherwise, the function will return: Error: Numbers must only contain digits.
    if len(first) >4 or len(second)>4:
      return "Error: Numbers cannot be more than four digits."
  #Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: Error: Numbers cannot be more than four digits.
    res = ""
    #do the math
    if op == "+":
      res= str(int(first)+int(second)) #need to turn this into string
    elif op == "-":
      res= str(int(first)-int(second))
    
    #the first and second should be right-aligned
    # fill in the space:
    
    space = max(len(first), len(second))+2 #more space
    top = first.rjust(space)
    middle = op + second.rjust(space-1)# at least one space between op and second number

    #There should be dashes at the bottom of each problem
    dash =""
    for ds in range(space):
      dash += "-"# dash accordingly 
    #There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand
    bottom = str(res).rjust(space)

    if problem != problems[-1]:#four spaces between each problem.
      line1 += top + space4
      line2 += middle + space4
      line3 += dash + space4
      line4 += bottom + space4
    else:
      line1 += top
      line2 += middle
      line3 += dash
      line4 += bottom
      
  if display:
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  return line1 + "\n" + line2 + "\n" + line3




