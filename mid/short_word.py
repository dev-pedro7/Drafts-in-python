def find_short(s):
    shorter = min(len(x) for x in s.split())
    return shorter