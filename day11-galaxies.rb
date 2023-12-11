require_relative "common"

lines = get_input("11")

class Grid

    attr_accessor :rows, :default, :row_sizes, :col_sizes

    def initialize(lines)
        @rows = lines.map { |line| line.split("") }
        @row_sizes = Hash.new { 1 }
        @col_sizes = Hash.new { 1 }
    end

    def width
        @rows.first.size
    end

    def height
        @rows.size
    end

    def dimensions
        [width, height]
    end

    def at(r, c)
        @rows.fetch(r, []).fetch(c, default)
    end

    def straight_distance(p1, p2)
        r1, c1 = p1
        r2, c2 = p2
        dr = ([r1, r2].min...[r1, r2].max).map { |r| @row_sizes.fetch(r, 1) }.sum
        dc = ([c1, c2].min...[c1, c2].max).map { |c| @col_sizes.fetch(c, 1) }.sum
        # puts "distance: #{p1} to #{p2} = #{dr}r, #{dc}c, total #{dr + dc}"
        dr + dc
    end

    def each_row(&block)
        rows.each_with_index(&block)
    end

    def each_column(&block)
        (0...width).each do |ci|
            col = @rows.map { |row| row[ci] }
            block.call(col, ci)
        end
    end

    def each_cell(&block)
        rows.each_with_index do |row, r|
            row.each_with_index do |cell, c|
                block.call(r, c, cell)
            end
        end
    end

    def insert_row(before, content)
        rows.insert(before, Array.new(width, content))
    end

    def insert_column(before, content)
        rows.map! do |row|
            row.insert(before, content)
        end
    end

    def set_expansion(expansion)
        each_row do |row, i|
            if row.all? { |c| c == "." }
                row_sizes[i] = expansion
            end
        end

        each_column do |col, i|
            if col.all? { |c| c == "." }
                col_sizes[i] = expansion
            end
        end

    end
end

g = Grid.new(lines)
puts g.dimensions.inspect

galaxies = []
g.each_cell do |r, c, content|
    galaxies << [r, c] if content == "#"
end

g.set_expansion(2)

distances = galaxies.combination(2).map do |g1, g2|
    g.straight_distance(g1, g2)
end

# puts distances.inspect
#
puts "PART 1: #{distances.sum}"

g.set_expansion(1_000_000)
distances = galaxies.combination(2).map do |g1, g2|
    g.straight_distance(g1, g2)
end
puts "PART 2: #{distances.sum}"

