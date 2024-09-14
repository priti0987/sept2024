inp="Priti Test Automation Specialist"

out =""
#print(inp.split(" "))
i1=inp.split(" ")
for i in i1:
    #print(i)
    if i.isnumeric():
        print("num")
    else:
        for n in range(len(i)):
            print(i[n])
            out=  i[n]+out
        print("* "+out)