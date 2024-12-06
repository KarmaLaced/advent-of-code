#Read in values
wordsearch = []
with open("wordsearch.txt") as file:
    for line in file:
        wordsearch.append(line)

# Create searching function
def letter_check(wordsearch, cur_row, cur_col, letter_to_find, direction):
    # Direction map:
    # [horz, vert]
        # [-1, 0, 1] = [left, mid, right]
        # [-1, 0, 1] = [down, mid, up]
    # ex: [-1, 0] = left
    # ex: [-1, 1] = left+up
    new_row = cur_row+direction[0]
    new_col = cur_col+direction[1]
    if new_row < 0 or new_col < 0:
        return False
    try:
        if wordsearch[new_row][new_col] == letter_to_find:
            return True
        return False
    except:
        return False


def xmas_search(wordsearch, cur_row, cur_col, word = "XMAS"):
    # Finds number of Xmas from current location
    # Won't be XMAS if it doesn't start with X
    
    if wordsearch[cur_row][cur_col] != word[0]:
        return 0
    
    # Find direction to move for second letter+
    horz = [-1, 0, 1]
    vert = [-1, 0, 1]
    wordcount = 0
    for i in horz:
        for j in vert:
            bad_letter = False
            direction = [i,j]
            new_row = cur_row
            new_col = cur_col
            if letter_check(wordsearch, new_row, new_col, letter_to_find=word[1], direction=direction):
                new_row += direction[0]
                new_col += direction[1]
                # Found a valid direction for second letter, keep going in same direction for remaining letters
                for letter in word[2:len(word)]:
                    if not letter_check(wordsearch, new_row, new_col, letter_to_find=letter, direction=direction):
                        bad_letter = True
                        break
                    new_row += direction[0]
                    new_col += direction[1]
                if not bad_letter:
                    wordcount += 1
    return wordcount 

def exmas_search(wordsearch, cur_row, cur_col):
    # Finds number of Xmas from current location
    # Won't be an X-MAS if there is no A in the middle
    
    if wordsearch[cur_row][cur_col] != "A":
        return 0  
    
    # Search in four opposing directions
    upleft = [-1,1]
    upright = [1,1]
    downleft = [-1,-1]
    downright = [1,-1]

    diag1 = [upleft,downright]
    diag2 = [upright,downleft]

    # Check top-left, if S or M, check bottom right for opposite
    # Then do same for top-right/bottom-left
    wordcount = 0
    for diag in [diag1, diag2]:
        next_letter = None
        for direction in diag:
            if not next_letter:
                #Check for M
                if letter_check(wordsearch, cur_row, cur_col, letter_to_find="M", direction=direction):
                    next_letter = "S"
                elif letter_check(wordsearch, cur_row, cur_col, letter_to_find="S", direction=direction):
                    next_letter = "M"
                else:
                    return 0
            else:
                if not letter_check(wordsearch, cur_row, cur_col, letter_to_find=next_letter, direction=direction):
                    return 0
    return 1

wordcount = 0
exwordcount = 0
for i, line in enumerate(wordsearch):
    for j, _ in enumerate(line):
        wordcount += xmas_search(wordsearch,i,j)
        exwordcount += exmas_search(wordsearch,i,j)

print(wordcount)
print(exwordcount)
