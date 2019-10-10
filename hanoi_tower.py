def tower(n, start = "1", dest = "2", spare = "3"):
    if n == 1:
        print(f"from {start} move to {dest}")
    else:
        tower(n-1, start, spare, dest)
        tower(1, start, dest, spare)
        tower(n-1, spare, dest, start)


if __name__ == "__main__":
    tower(3)

