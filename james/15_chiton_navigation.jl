using Graphs, SimpleWeightedGraphs
using SparseArrays
using GraphPlot; import Cairo

function risks_to_graph(risk_matrix)
    nodes = prod(size(risk_matrix))
    adj_matrix = spzeros(Int, nodes, nodes)
    for (y, x) = Iterators.product(1:size(risk_matrix, 1), 1:size(risk_matrix, 2))
        this_node_id = ((y-1) * size(risk_matrix, 1)) + x
        for (ny, nx) = [(y+1, x), (y, x+1)]
            try
                neighour_node_id = ((ny-1) * size(risk_matrix, 1)) + nx
                adj_matrix[this_node_id, neighour_node_id] = risk_matrix[ny, nx]
            catch
                continue
            end
        end
    end
    return SimpleWeightedDiGraph(adj_matrix) 
end

function read_chiton_data(data_file)
    lines = readlines(data_file)
    chiton_matrix = Array{Int}(undef, length(lines), length(lines[1]))
    for (ind, row) in enumerate(lines)
        chiton_matrix[ind, :] = parse.(Int, collect(row))
    end
    return chiton_matrix
end

function navigate_matrix(chiton_matrix)
    graph = risks_to_graph(chiton_matrix)
    path = enumerate_paths(dijkstra_shortest_paths(graph, 1), length(vertices(graph)))
    min_risk = sum([weights(graph)[n1,n2] for (n1,n2) in zip(path[1:end-1], path[2:end])])
    return trunc(Int, min_risk)
end

function extend_matrix_scan(chiton_matrix)
    # Repeat the matrix 5 times, add one for each addition, and mod 9
    new_grid = zeros(Int, size(chiton_matrix).*5)
    h, w = size(chiton_matrix)
    for (y_rep, x_rep) = Iterators.product(0:4, 0:4)
        for (y, x) = Iterators.product(1:h, 1:w)
            new_x = x_rep * w + x
            new_y = y_rep * h + y
            new_grid[new_y, new_x] = chiton_matrix[y, x] + (y_rep + x_rep - 1)
        end
    end
    large_chiton = mod.(new_grid, 9) .+ 1
    # large_chiton[large_chiton.==0] .= 1
    println("Generated large data")
    return large_chiton
end

# chiton_matrix = read_chiton_data("james/rsc/15_chiton_risks.txt")
chiton_matrix = read_chiton_data("james/rsc/15_chiton_risks_smol.txt")
println("Part 1: $(navigate_matrix(chiton_matrix))")
println("Part 2: $(navigate_matrix(extend_matrix_scan(chiton_matrix)))")
