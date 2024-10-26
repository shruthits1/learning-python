#!/usr/bin/env python3
SPACE = ' '
def convert2digits(n: int) -> str:
    oneword = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
               "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
               "Seventeen", "Eighteen", "Ninteen"]
    tens = ["","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n < 20:
        return oneword[n] + SPACE
    else:
        return tens[n // 10] + SPACE + oneword[n % 10]

def convert3digits(n: int) -> str:
    HUN = "Hundred"
    if n < 100:
        return convert2digits(n)
    else:
        h, tu = divmod(n, 100)
        if tu == 0:
            return convert2digits(h) + SPACE + HUN
        else:
            return convert2digits(h) + SPACE + HUN + " and " + convert2digits(tu)

def fig2words(system: dict, amount: int) -> str:
    denoms = sorted(system.keys(), reverse=True)
    inwords = ''
    for denom in denoms:
        n = amount // denom
        if n > 0:
            inwords += convert3digits(n) + SPACE + system[denom] + SPACE
            amount %= denom
    return inwords

INDIAN = {10**7: "Crore", 10**5: "Lakh", 1000: "Thousand", 1: ""}
WESTERN = {10**9: "Billion", 10**6: "Million", 1000: "Thousand", 1: ""}

import sys
for amt in sys.argv[1:]:
    print(amt, fig2words(INDIAN, int(amt)))
    print(amt, fig2words(WESTERN, int(amt))) 
