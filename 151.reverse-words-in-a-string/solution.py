s = "the sky is blue"

split = s.split()
split[:] = split[::-1]
rev = " ".join(split)
print(rev) 