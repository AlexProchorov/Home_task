def func():
    result=0
    try:
       while True:
        for n in map(int, input().split()):
            result += n
            print(result)
    except ValueError:
        print(f' {result} последнее значение')



func()
