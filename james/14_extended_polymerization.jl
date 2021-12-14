function countmatch(substr, str)
    return length(collect(eachmatch(Regex(string(substr)), str)))
end

function read_polymer_data(data_file)
    lines = readlines(data_file)
    return (lines[1], Dict(split.(lines[3:102], " -> ")))
end

function extend_polymer(polymer, rules, steps)
    countmatch(substr, str) = length(collect(eachmatch(Regex(substr), str)))
    pair_counts = Dict((k, countmatch(string(k), polymer)) for (k, v) in rules)
    indiv_counts = Dict((v, countmatch(string(v), polymer)) for (k, v) in rules)
    for _ in 1:steps
        # Iterate over a copy, and modify the original - sneaky!
        for (pair, count) in copy(pair_counts)
            # Count of this pair gets reduced
            pair_counts[pair] -= count
            # Add the count of new composed pair_counts to existing
            pair_counts[string(pair[1], rules[pair])] += count
            pair_counts[string(rules[pair], pair[2])] += count
            # Only the counts of the new value have changed overall
            indiv_counts[rules[pair]] += count
        end
    end
    return maximum(values(indiv_counts)) - minimum(values(indiv_counts))
end

polymer_template, update_rules = read_polymer_data("james/rsc/14_polymer_rules.txt")
println("Part 1: $(extend_polymer(polymer_template, update_rules, 10))")
println("Part 1: $(extend_polymer(polymer_template, update_rules, 40))")
