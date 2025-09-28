import sortedcontainers as sc

strs: sc.SortedKeyList = sc.SortedKeyList(key=str.casefold)
strs.add("AbCd")
strs.add("aBc")
strs.add("abcd")
strs.add("AC")

if __name__ == '__main__':
    print(strs)
