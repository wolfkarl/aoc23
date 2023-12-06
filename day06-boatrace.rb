require_relative "common"

input = get_input("06")

class Race 
    attr_accessor :time, :distance

    def self.from_array(a)
        r = Race.new
        r.time, r.distance = a 
        r
    end

    def distance_bested(seconds_pressed)
        d = (time-seconds_pressed)*seconds_pressed
        d > distance
    end

    def num_bested 
        (0..time).select{|t| distance_bested(t)}.length

        # technically, we'd just need the first and last won 
        # even more technically, we could binary search for the first and last
        # also there's probably a formula
    end
end

times, distances = input.map{|line| line.scan(/\d+/).map(&:to_i)}
races = [times, distances].transpose.map{|a| Race.from_array(a)}

nums_bested = races.map do |race|
    race.num_bested
end

puts "PART 1: #{nums_bested.reduce(:*)}"

large_time = (times.map(&:to_s)).join("").to_i
large_distance = (distances.map(&:to_s)).join("").to_i
large_race = Race.from_array([large_time, large_distance])

large_nb = large_race.num_bested 
puts "PART 2: #{large_nb}"