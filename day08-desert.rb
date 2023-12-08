require_relative "common"

lines = get_input "08"

@path = nil
@nodes = {}

lines.each do |line|
    unless @path
        @path = line.split("") 
        next
    end

    next if line == ""

    n, l, r = line.scan(/\w+/)
    @nodes[n] = {"L" => l, "R" => r}
end


def num_steps(start)
    j = 0
    node = @nodes[start]
    @path.cycle do |p|
        j += 1

        target = node[p]
        break if target.end_with? "Z"
        node = @nodes[target]
        # break if j > 1000000000000
    end
    return j
end

steps_aaa = num_steps("AAA")
puts "PART 1: #{steps_aaa}"

ghost_nodes = @nodes.select{|n, _| n.end_with?("A")}.keys
steps = ghost_nodes.map{|gn| num_steps(gn)}
# puts steps.inspect

puts "PART 2: #{steps.reduce(:lcm)}"
