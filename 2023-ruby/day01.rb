require_relative "common"

content = get_input("01")
# puts content


def extract_digits(line)
    dw = %w(zero one two three four five six seven eight nine)
    l = line.scan(/(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))/)
    l.map! do |els|
        el = els.first # resolve double grouping 🙄
        i = dw.index(el)
        # puts ">#{el}< --> #{i}"
        i ? i : el
    end
    "#{l.first}#{l.last}".to_i
end


digits = content.map {|line| extract_digits(line)}
puts digits
puts digits.sum