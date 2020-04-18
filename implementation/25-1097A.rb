def read_tokens
  return gets.chomp.to_s.strip.split(' ')
end

def read_ints
  data = []
  read_tokens.each { |s|
    data.push(s.to_i)
  }
  return data
end

table_card, = read_tokens
my_cards = read_tokens

def solve(table_card, my_cards)
  suit = table_card[0]
  rank = table_card[1]
  my_cards.each { |card|
    if card.include? suit or card.include? rank
      return "YES"
    end
  }
  return "NO"
end

ans = solve(table_card, my_cards)
print ans