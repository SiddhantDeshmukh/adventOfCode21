# Vent Horizon! Don't hit the hydrothermal vents
using LazySets 

function parse_vents(segment_file)
    all_segments = readlines(segment_file)
    split_coords = map((x)->split.(x, ","), split.(all_segments, "->"))
    point_coords = map((x)->parse.(Float32, collect(Iterators.flatten(x))), split_coords)
    line_segments = map((x)->LineSegment(x[1:2], x[3:4]), point_coords)
    return line_segments
end

function not_diag(seg)
    return seg.p[1] == seg.q[1] || seg.p[2] == seg.q[2]
end

function overlapping_ints(seg)
    positions = []
    xs = [seg.p[1], seg.q[1]]
    ys = [seg.p[2], seg.q[2]]
    for x = minimum(xs):maximum(xs)
        for y = minimum(ys):maximum(ys)
            if in([x, y], seg)
                push!(positions, [x, y])
            end
        end
    end
    return positions
end

function count_intersections(segments; allow_diag = false)
    """Count the number of intersections between these vent sections"""
    intersection_points = Set()
    for (seg1, seg2) in Iterators.product(segments, segments)
        if (allow_diag || (not_diag(seg1) && not_diag(seg2))) && (seg1 != seg2)
            if !isdisjoint(seg1, seg2)
                inter = intersection(seg1, seg2)
                if inter isa Singleton
                    push!(intersection_points, [element(inter, 1), element(inter, 2)])
                else
                    for point = overlapping_ints(inter)
                        push!(intersection_points, point)
                    end
                end
            end
        end
    end
    return length(intersection_points)
end

function part_2_alternative(vent_segments)
    # Create 2d array of correct size
    all_x, all_y = [], [] 
    for seg in vent_segments
        push!(all_x, seg.p[1])
        push!(all_x, seg.q[1])
        push!(all_y, seg.p[2])
        push!(all_y, seg.p[2])
    end
    max_x, max_y = trunc(Int, maximum(all_x)), trunc(Int, maximum(all_y))
    vent_map = zeros((max_x+1, max_y+1))
    # Add one at each line point
    for seg in vent_segments
        points = overlapping_ints(seg)
        for point in points
            vent_map[trunc(Int, point[1])+1, trunc(Int, point[2])+1] += 1
        end
    end
    # Count points > 1
    intersect_points = sum((x)->x>1, Iterators.flatten(vent_map))
    return intersect_points
end

vent_segments = parse_vents("james/rsc/5_vent_segments.txt")
println("Part 1: $(count_intersections(vent_segments))")
println("Part 2: $(part_2_alternative(vent_segments))")

