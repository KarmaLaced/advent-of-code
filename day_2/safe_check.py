def is_safe(value_list):
    for i, value in enumerate(value_list):
        value = int(value)
        if i == 0:
            prev_value = value
            continue
        # Get delta
        delta = value-prev_value
        if delta == 0 or abs(delta)>3:
            return 0
        
        if i > 1:
            # Check if delta in same direction
            direction = delta*prev_delta
            if direction < 0:
                return 0
            
        prev_delta = delta
        prev_value = value
    return 1

def is_safe_dampen(value_list):
    safe_arr = []
    for i, value in enumerate(value_list):
        dampened_list = value_list.copy()
        del dampened_list[i]
        safe_arr.append(is_safe(dampened_list))
    if 1 in safe_arr:
        print(safe_arr)
        return 1
    return 0

safesum = 0
safesumdamp = 0
#Read in values
with open("reports.txt") as file:
    for line in file:
        values = line.split()
        safesum += is_safe(values)
        safesumdamp += is_safe_dampen(values)

print(f"Safe Sum: {safesum}")
print(f"Safe Sum (dampened) {safesumdamp}")