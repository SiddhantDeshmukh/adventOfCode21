# import Cairo, Fontconfig
# using GraphPlot 
using StatsBase
using Graphs 

function read_cave_paths(path_file)
    raw_links = split.(readlines(path_file), "-")
    # Convert to adjacency matrix
    unique_nodes = unique(Iterators.flatten(raw_links))
    node_map = Dict((v, i) for (i, v) in enumerate(unique_nodes))
    # Convert edges to adjacency matrix
    adj_matrix = zeros(Int, length(unique_nodes), length(unique_nodes))
    for edge in raw_links
        n1, n2 = node_map[edge[1]], node_map[edge[2]]
        adj_matrix[n1, n2] = 1
        adj_matrix[n2, n1] = 1
    end
    # Convert to graph object
    graph = SimpleGraph(adj_matrix)
    return graph, node_map
end

function is_small_cave(label)
    return (lowercase(label) == label) && !(label == "start") && !(label == "end")
end 

function find_unique_paths(graph, labels, node_test_func; first="start", last="end")
    # Get paths from start
    inv_lab = Dict((v, k) for (k, v) in labels)
    from, to = labels[first], labels[last]
    done, paths, completed_paths = false, [[from]], Set()
    while !done
        new_paths = Set()
        for path in paths
            for neigh in neighbors(graph, path[end])
                # If completed, add to end of path and store
                if neigh == to
                    push!(completed_paths, append!(copy(path), [neigh]))
                # else, if a valid path, add to new_paths
                elseif node_test_func(neigh, path, inv_lab)
                    push!(new_paths, append!(copy(path), [neigh]))
                end
            end
        end
        # Check if done
        if length(new_paths) == 0
            done = true
        else 
            paths = new_paths  
        end
    end
    return length(completed_paths)
end

function part1_test(n, path, inv_lab)
    """Allowed to revisit if Uppercase or Lowercase if not visited before"""
    n_lab = inv_lab[n]
    return (uppercase(n_lab) == n_lab || (is_small_cave(n_lab) && !(n in path))) 
end

function part2_test(n, path, inv_lab)
    """Allowed to revisit if Uppercase, Lowercase if visited once, and not start"""
    n_lab = inv_lab[n]
    d = countmap([e for e in path if is_small_cave(inv_lab[e])])
    if (n_lab == "start")
        return false
    elseif !(n in keys(d))
        return true
    elseif (d[n] == 1) && (length([(k, v) for (k, v) in d if (k != n) && (v == 2)]) == 0)
        return true
    end
    return false
end

cave_graph, node_labels = read_cave_paths("james/rsc/12_puzzling_pathways.txt")
println("Part 1: $(find_unique_paths(cave_graph, node_labels, part1_test))")
println("Part 2: $(find_unique_paths(cave_graph, node_labels, part2_test))")
