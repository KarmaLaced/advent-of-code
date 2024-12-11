import itertools
antennafield = []
with open("antennafield.txt") as file:
    for line in file:
        data = line.strip()
        antennafield.append(data)

field_size = [len(antennafield)-1,len(antennafield[0])-1]
print(field_size)
antennas = {}
all_antenna_locations = []
for i, row in enumerate(antennafield):
    #Get antenna locations
    for j, col in enumerate(row):
        if col != ".":
            if col in antennas:
                antennas[col].append([i,j])
            else:
                antennas[col] = [[i,j]]
            all_antenna_locations.append([i,j])

def hotspot_calc(site1, site2):
    site_diff = [site2[0]-site1[0], site2[1]-site1[1]]
    
    hotspot1 = [site1[0]-site_diff[0],site1[1]-site_diff[1]]
    hotspot2 = [site2[0]+site_diff[0],site2[1]+site_diff[1]]
    return [hotspot1, hotspot2]

def super_hotspot_calc(site1, site2, field_size,all_antenna_locations):
    site_diff = [site2[0]-site1[0], site2[1]-site1[1]]
    hotspot_list = []
    # For every antenna pair find all diagonals based on field size
    # Move away from site 1, then away from from site2
    while hotspot_check(site1, field_size):
        site1 = [site1[0]-site_diff[0],site1[1]-site_diff[1]]
        if hotspot_check(site1, field_size) and site1 not in all_antenna_locations:
            hotspot_list.append(site1)
    while hotspot_check(site2, field_size):
        site2 = [site2[0]+site_diff[0],site2[1]+site_diff[1]]
        if hotspot_check(site2, field_size) and site2 not in all_antenna_locations:
            hotspot_list.append(site2)
    
    return hotspot_list

def hotspot_check(hotspot, field_size):
    if hotspot[0] < 0 or hotspot[1] < 0 or hotspot[0]>field_size[0] or hotspot[1]>field_size[1]:
        return False
    return True

# Loop through each antenna and get location of hotspots
all_pairs = []
hotspots = []
superhotspots = []
antenna_hotspot_count = 0
for antenna in antennas:
    # Loop through 0:second to last value in each antenna location
    # For each pair, calculate distance between then calculate hotspot
    for i, location in enumerate(antennas[antenna]):
        for j in range(i+1,len(antennas[antenna])):
            hotspotpair = hotspot_calc(location, antennas[antenna][j])
            superhotspots_list = super_hotspot_calc(location, antennas[antenna][j],field_size, all_antenna_locations)

            for hotspot in hotspotpair:
                if hotspot_check(hotspot,field_size):
                    hotspots.append(hotspot)
            for hotspot in superhotspots_list:
                superhotspots.append(hotspot)
            all_pairs.append([location, antennas[antenna][j]])
            
        antenna_hotspot_count += 1

# Remove duplicate hotspots
hotspots.sort()
print(f"Length Hotspots: {len(hotspots)}")
filtered_hotspots = list(k for k, _ in itertools.groupby(hotspots))
print(f"Length Hotspots (Filtered): {len(filtered_hotspots)}")

superhotspots.sort()
print(f"Length Super Hotspots: {len(superhotspots)}")
filtered_superhotspots = list(k for k, _ in itertools.groupby(superhotspots))
print(f"Length Super Hotspots (Filtered): {len(filtered_superhotspots)} + {antenna_hotspot_count} = {len(filtered_superhotspots)+antenna_hotspot_count}")