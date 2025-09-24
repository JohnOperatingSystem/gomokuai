def is_empty(board):
    # Check if the board is completely empty
    for i in range(8):
        for j in range(8):
            if board[i][j] != " ":
                return False
    return True
    
    
def is_bounded(board , y_end , x_end , length , d_y , d_x):
    # Check if a sequence is OPEN, SEMIOPEN, or CLOSED
    # side1: check one end
    if y_end + d_y < 8 and y_end + d_y > -1 and x_end + d_x < 8 and x_end + d_x > -1:
        if board[y_end + d_y][x_end + d_x] ==  ' ':
            side1 = True
        else:
            side1 = False
    else:
        side1 = False
    # side2: check the other end
    if y_end - length * d_y < 8 and y_end + -length * d_y > -1 and x_end - length * d_x <8 and x_end - length * d_x > -1:
        if board[y_end - length * d_y][x_end - length * d_x] == ' ':
            side2 = True
        else:
            side2 = False
    else:
        side2 = False
    # determine sequence type
    if side1 and side2:
        return 'OPEN'
    elif side1 or side2:
        return "SEMIOPEN"
    else:
        return 'CLOSED'


def sequences_with_start_and_length(lst , col):
    # Identify all sequences of a specific color in a 1D list
    sequences = []
    current_length = 0
    start_index = None

    for i , item in enumerate(lst):
        if item == col:
            if current_length == 0:  # New sequence starts
                start_index = i
            current_length += 1
        else:
            if current_length > 0:  # Sequence ends
                sequences.append((start_index , current_length))
                current_length = 0

    # Add the last sequence if the list ends with the col
    if current_length > 0:
        sequences.append((start_index , current_length))

    return sequences    

def detect_row(board , col , y_start , x_start , length , d_y , d_x):
    # Detect sequences of a certain length in a row along a given direction
    open_seq_count, semi_open_seq_count = 0, 0
    res = []
    for i in range(len(board)):
        # Collect the row in the given direction
        if 0<= y_start+ i*d_y < 8 and 0 <= x_start + i*d_x < 8:
            res.append(board[y_start+ i*d_y][x_start + i*d_x])
    
    a = sequences_with_start_and_length(res,col)
    for i in a:
        if i[1] == length:
            # Check sequence type (OPEN or SEMIOPEN)
            if is_bounded(board, y_start +i[0]*d_y + (length-1) *d_y, x_start +i[0]*d_x + (length-1) *d_x, length, d_y, d_x) == "OPEN":
                open_seq_count +=1
            elif is_bounded(board, y_start +i[0]*d_y + (length-1) *d_y, x_start +i[0]*d_x + (length-1) *d_x, length, d_y, d_x) == "SEMIOPEN":
                semi_open_seq_count +=1

    return open_seq_count, semi_open_seq_count

def detect_rows_(board, col, length):
    # Count sequences for all directions (helper function)
    open_seq_count, semi_open_seq_count = 0, 0
    # left to right
    for y in range(8):
        sequence = detect_row(board, col, y, 0, length, 0, 1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]
    # top to bottom
    for x in range(8):
        sequence = detect_row(board, col, 0, x, length, 1, 0)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]
    # top left to bottom right
    for y in range(1, 8-(length-1)):
        sequence = detect_row(board, col, y, 0, length, 1, 1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]  
    for x in range (8-(length-1)):
        sequence = detect_row(board, col, 0, x, length, 1, 1) 
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]               
    # top right to bottom left
    for x in range(1, 8-(length-1)):
        sequence = detect_row(board, col, 0, x, length, 1, -1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]   
    for y in range(8-(length-1)):
        sequence = detect_row(board, col, y, 0, length, 1, -1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]           
    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    # Main function to detect sequences in all directions for a color
    open_seq_count, semi_open_seq_count = 0, 0
    # left to right
    for y in range(8):
        sequence = detect_row(board, col, y, 0, length, 0, 1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]
    # top to bottom
    for x in range(8):
        sequence = detect_row(board, col, 0, x, length, 1, 0)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]
    # top left to bottom right
    for y in range(1, 8-(length-1)):
        sequence = detect_row(board, col, y, 0, length, 1, 1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]  
    for x in range (8-(length-1)):
        sequence = detect_row(board, col, 0, x, length, 1, 1) 
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]               
    # top right to bottom left
    for x in range(1, 8-(length-1)):
        sequence = detect_row(board, col, 0, x, length, 1, -1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]   
    for y in range(8-(length-1)):
        sequence = detect_row(board, col, y, 0, length, 1, -1)
        open_seq_count += sequence[0]
        semi_open_seq_count += sequence[1]           
    return open_seq_count, semi_open_seq_count


def search_max(board):
    # Choose the best move for computer
    biggest_score = -100000
    move_x, move_y = 0, 0
    for x in range(8):
        for y in range(8):
            if board[y][x] == " ":
                board[y][x] = "b"
                if score(board) > biggest_score:  
                    move_x = x
                    move_y = y                      
                    biggest_score = score(board)
                    board[y][x] = " "
                else:
                    board[y][x] = " "
    return move_y, move_x
    
def score(board):
    # Evaluate the board and return a numeric score
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    # Count sequences for both colors
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    # Check if someone already won
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    # Weighted score calculation for other sequences
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    # Check all possible winning directions for each stone
    for x in range(8):
        for y in range(8):
            if board[y][x] != " ":
                col = board[y][x]

                # Horizontal check
                dummyx = x
                counter = 0
                while board[y][dummyx] == col and dummyx < 7:
                    dummyx += 1
                    counter += 1
                    if counter >= 5:
                        return "Black won" if col == "b" else "White won"
                    
                # Vertical check
                dummyy = y
                counter = 0
                while board[dummyy][x] == col and dummyy < 7:
                    dummyy += 1
                    counter += 1
                    if counter >= 5:
                        return "Black won" if col == "b" else "White won"
                
                # Diagonal top-left to bottom-right
                dummyx, dummyy = x, y
                counter = 0
                while board[dummyy][dummyx] == col and dummyx < 7 and dummyy < 7:
                    counter += 1
                    dummyx += 1
                    dummyy += 1
                    if counter >= 5:
                        return "Black won" if col == "b" else "White won"

                # Diagonal top-right to bottom-left
                dummyx, dummyy = x, y
                counter = 0
                while board[dummyy][dummyx] == col and (dummyx >= 1 and dummyy < 7):
                    counter += 1
                    dummyx -= 1
                    dummyy += 1
                    if counter >= 5:
                        return "Black won" if col == "b" else "White won"        

    # If there are empty spaces, continue playing
    for x in range(8):
        for y in range(8):  
            if board[y][x] == " ":
                return "Continue playing"
    return "Draw"


def print_board(board):
    # Print the board in a formatted way
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    # Create an empty board of size sz x sz
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                

def analysis(board):
    # Print counts of sequences for each player
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    # Main game loop
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    # Place a sequence of stones on the board
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

if __name__ == "__main__":
    some_tests()
