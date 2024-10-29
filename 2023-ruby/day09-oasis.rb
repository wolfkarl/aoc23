require_relative "common"

lines = get_input "09"

def guess_sequence(seq)
    steps = [seq]
    loop do
        current = steps.last
        break if current.all? {|n| n == 0}
        nxt = []
        current.each_cons(2) do |a, b|
            nxt << b - a
        end
        steps << nxt
    end

    filler = 0
    steps.reverse.map! do |step|
        newlast = step.last + filler
        step << newlast
        filler = newlast
    end
    
    steps.first.last
end

seqs = lines.map{|line| line.split(" ").map(&:to_i)}

future_elems = seqs.map{|seq| guess_sequence(seq)}

puts "PART 1: #{future_elems.sum}"

past_elems = seqs.map{|seq| guess_sequence(seq.reverse)}

puts "PART 2: #{past_elems.sum}"