numbers: list[int] = [30, 20, 50, 3]

def getNumbersRange(arr: list[int], min: int, max: int) -> list[int]:
    res: list[int] = []
    for v in arr:
        if (min <= v <= max):
            res.append(v)
    return res
            
    

if __name__ == '__main__':
    print(numbers)
    print(getNumbersRange(numbers, 25, 35))