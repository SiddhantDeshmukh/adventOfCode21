# Sonar Sweep: Ack! You've lost your keys, let's use the submarine to find them
using DelimitedFiles

function count_increases(sensor_data)
    increases = 0
    for index = 2:length(sensor_data)
        if sensor_data[index] > sensor_data[index-1]
            increases += 1
        end
    end
    return increases
end

function count_window_increases(sensor_data)
    increases = 0
    for index = 2:(length(sensor_data)-2)
        window_1 = sum(sensor_data[index-1:index+1])
        window_2 = sum(sensor_data[index:index+2])
        if window_2 > window_1
            increases += 1
        end
    end
    return increases
end

data = readdlm("james/rsc/1_sonar_data.txt", '\t', Int, '\n')
println("Part 1: $(count_increases(data))")
println("Part 2: $(count_window_increases(data))")

# # For future reference, a gorgeous one-liner for this problem:
# increases(data, width) = sum(b > a for (a, b) in zip(data, data[width+1:end]))
# println("Part 1: $(increases(data, 1))")
# println("Part 2: $(increases(data, 3))")