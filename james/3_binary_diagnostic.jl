# Binary Diagnostic. That's a creaking noise, check the logs to find the issue.
using DelimitedFiles
using StatsBase

function common_column_elements(binary_mat; use_mode=true)
    function common_element(col)
        val = mode(col)
        if !use_mode
            val = Int(!Bool(val))
        end
        val_count = sum(x->x==val, col)
        if val_count == size(col, 1)/2
            val = Int(use_mode)
        end
        return floor(Int, val)
    end
    return map(common_element, eachrow(binary_mat))
end

function binarray_to_int(binary_array)
    return parse(Int, reduce(string, binary_array); base=2)
end

function filter_binary(binary_mat; use_mode = true)
    keep_cols = 1:size(binary_mat, 2)
    for (ind, col) = enumerate(eachrow(binary_mat))
        bit_array = common_column_elements(binary_mat[:, keep_cols], use_mode=use_mode)
        binary_match = findall(x -> x == bit_array[ind], col)
        keep_cols = intersect(keep_cols, binary_match)
        if length(keep_cols) == 1
            return binary_mat[:, keep_cols[1]]
        end
    end
end

function measure_power(binary_mat)
    gamma = common_column_elements(binary_mat)
    epsilon = common_column_elements(binary_mat, use_mode=false)
    return binarray_to_int(gamma) * binarray_to_int(epsilon)
end

function measure_life_support(binary_mat)
    oxygen_gen_rating = filter_binary(binary_mat, use_mode=true)
    co2_scrubber_rating = filter_binary(binary_mat, use_mode=false)
    return binarray_to_int(oxygen_gen_rating) * binarray_to_int(co2_scrubber_rating)
end

data = readdlm("james/rsc/3_binary_data.txt", String)
int_data = map((x) -> parse(Int, x; base=2), data)
mat_int = reduce(hcat, map((x) -> digits(x, base=2, pad=12)[end:-1:1], int_data))
println("Part 1: $(measure_power(mat_int))")
println("Part 2: $(measure_life_support(mat_int))")
