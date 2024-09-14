strings= ["my","world","apple","pear"]
# lengths1 = map(len,strings)
def add_s(string):
    return string + "ss"
lengths1 = map(lambda x:x+"s",strings)
lengths1 = map(add_s,strings)

print(list(lengths1))
