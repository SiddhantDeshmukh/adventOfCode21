# https://adventofcode.com/2021/day/12
using AdventOfCode

input = readlines("./data/day_12_test.txt")

mutable struct Graph
  vertices::Array{String}
  adjacency::Matrix{Int}

  # Need to write my own pathfinding alg from (start -> end)
  # that allows for multiple traversals through big caves but not small caves
end
Graph(vertices) = Graph(vertices,
                        reduce(hcat, [[0 for j in 1:length(vertices)]
                                        for i in 1:length(vertices)]))

function find_vertices(input)
  vertices = []
  for line in eachrow(input)
    vs = split(line[1], "-")
    for v in vs
      if !(v in vertices)
        push!(vertices, v)
      end
    end
  end
  return vertices
end

function add_edge!(graph::Graph, head::String, tail::String)
  # undirected, add both edges
  i_h, i_t = findfirst(x->x==head, graph.vertices), findfirst(x->x==tail, graph.vertices)
  graph.adjacency[i_h, i_t] = 1
  graph.adjacency[i_t, i_h] = 1
end

function add_edges!(graph::Graph, input)
  for line in eachrow(input)
    (head, tail) = split(line[1], "-")
    add_edge!(graph, string(head), string(tail))
  end
end

function part_1(input)
  vertices = find_vertices(input)
  G = Graph(vertices)
  add_edges!(G, input)
  display(G.adjacency)
  println()
  println(G.vertices)
end
@info part_1(input)

function part_2(input)
  nothing
end
@info part_2(input)

