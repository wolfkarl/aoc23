require_relative "common"

input = get_input "02"

class Game
    attr_accessor :id, :throws

    def initialize
         @throws = {"red": [], "green": [], "blue": []}
    end

    def self.from_line(line)
    	game = Game.new
        d = /Game (?<id>.*): (?<rounds>.*)/.match(line)
    	game.id = d['id'].to_i
            d['rounds'].split(";").each do |round|
                round.split(",").each do |die|
    	        dd = die.split
    	        amount = dd[0].chomp
                    color = dd[1].chomp.to_sym
                    begin 
                        game.throws[color] << amount.to_i
                    rescue
                        puts "invalid color " + color.inspect
                    end 
                end
            end
        game
    end

    def possible?(max_dies)
         max_dies.each do |color, cmax| 
             return false if cmax < throws[color].max 
         end 
        true
    end 

    def min_set
	  throws.map{|c, ts| [c, ts.max]}.to_h
    end

    def min_set_power
        min_set.values.reduce(:*)
    end
	
end

games = input.map{|l| Game.from_line(l)}

possible_games = games.select{|g| g.possible?({:red => 12, :green => 13, :blue => 14})}
possible_id_sum = possible_games.sum(&:id)
puts "PART 1: #{possible_id_sum}"

min_set_power_sums = games.map{|g| g.min_set_power}.sum
puts "PART 2: #{min_set_power_sums}"
