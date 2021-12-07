# Exponential lanternfish! Let's model their expanson
using StatsBase 

function parse_lanternfish(ages_file)
    ages_row = readlines(ages_file)[1]
    ages_ints = map((x)->parse(Int, x), split(ages_row, ","))
end

function evolve_population(population_ages, days)
    # Setup population dictionary
    pop_dict = countmap(population_ages)
    for key in 0:8
        if !(key in keys(pop_dict))
            pop_dict[key] = 0
        end
    end
    # Evolve
    for day = 1:days
        # Subtract one from all
        new_dict = copy(pop_dict)
        for key in 8:-1:1
            new_dict[key-1] = pop_dict[key]
        end
        # Set all 0's to 6's and add that many 8's
        new_dict[6] += pop_dict[0] 
        new_dict[8] = pop_dict[0]
        # Update
        pop_dict = new_dict
    end
    # Get population
    final_pop = sum(value for (key, value) in pop_dict)
    return final_pop
end

lanternfish_ages = parse_lanternfish("james/rsc/6_lanternfish_ages.txt")
println("Part 1: $(evolve_population(lanternfish_ages, 80))")
println("Part 1: $(evolve_population(lanternfish_ages, 256))")
