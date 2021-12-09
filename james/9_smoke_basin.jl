# Vents ahead! Inspect the terrain hights to deal with their smoke

function parse_terrain(terrain_file)
    """Convert terrain strings from file into 2D matrix"""
    terrain_data = readlines(terrain_file)
    terrain_matrix = Array{Int}(undef, length(terrain_data), length(terrain_data[1]))
    for i = 1:length(terrain_data)
        terrain_matrix[i, :] = parse.(Int, collect(terrain_data[i]))
    end
    return terrain_matrix
end

function get_neighbours(point, terrain)
    """All valid immediately adjacent neighbours of point in terrain"""
    row, col = point
    neighbours = []
    for offset = [-1, 1]
        neighbour_row, neighbour_col = row + offset, col + offset
        if neighbour_row > 0 && neighbour_row <= size(terrain, 1)
            push!(neighbours, [neighbour_row, col])
        end
        if neighbour_col > 0 && neighbour_col <= size(terrain, 2)
            push!(neighbours, [row, neighbour_col])
        end
    end
    return neighbours
end

function find_minima(terrain)
    """Find minima in the terrain data and return coordinates"""
    minima = []
    for (row, col) in Iterators.product(1:size(terrain, 1), 1:size(terrain, 2))
        if all(x->terrain[x...]>terrain[row, col], get_neighbours([row, col], terrain))
            push!(minima, [row, col])
        end
    end
    return minima
end

function flood_fill(terrain, minima)
    """Identify each basin: all points around minima and < 9"""
    basin_points, positions_to_fill = [minima], [minima]
    while length(positions_to_fill) > 0
        for n in get_neighbours(pop!(positions_to_fill), terrain)
            if !(terrain[n...] == 9) && !(n in basin_points)
                push!(basin_points, n)
                push!(positions_to_fill, n)
            end
        end
    end
    return basin_points
end

function minima_risks(terrain_data)
    """Get all minima in the terrain data, and sum their risk (height + 1)"""
    return sum(map(x->terrain_data[x...] + 1, find_minima(terrain_data)))
end

function minima_basins(terrain_data)
    """Find all the basins around minima, and return product of largest 3 areas"""
    basin_sizes = map(x->length(flood_fill(terrain_data, x)), find_minima(terrain_data))
    return prod(sort(basin_sizes, rev=true)[1:3])
end

terrain = parse_terrain("james/rsc/9_seabed_terrain.txt")
println("Part 1: $(minima_risks(terrain))")
println("Part 2: $(minima_basins(terrain))")
