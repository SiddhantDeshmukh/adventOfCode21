# Angry Glowy Octopi! Predict their flashes to navigate by it's light

function read_octopi_energy(energy_file)
    energy_data = readlines(energy_file)
    energy_matrix = Array{Int}(undef, length(energy_data), length(energy_data[1]))
    for i = 1:length(energy_data)
        energy_matrix[i, :] = parse.(Int, collect(energy_data[i]))
    end
    return energy_matrix
end

function update_energies(energy_dict, grid_size)

    function get_neighbours(pos, grid_size)
        r, c = pos
        neighbours = []
        for i in [(r-1,c),(r+1,c),(r,c-1),(r,c+1),(r-1,c-1),(r+1,c+1),(r+1,c-1),(r-1,c+1)]
            if i[1] > 0 && i[1] <= grid_size[1] && i[2] > 0 && i[2] <= grid_size[2]
                push!(neighbours, i)
            end
        end
        return neighbours
    end

    function get_to_flash(dict, flashed)
        return [k for (k, v) in dict if !(k in flashed) && v >= 10]
    end

    flashes = 0
    flashed = Set()
    # Increment
    energy_dict = Dict((k, v+1) for (k,v) in energy_dict)
    # While positions to flash, flash-em and update neighbours
    to_flash = get_to_flash(energy_dict, flashed)
    while length(to_flash) > 0
        for flash in to_flash
            push!(flashed, flash)
            for n in get_neighbours(flash, grid_size)
                energy_dict[n] += 1
            end
        end
        to_flash = get_to_flash(energy_dict, flashed)
    end
    # Reset the flashed values to 0
    for (k, v) in energy_dict
        if v > 9
            energy_dict[k...] = 0
            flashes += 1
        end
    end
    return energy_dict, flashes
end

function count_flashes(energy_matrix, steps)
    grid_size = size(energy_matrix)
    energy_dict = Dict(((x, y), energy_matrix[x, y]) for (x,y) in Iterators.product(1:size(energy_matrix, 1), 1:size(energy_matrix, 2)))
    flashes = 0  
    for _ in 1:steps 
        (energy_dict, step_flashes) = update_energies(energy_dict, grid_size)
        flashes += step_flashes
    end
    return flashes
end

function find_flash_sync(energy_matrix)
    grid_size = size(energy_matrix)
    energy_dict = Dict(((x, y), energy_matrix[x, y]) for (x,y) in Iterators.product(1:size(energy_matrix, 1), 1:size(energy_matrix, 2)))
    step, found_sync = 0, false
    while !(found_sync)
        step += 1
        (energy_dict, _) = update_energies(energy_dict, grid_size)
        if length(unique(values(energy_dict))) == 1
            found_sync = true    
        end
    end
    return step
end

energies = read_octopi_energy("james/rsc/11_octopus_energies.txt")
println("Part 1: $(count_flashes(energies, 100))")
println("Part 2: $(find_flash_sync(energies))")
