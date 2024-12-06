
list1 = []
list2 = []
#Read in values
with open("lists.txt") as file:
    for line in file:
        values = line.split()
        list1.append(int(values[0]))
        list2.append(int(values[1]))

#Sort lists
list1.sort()
list2.sort()

#diff the lists
diff = []
sim = []
for value1, value2 in zip(list1,list2):
    #find diff
    diff.append(abs(value1-value2))

    #find sim
    sim.append(value1*list2.count(value1))
print(f"Sum of differences: {sum(diff)}")
print(f"Sum of similarity: {sum(sim)}")

#Find similarity score

