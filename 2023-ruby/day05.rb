require_relative "common"

lines = get_input("05")


class Mapping
    attr_accessor :start, :target, :length

    def self.from_string(s)
        m = Mapping.new
        m.target, m.start, m.length = s.split(" ").map(&:to_i)
        m
    end

    def range
        (start..start+length-1)
    end 

    def contains?(s)
        range.include?(s)
    end

    def convert(s)
        s += target-start
    end

    def convert_range(r)
        offset = target-start
        (r.begin + offset .. r.end + offset)
    end

    def to_s
        "#{range} -> #{convert_range(range)}"
    end
end

class Converter 
    attr_accessor :levels

    def initialize(levels)
        @levels = levels
    end

    def convert_from_mappings(seed, mappings)
        mappings.each do |mapping|
            if mapping.contains? seed
                return mapping.convert(seed)
            end
            # if no mapping matches, seed stays identical
        end
        return seed
    end

    def convert_seed(seed)
        evolution = levels.map{|l, ms| seed = convert_from_mappings(seed, ms)}
        # puts evolution.inspect
        return evolution.last
    end

    # convert ranges for one level (with given mappings)
    def convert_ranges_for_mappings(mranges, mappings)

        converted_ranges = []

        mappings.each do |m|
            # puts "total: #{mranges.map(&:size).sum}"
            next_ranges = []

            mranges.each do |range|
                left, overlap, right = split_range(range, m.range)
                # puts "compare #{range}, #{m.range}:"
                # puts "LOR: " + [left, overlap, right].inspect
                next_ranges << left if left
                converted_ranges << m.convert_range(overlap) if overlap
                next_ranges << right if right
            end

            mranges = next_ranges
            # puts "next: " + next_ranges.inspect
            # puts "converted: " + converted_ranges.inspect
        end
        # return ranges that could be converted and those that stay as they are

        final = converted_ranges + mranges
        # puts "#{converted_ranges.length} conv + #{mranges.length} other = #{final.length}"
        # puts final.inspect
        # puts "final total: #{final.map(&:size).sum}"
        return final
    end

    def convert_ranges(lranges)
        levels.each do |l, mappings|
            lranges = convert_ranges_for_mappings(lranges, mappings)
        end

        lranges
    end
    


    def split_range(source, target)
        left, overlap, right = nil

        if source.begin < target.begin
            left =  Range.new(source.begin, [source.end, target.begin-1].min)
        end

        # overlap
        if target.include?(source.end) || target.include?(source.begin)
            overlap = Range.new([target.begin, source.begin].max, [source.end, target.end].min)
        end

        # right
        if source.end > target.end
            right = Range.new([target.end+1, source.begin].max, source.end )
        end

        return left, overlap, right

    end

end


seeds = []
levels = {}
current_level = 0

## First, read all mappings 

lines.each do |line|
    if line.start_with?("seeds:")
        seeds = line.scan(/\d+/).map(&:to_i)
        next
    end

    if line == ""
        next
    end

    if line.end_with?("map:")
        current_level += 1 unless levels[current_level].nil?
        levels[current_level] = []
        next 
    end
     
    # line with mappings
    m = Mapping.from_string(line)
    levels[current_level] << m 
    
end


## Then, resolve all seeds

# puts seeds.inspect
# puts levels.inspect

conv = Converter.new(levels)

converted_seeds = seeds.map{|seed| conv.convert_seed(seed) }
# puts converted_seeds.inspect

puts "PART 1: #{converted_seeds.min}"


## Naive method that runs forever

# converted_seeds_2 = []
# ranged_seeds = seeds.each_slice(2) {|a, b| (a..a+b-1).each{|seed| converted_seeds_2 << conv.convert_seed(seed)}}
# puts "PART 2: #{converted_seeds_2.min}"

ranges = []
seeds.each_slice(2) {|a,l| ranges << (a..a+l-1)}
# puts ranges.inspect

converted_ranges = conv.convert_ranges(ranges)
# puts converted_ranges.inspect
puts "PART 2: #{converted_ranges.map(&:begin).min}"
