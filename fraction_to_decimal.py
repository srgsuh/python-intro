#https://leetcode.com/problems/fraction-to-recurring-decimal/description/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator in [-1, 1] or numerator == 0:
            return str(numerator * denominator)
        sign = (1 if numerator > 0 else -1) * (1 if denominator > 0 else -1)
        numerator, denominator = abs(numerator), abs(denominator)
        integerPart = str( numerator // denominator)
        dividend = numerator % denominator
        divisor = denominator
        memo = {}
        cycleStart = -1
        ratio = []
        while dividend:
            if dividend in memo:
                cycleStart = memo[dividend]
                break
            memo[dividend] = len(ratio)
            dividend *= 10
            ratio.append(str(dividend // denominator))
            dividend = dividend % denominator
        
        openPar = "(" if cycleStart >= 0 else ""
        closePar = ")" if cycleStart >= 0 else ""
        nonCyclePart = ("".join(ratio[:cycleStart])) if cycleStart >= 0 else "".join(ratio) if len(ratio) else ""
        cyclePart = ("".join(ratio[cycleStart:])) if cycleStart >= 0 else ""
        decimalDot = "." if len(ratio) else ""
        signPart = "-" if sign < 0 else ""
        return signPart + integerPart + decimalDot + nonCyclePart + openPar + cyclePart + closePar