# Treachery! We don't want to be a whale snack - align the crab submarines!

function parse_crabs(crab_file)
    pos_row = readlines(crab_file)[1]
    pos_ints = map((x)->parse(Int, x), split(pos_row, ","))
    return pos_ints
end

function minimum_fuel(positions; understand_crab_engineering=false)
    min_fuel_use = Inf
    for pos = minimum(positions):maximum(positions)
        indiv_fuels = @. abs(positions - pos)
        if understand_crab_engineering
            indiv_fuels = map((x)->(x*(x+1))/2, indiv_fuels)
        end
        min_fuel_use = min(min_fuel_use, sum(indiv_fuels))
    end
    return trunc(Int, min_fuel_use)
end

crab_positions = parse_crabs("james/rsc/7_crab_positions.txt")
println("Part 1: $(minimum_fuel(crab_positions))")
println("Part 2: $(minimum_fuel(crab_positions, understand_crab_engineering=true))")
