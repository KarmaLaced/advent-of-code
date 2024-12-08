guardmap = []
with open("guardmap.txt") as file:
    for line in file:
        guardmap.append(line.replace("\n",""))

# Build/initialize guard class
class Guard:
    def __init__(self,map):
        self.map = map
        # Find size and boundaries of map
        self.mapwidth = len(self.map[0])
        self.mapheight = len(self.map)

        # Find starting position of guard
        # Will be either ^, >, v, <
        self.valid_positions = ["^", ">", "v", "<"]
        for i, row in enumerate(self.map):
            for position in self.valid_positions:
                if position in row:
                    self.position = position
                    self.row = i
                    self.col = row.index(position)
        
        self.current_target = "?"
        self.coord_history = [f"{self.row},{self.col}"]
        self.combined_history = [f"{self.position},{self.row},{self.col}"]

    def turn_right(self):
        current_pos_ind = self.valid_positions.index(self.position)
        self.position = self.valid_positions[(current_pos_ind + 1) % 4]
        self.get_current_target()

    def turn_right_until_valid(self):
        # Turn right until target is not "#"
        # Do one turn first
        self.turn_right()
        while self.current_target == "#":
            self.turn_right()
        
    
    def get_current_target(self):
        target_row = self.row
        target_col = self.col
        match self.position:
            case "^":
                target_row += -1
            case ">":
                target_col += 1
            case "v":
                target_row += 1
            case "<":
                target_col += -1
        self.current_target = self.map[target_row][target_col]
    
    def take_step(self):
        self.get_current_target()        
        if self.current_target == "#":
            self.turn_right_until_valid()
        
        match self.position:
            case "^":
                self.row += -1
            case ">":
                self.col += 1
            case "v":
                self.row += 1
            case "<":
                self.col += -1
        # Append new position to history
        self.coord_history.append(f"{self.row},{self.col}")
        self.combined_history.append(f"{self.position},{self.row},{self.col}")

guard = Guard(guardmap)
while guard.row > 0 and guard.row <= guard.mapwidth and guard.col > 0 and guard.col <= guard.mapheight:
    try:
        guard.take_step()
    except IndexError:
        # Found edge of map, break
        break

# Check coord history and remove duplicates
history = list(dict.fromkeys(guard.coord_history))
print(f"Total Unique Steps: {len(history)}")


loop_count = 0
for i in range(0,guard.mapwidth):
    print(f"{i}/{guard.mapwidth}...{loop_count}")
    for j in range(0,guard.mapheight):
        # Initialize new loop_guard
        loop_guard = Guard(guardmap.copy()) # Initial loop guard
        num_steps = 0
        if loop_guard.map[i][j] in ["#","^",">","v","<"]:
            # Go to next (no need to check this)
            continue

        if f"{i},{j}" not in guard.coord_history:
            # Obstruction not in original path, can't create loop
            continue
        # place obstruction
        old_row = loop_guard.map[i]
        new_row = list(old_row)
        new_row[j] = "#"
        loop_guard.map[i] = new_row
        
        while loop_guard.row > 0 and loop_guard.row <= loop_guard.mapwidth and loop_guard.col > 0 and loop_guard.col <= loop_guard.mapheight:
            try:
                loop_guard.take_step()
                num_steps += 1
            except IndexError:
                # Found edge of map, break
                break
            if num_steps > 3:
                if f"{loop_guard.position},{loop_guard.row},{loop_guard.col}" in loop_guard.combined_history[0:-2]:
                    loop_count += 1
                    break

print(f"Total Possible Loops: {loop_count}")