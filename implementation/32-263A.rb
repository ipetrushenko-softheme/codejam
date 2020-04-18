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


r_1, c_1 = 0, 0
(0...5).each { |r|
  row = read_ints
  c = row.find_index(1)
  if c != nil
    r_1, c_1 = r, c
  end
}

def solve(row, col)
  dest_r, dest_c = 2, 2
  return (dest_r - row).abs + (dest_c - col).abs
end


print(solve(r_1, c_1))