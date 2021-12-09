# Search for the Seven Segments! Displays busted, let's figure out how

function parse_segments(data_path)
    return map((x)->split.(x, " ", keepempty=false), split.(readlines(data_path), "|"))
end

function count_unique_segments(display_data)
    """In each out the outputs (2), count the number of times 1, 4, 7, and 8
    appear, as they use a unique number of segments (2, 4, 3, 7)"""
    total_count = 0
    for row in display_data
        total_count += count((y)->(x = length(y); x==2 || x==4 || x==3 || x==7), row[2])
    end
    return total_count
end

function decode_outputs(display_data)
    """Using the reference inputs, deduce the segment assignements and the value of the output, 
    returning the sum of all outputs"""
    
    function identify_segments(reference_data)
        # We can identify 1, 4, 7, 8
        #   a 
        #  b c 
        #   d
        #  e f 
        #   g

        # Extract useful initial known information about segment display
        ref_lengths = [length(x) for x in reference_data]
        one = reference_data[findall(x->x==2, ref_lengths)][1]
        four = reference_data[findall(x->x==4, ref_lengths)][1]   
        seven = reference_data[findall(x->x==3, ref_lengths)][1]
        eight = reference_data[findall(x->x==7, ref_lengths)][1]
        five_lens = reference_data[findall(x->x==5, ref_lengths)] # 2, 3, 5
        six_lens = reference_data[findall(x->x==6, ref_lengths)] # 0, 6, 9

        # a = difference between 7 and 1
        a = [char for char in seven if !(char in one)][1]
        # g = value in single-values six_lens after deleting four + a 
        g = " "
        for num in six_lens
            # Remove 4 + a 
            diff = [char for char in num if !(char in string(four, a))]
            if length(diff) == 1
                g = diff[1]
            end
        end
        # Can get e from 8 - (4 + a + g)
        e = [char for char in eight if !(char in string(four, a, g))][1]
        # Can use one to differentiate 6 from 0,9
        six = ""
        for (ind, s) in enumerate(six_lens)
            start_len = length(s)
            # Remove all elements of one 
            for val in one
                s = replace(s, val=>"")
            end
            end_len = length(s)
            # If only 1 shorter, is 6!
            if start_len - end_len == 1
                six = six_lens[ind]
            end
        end
        # Get f from intersect between one/six, then c is the remaining character in one
        f = [char for char in one if char in six][1]
        c = replace(one, f=>"")[1]

        # Common elements in five_lens=adg, so d is any five_len without common AND a,g
        fives_common = [char for char in five_lens[1] if (char in five_lens[2]) && (char in five_lens[3])]
        d = [char for char in fives_common if !(char in string(a, g))][1]
        # b is the last unassigned character
        b = [char for char in "abcdefg" if !(char in string(a,c,d,e,f,g))][1]

        # I have the full mapping!
        return Dict(a=>'a', b=>'b', c=>'c', d=>'d', e=>'e', f=>'f',g=>'g')         
    end

    function apply_correction(data, correction_map)
        corrected_segments = []
        for num in data
            corrected = join(correction_map[char] for char in num)
            sorted = join(sort([a for a in corrected]))
            push!(corrected_segments, sorted)
        end
        return corrected_segments
    end

    segments_to_number = Dict(
        "abcefg"=>0,
        "cf"=>1,
        "acdeg"=>2,
        "acdfg"=>3,
        "bcdf"=>4,
        "abdfg"=>5,
        "abdefg"=>6,
        "acf"=>7,
        "abcdefg"=>8,
        "abcdfg"=>9
    )

    total_output = 0
    for row in display_data
        # Create segment map
        segment_correction = identify_segments(row[1])
        # Convert output segments to corrected segments
        corrected_segments = apply_correction(row[2], segment_correction)
        # Parse as a number using segments_to_number
        outputs_numbers = join(segments_to_number[seg] for seg in corrected_segments)
        output = parse(Int, outputs_numbers)
        # Add to total
        total_output += output
    end
    return total_output
end

segment_data = parse_segments("james/rsc/8_segment_patterns.txt")
println("Part 1: $(count_unique_segments(segment_data))")
println("Part 2: $(decode_outputs(segment_data))")
