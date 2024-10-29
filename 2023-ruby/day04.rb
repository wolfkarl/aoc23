require_relative "common"

lines = get_input("04")

def num_winning(line, points=true)
    game, numbers = line.split(":")
    drawn_raw, mine_raw = numbers.split("|")
    drawn = drawn_raw.scan(/\d+/).map{|n| n.to_i}
    mine = mine_raw.scan(/\d+/).map{|n| n.to_i}

    winning = mine.intersection(drawn)

    numw = winning.length
end

scores = lines.map do |line|
    numw = num_winning(line)
    numw > 0 ? 2**(numw-1) : 0
end

puts "PART 1: #{scores.sum}"


card_copies = Hash.new(1)
(0..lines.length-1).each {|j| card_copies[j] = 1}


lines.map.with_index do |line, i|
    numc = card_copies[i]
    numw = num_winning(line)
    # puts "card #{i} wins #{numw}"
    # puts card_copies.inspect
    if numw > 0
        (i+1..i+numw).each do |i|
            card_copies[i] += numc
        end
    end

end

score2 = card_copies.values.sum
# puts card_copies.inspect
puts "PART 2: #{score2}"



