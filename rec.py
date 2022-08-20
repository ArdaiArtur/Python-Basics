def recursive_method(n):
    if n == 1:
        return 1 
    else:
        return n * recursive_method(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120
num = int(input('enter num '))
print(recursive_method(num))






 pythonCopydef fact(n):
    """Recursive function to find factorial"""
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))
a = 6
print("Factorial of", a, "=", fact(a))


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


