def generate_abcd_triangle(n):
    """
    Generates a triangle pattern of letters like:
    A
    A B
    A B C
    ...
    """
    for i in range(1, n): 
        for j in range(i):
            print(chr(97 + j), end=' ') 
        print()
        
if __name__ == "__main__":
    rows = input("Enter number of rows: ")
    generate_abcd_triangle(rows)
