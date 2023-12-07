require_relative "common"
lines = get_input("07")

class Hand
    include Comparable 
    attr_accessor :cards, :bid, :wildcard

    @@wildcard = nil
    def self.wildcard=(wc); @@wildcard = wc; end

    def self.from_line(line)
        h = Hand.new
        h.cards, bid = line.split(" ")
        h.bid = bid.to_i
        h
    end

    def rank_type

        icards = cards.split("")

        # remove wildcards from set
        if @@wildcard
            icards.delete(@@wildcard)
            num_wcs = cards.length - icards.length
        end

        chist = icards.tally.values.sort.reverse

        # add wildcards to most common card
        if @@wildcard
            begin
                chist[0] = 0 if chist.empty?
                chist[0] += num_wcs
            rescue
                puts [cards, icards].inspect
            end
        end

        return 7 if chist[0] == 5
        return 6 if chist[0] == 4
        return 5 if chist[0] == 3 and chist[1] == 2
        return 4 if chist[0] == 3
        return 3 if chist[0] == 2 and chist[1] == 2
        return 2 if chist[0] == 2
        return 1
    end

    def card_value(card)
        special = {"T" => 10, "J" => 11, "Q" => 12, "K" => 13, "A" => 14}
        special[@@wildcard] = 0
        special.fetch(card, card.to_i)
    end

    def absolute_rank
        ar = 0
        mag = 0
        base = 100
        cards.split("").reverse.each do |c|
            cv = card_value(c)
            ar += cv * (base**mag)
            mag += 1
        end
        ar += rank_type * (base**mag)
        ar
    end

    def <=>(other)
        return absolute_rank <=> other.absolute_rank
    end

end

hands = lines.map{|l| Hand.from_line(l)}
hands.sort!

winnings = hands.map.with_index do |hand, i|
    hand.bid * (i+1)
end

puts "PART 1: #{winnings.sum}"

Hand.wildcard = "J"
hands.sort!
winnings = hands.map.with_index do |hand, i|
    hand.bid * (i+1)
end

puts "PART 2: #{winnings.sum}"
    



