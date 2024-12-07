import math

#Read in rules and updates
rules = []
updates = []
with open("page_rules.txt") as file:
    for line in file:
        rules.append(line.split()[0].split("|"))

with open("page_updates.txt") as file:
    for line in file:
        updates.append(line.split()[0].split(","))

# Convert rules to a dict with a list associated with each 'left' number
rule_dict = {}
for rule in rules:
    if rule[0] in rule_dict:
        rule_dict[rule[0]].append(rule[1]) 
    else:
        rule_dict[rule[0]] = [rule[1]]

def rule_check(rule, update, ind_range):
    # Return False if a rule is broken
    for ind in ind_range:
        if rule in rule_dict:
            if update[ind] in rule_dict[rule]:
                return False
    return True

#Check each update for validity
okay_count = 0
fixed_count = 0
for update in updates:
    bad_list = False
    for i, value in enumerate(update):
        # First value is always good
        if i == 0:
            continue

        # Check that the current number doesn't violate any rules of the
        # numbers before it
        # if it does, break the loop
        if not rule_check(value, update, range(i)):
            bad_list = True
            break
    if not bad_list:
        # Now get middle number of update
        mid_num = update[math.floor(len(update)/2)]
        print(update)
        print(mid_num)
        okay_count += int(mid_num)
    else:
        # Fix the bad list
        pass
    
print(okay_count)