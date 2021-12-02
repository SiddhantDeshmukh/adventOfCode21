# Dive! Where are we? Work out where we stopped from a manual and movement logs
using DelimitedFiles

function dive_displacement(movement)
    horizontal, depth = 0, 0
    for (move, disp) in eachrow(movement)
        if move == "forward"
            horizontal += disp
        elseif move == "down"
            depth += disp
        elseif move == "up"
            depth -= disp
        end
    end
    return horizontal * depth
end 

function aimed_dive_displacement(movement)
    horizontal, depth, aim = 0, 0, 0
    for (move, disp) in eachrow(movement)
        if move == "forward"
            horizontal += disp
            depth += disp * aim
        elseif move == "down"
            aim += disp
        elseif move == "up"
            aim -= disp
        end
    end
    return horizontal * depth
end 

# Read in the data to an array
data = readdlm("james/rsc/2_submarine_movement.txt")
println("Part 1: $(dive_displacement(data))")
println("Part 2: $(aimed_dive_displacement(data))")