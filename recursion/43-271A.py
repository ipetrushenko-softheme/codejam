n = int(input())


for year in range(n+1, 9013):
    if len(set(str(year))) == 4:
        print(year)
        break
