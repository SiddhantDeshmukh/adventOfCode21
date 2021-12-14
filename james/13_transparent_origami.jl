function read_dots_folds(data_file)
    lines = readlines(data_file)
    # Parse points
    point_array = Set(parse.(Int, r) for r in split.(lines[1:907], ","))
    # Parse folds 
    clean_folds = []
    for fold in split.(lines[909:920], "=")
        val = parse(Int, fold[2])
        push!(clean_folds, (fold[1][end] == 'x' ? [val, 0] : [0, val]))
    end
    return (point_array, clean_folds)
end

function fold(points, folds)
    for this_fold in folds
        new_points = Set()
        fold_index = this_fold[1] == 0 ? 2 : 1
        fold_point = this_fold[fold_index]
        for point in points
            fold_val = point[fold_index]
            if fold_val > fold_point
                fold_val = fold_point - (fold_val - fold_point)
            end
            new_point = collect(point)
            new_point[fold_index] = fold_val
            push!(new_points, Tuple(new_point))
        end
        # Update for next instruction
        points = new_points
    end
    return points
end

function fold_and_visualise(points, folds)
    # Do all the folds
    after_folding = fold(points, folds)
    # Draw the points onto a matrix
    max_x, max_y = maximum(p[1] for p in after_folding), maximum(p[2] for p in after_folding)
    draw_matrix = zeros(Int, max_y+1, max_x+1)
    for point in after_folding
        draw_matrix[point[2]+1, point[1]+1] = 1
    end
    # Convert to nicely viewable form
    return string("\n", join([string(join([(n==1 ? '*' : ' ') for n in r]),"\n") for r in eachrow(draw_matrix)]))
end

dots, folds = read_dots_folds("james/rsc/13_dots_and_folds.txt")
println("Part 1: $(length(fold(dots, folds[1:1])))")
println("Part 2: $(fold_and_visualise(dots, folds))")
