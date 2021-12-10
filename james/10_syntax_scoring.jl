# Sytanx Error! Somethings wrong with the nav system - fix the subsystems!
using Statistics

function find_illegal_character(subsystem)
    open_history = []
    for char in subsystem
        if char in values(close_open_map)
            push!(open_history, char)
        elseif char in keys(close_open_map)
            if close_open_map[char] == open_history[end]
                pop!(open_history)
            else
                return char
            end
        end
    end
    return nothing
end

function get_hanging_brackets(subsystem)
    open_history = []
    for char in subsystem
        if char in values(close_open_map)
            push!(open_history, char)
        elseif char in keys(close_open_map)
            if close_open_map[char] == open_history[end]
                pop!(open_history)
            end
        end
    end
    return open_history
end

function score_syntax_corruption(subsystem_lines)
    illegal_score = Dict(')'=>3, ']'=>57, '}'=>1197, '>'=>25137, nothing=>0)
    return sum(illegal_score[find_illegal_character(s)] for s in subsystem_lines)
end

function score_syntax_completion(subsytem_lines)
    completion_scores = Dict('('=>1, '['=>2, '{'=>3, '<'=>4)
    incomplete_lines = [l for l in subsytem_lines if find_illegal_character(l) === nothing]
    all_scores = []
    for line in incomplete_lines
        completion = reverse(get_hanging_brackets(line))
        score = 0
        for char in completion
            score = (score * 5) + completion_scores[char]
        end
        push!(all_scores, score)
    end
    return trunc(Int, median(all_scores))
end

# Read in the subsystem data
subsystems = readlines("james/rsc/10_subsystem_syntaxes.txt")
close_open_map =  Dict('>'=>'<', '}'=>'{', ']'=>'[', ')'=>'(')
println("Part 1: $(score_syntax_corruption(subsystems))")
println("Part 2: $(score_syntax_completion(subsystems))")
