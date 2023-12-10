require_relative "common"

lines = get_input "10"
@rows = lines.map { |line| line.split("") }

def find_start
    @rows.each.with_index do |rc, r|
        rc.each.with_index do |cc, c|
            if cc == "S"
                return [r, c]
            end
        end
    end
end

class Walker
    attr_accessor :rows, :position, :direction, :walked

    FIELDS = {
      "L" => [:up, :right],
      "F" => [:down, :right],
      "|" => [:up, :down],
      "-" => [:left, :right],
      "J" => [:left, :up],
      "7" => [:left, :down],
    }

    def initialize(rows)
        @rows = rows
    end

    def current_field
        r, c = position
        @rows.fetch(r, []).fetch(c, ".")
    end

    def reverse_direction
        case direction
        when :down then :up
        when :up then :down
        when :right then :left
        when :left then :right
        end
    end

    def step
        r, c = @position
        @position = case direction
                    when :up then [r - 1, c]
                    when :down then [r + 1, c]
                    when :right then [r, c + 1]
                    when :left then [r, c - 1]
                    end

        f = current_field

        puts "walking #{direction} to #{@position}, found #{f}"

        return false if current_field == "."
        return true if current_field == "S"

        ds = FIELDS[f]

        # non-matching field
        return false if !ds.include? reverse_direction

        # turn into new direction
        @direction = (ds - [reverse_direction]).first
        true
    end

    def walk_until_loop(start, d)
        @position = start
        @direction = d
        count = 0
        @walked = [start]
        loop do
            success = step
            return 0 if not success
            count += 1
            @walked << position
            return count if position == start
        end
    end

end

start = find_start
puts start.inspect
w = Walker.new(@rows)
num = 0
[:up, :down, :left, :right].each do |d|
    num = w.walk_until_loop(start, d)
    puts num.inspect
    break if num > 0
end

puts "PART 1: #{(num / 2).ceil}"

@loop_coords = w.walked
# puts @loop_coords.inspect

def is_field?(r, c, field)
    @rows.fetch(r, []).fetch(c, ".") == field
end

def loops_left(rt, ct)
    @loop_coords.select { |r, c| r == rt && c < ct && !is_field?(r,c,"-")}.size
end

def loops_above(rt, ct)
    @loop_coords.select { |r, c| c == ct && r < rt && !is_field?(r,c,"|")}.size
end

def colorize(text, color_code)
  "#{color_code}#{text}e[0m"
end

def red(text); colorize(text, "e[31m"); end
def green(text); colorize(text, "e[32m"); end


# inner_grid = Hash.new{[]}
inner = []
@rows.each.with_index do |rc, r|
    line = ""
    rc.each.with_index do |cc, c|
        if loops_left(r, c).odd? && loops_above(r, c).odd? && !@loop_coords.include?([r, c])
            inner << [r, c]
            line += "X"
        else
            line += @loop_coords.include?([r, c]) ? @rows.fetch(r, []).fetch(c, ".") : "."
        end
    end
    puts line
end

puts "PART 2: #{inner.size}"

