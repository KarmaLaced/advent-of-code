import re

def mul(a,b):
    return a*b

#Read in values
with open("corrupted_memory.txt") as file:
    content = file.read()
# mul(##,##)
regexp = r"(mul\(\d+,\d+\))"

# do() or don't()
ena_regexp = r"(do\(\)|don't\(\))"
combined_regexp = '|'.join([regexp,ena_regexp])
print(combined_regexp)
mul_matches = re.findall(regexp,content)
combined_matches = ["".join(x) for x in re.findall(combined_regexp,content)]
print(combined_matches)
matchsum = 0
combinedsum = 0
do = 1
for match in combined_matches:
    if re.match(regexp,match):
        matchsum += eval(match)
        if do:
            combinedsum += eval(match)
        continue
    if match == "do()":
        do = 1
    if match == "don't()":
        do = 0

print(f"Match Sum: {matchsum}")
print(f"Combined Sum: {combinedsum}")