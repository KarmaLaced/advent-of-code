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

    while bad_list:
        break_early = False  
        print(update)
        for i, value in enumerate(update):
            if i == 0:
                continue
            print(value)
            if value in reverse_rule_dict:
                # Any numbers associated with the value in the reverse dict
                # need to be before this value. Loop through the remaining numbers
                # and if any have precedence move them in front, then rerun
                for j, forward_value in enumerate(update[i+1:-1]):
                    if forward_value in reverse_rule_dict[value]:
                        # Move forward_value to before current value
                        print(*range(0,i))
                        print(j+i)
                        print(*range(i,j+i))
                        print(*range(j+i+1,len(update)))
                        new_order = [
                            *range(0,i),
                            j+i+1,
                            *range(i,j+i+1),
                            *range(j+i+2,len(update))
                        ]
                        print(new_order)
                        update = [update[k] for k in new_order]
                        print(update)
                        break_early = True
                        break
                if break_early:
                    break


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
        okay_count += int(mid_num)
    else:
        # Fix the bad list then check middle number
        pass
    
print(f"Okay Count:{okay_count}")