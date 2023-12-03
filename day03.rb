require_relative "common"


class Grid

    attr_accessor :rows, :stars

    def initialize(rows)
        @rows = rows
        @stars = Hash.new {[]}
    end

    def has_adjacend_symbols?(r, cs)
        symbol_in_range?(r-1..r+1, cs.begin-1..cs.end+1)
    end


    def symbol_in_range?(rs, cs)
        rs.each do |r|
            cs.each do |c|
                return true if is_symbol?(r,c)
            end
        end
        false
    end

    def is_symbol?(r, c)
        is_regex?(r,c,/[^\d\.]/)
    end

    def is_regex?(r, c, pattern)
        return false if r < 0 || c < 0
        return false if r >= rows.length || c >= rows[0].length
        s = rows[r][c]
        s =~ pattern
    end

    def get_adjacent_stars(r, cs, number)
        (r-1..r+1).each do |r|
            (cs.begin-1..cs.end+1).each do |c|
                if is_regex?(r,c,/\*/)
                    stars["#{r}x#{c}"] += [number]
                end
            end
        end
    end


end

rows = get_input "03"
grid = Grid.new(rows)

symbol_numbers = []

grid.rows.each_with_index do |row, r|
    row.gsub(/\d+/).each do |n| # gsub works, scan doesn't
        match = Regexp.last_match

        if grid.has_adjacend_symbols?(r, match.begin(0)..match.end(0)-1)
            symbol_numbers << n.to_i
        end 
    end
end

# puts symbol_numbers.inspects
puts "PART 1: #{symbol_numbers.sum}"

grid.rows.each_with_index do |row, r|
    row.gsub(/\d+/).each do |n| # gsub works, scan doesn't
        match = Regexp.last_match
        grid.get_adjacent_stars(r, match.begin(0)..match.end(0)-1,n.to_i)
    end
end

ratios = grid.stars.select{|k,v| v.length > 1}
ratio_sum = ratios.map {|k, v| v.reduce(:*)}.sum

puts "PART 2: #{ratio_sum}"


