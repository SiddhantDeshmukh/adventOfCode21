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


# Read in the data to an array
data = readdlm("james/rsc/1_sonar_data.txt", '\t', Int, '\n')

# Part 1: Count increases
println(count_increases(data))

# Part 2: Sliding window increases
println(count_window_increases(data))