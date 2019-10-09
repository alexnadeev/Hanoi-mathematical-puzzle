def tower(n, start = "1", dest = "2", spare = "3"):
    if n == 1:
        print(f"from {start} move to {dest}")
    else:
        tower(n-1, start, spare, dest)
        tower(1, start, dest, spare) #print(f"from {start} move to {dest}")
        tower(n-1, spare, dest, start)

tower(3)
