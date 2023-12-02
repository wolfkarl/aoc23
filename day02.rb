require_relative "common"

input = get_input "02a"




 #puts input.inspect

input.each do |i|
    d = /Game (?<id>.*): (?<rounds>((?<c>.*);)*)/.match(i)
    # d = /Game (.*):/.match(i)
    puts d.inspect
end
