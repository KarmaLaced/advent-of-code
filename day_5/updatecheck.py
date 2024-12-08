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
# Also create a reverse rule dict associated with each 'right' number
rule_dict = {}
reverse_rule_dict = {}
for rule in rules:
    if rule[0] in rule_dict:
        rule_dict[rule[0]].append(rule[1]) 
    else:
        rule_dict[rule[0]] = [rule[1]]
    
    if rule[1] in reverse_rule_dict:
        reverse_rule_dict[rule[1]].append(rule[0]) 
    else:
        reverse_rule_dict[rule[1]] = [rule[0]]

def rule_check(rule, update, ind_range):
    # Return False if a rule is broken
    for ind in ind_range:
        if rule in rule_dict:
            if update[ind] in rule_dict[rule]:
                return False
    return True

def fix_update(update):
    # For each number in the update, check if there is a following
    # number that it is supposed to be 
    bad_list = True
    break_early = False

    while bad_list:
        break_early = False
        update_loop = update.copy()
        print(update)
        for i, value in enumerate(update):
            print(value)
            # Look ahead and find any violations
            if value in reverse_rule_dict:
                remaining = [update[x] for x in range(i+1,len(update))]
                violating_inds = []
                for j, forward_value in enumerate(remaining):
                    if forward_value in reverse_rule_dict[value]:
                        violating_inds.append(i+1+j)
                # If a rule is violated, swap the current index and the latest
                # violating index
                if violating_inds:
                    update_loop[violating_inds[-1]] = update[i]
                    update_loop[i] = update[violating_inds[-1]]
                    update = update_loop
                    break_early = True
                    break
        if not break_early:
            bad_list = False
    
    # Return middle value
    mid_num = update[math.floor(len(update)/2)]
    return mid_num





#Check each update for validity
okay_count = 0
fixed_count = 0
for update in updates:
    bad_list = False
    for i, value in enumerate(update):
        # Check that the current number doesn't violate any rules of the
        # numbers before it
        # if it does, break the loop
        if not rule_check(value, update, range(i)):
            bad_list = True
            break
    if not bad_list:
        # Now get middle number of update
        mid_num = update[math.floor(len(update)/2)]
        okay_count += int(mid_num)
    else:
        # Fix the bad list then check middle number
        fixed_count += int(fix_update(update))
    
print(f"Okay Count:{okay_count}")
print(f"Fixed Count:{fixed_count}")