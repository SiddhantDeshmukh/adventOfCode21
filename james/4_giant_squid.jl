# Giant Squid! Let's play bingo with it to make it feel better

function parse_bingo_data(bingo_file)
    data_lines = readlines(bingo_file)
    # Extract the calling order: Vector of Ints
    calling_order = map((x)->parse(Int, x), split(data_lines[1], ","))
    # Parse all the boards: Vector of Vectors
    all_boards = map(3:6:size(data_lines, 1)) do start_line
        lines = join(data_lines[start_line:start_line+4], " ") 
        board = map((x)->parse(Int, x), split(lines, " ", keepempty=false))
        return board
    end
    return (calling_order, all_boards)
end

function is_bingo(board, called)
    """Check if a full column or row of board has been called"""
    for ind = 1:5
        row_start = ((ind-1)*5)+1
        col, row = board[ind:5:end], board[row_start:row_start+4]
        if intersect(col, called) == col || intersect(row, called) == row
            return true
        end
    end
    return false
end

function board_score(board, called_numbers)
    return called_numbers[end] * sum(setdiff(board, called_numbers))
end

function best_board_score(calling_order, all_boards)
    """Score the best board (first to win) on the calling order
    Win if all numbers in a row or column are finished
    Score = (last number called) * (sum of all uncalled numbers on card)"""
    for val = 5:size(calling_order, 1)
        called_numbers = calling_order[1:val]
        for board in all_boards
            if is_bingo(board, called_numbers)
                return board_score(board, called_numbers)
            end
        end
    end
end

function worst_board_score(calling_order, all_boards)
    """Score the worst board (last to win) on the calling order
    Same rules as best_board_score"""
    remaining_boards = 1:size(all_boards, 1)
    for val = 5:size(calling_order, 1)
        called_numbers = calling_order[1:val]
        for (ind, board) in enumerate(all_boards)
            if is_bingo(board, called_numbers)
                new_remaining = setdiff(remaining_boards, ind)
                if length(new_remaining) == 0
                    return board_score(all_boards[remaining_boards][1], called_numbers)
                else
                    remaining_boards = new_remaining
                end
            end
        end
    end
end

# Parse all the data: boards and call_order separately
call_order, boards = parse_bingo_data("james/rsc/4_squid_bingo.txt")
println("Part 1: $(best_board_score(call_order, boards))")
println("Part 2: $(worst_board_score(call_order, boards))")
