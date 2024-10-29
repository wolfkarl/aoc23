require_relative 'common'
lines = get_input "15"
inputs = lines.join.split(",")

def hash_char(char, cv = 0)
    ascii = char.ord
    cv += ascii
    cv *= 17
    cv % 256
end

def hash_string(str)
    str.split("").reduce(0) { |cv, char| hash_char(char, cv) }
end

hashes = inputs.map { |i| hash_string(i) }
# puts hashes.inspect

puts "PART 1: #{hashes.sum}"

boxes = Hash.new
(0...256).each {|k| boxes[k] = {}}

inputs.each do |i|
    if i.end_with? "-"
        label, = i.split("-")
        box_no = hash_string(label)
        boxes[box_no].delete(label)
    else
        label, focal = i.split "="
        box_no = hash_string(label)
        boxes[box_no][label] = focal.to_i
        # puts boxes[box_no]
    end
end

powers = boxes.map do |box_no, box|
    box_powers = box.map.with_index(1) {|label_lens, li| li * (box_no+1) * label_lens[1]}
    # puts box_powers.inspect
    box_powers.sum
end

# puts powers.inspect
puts "PART 2: #{powers.sum}"


