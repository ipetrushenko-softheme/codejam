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

def find_ones(nums)
  count = 0
  for el in nums
    if el == 1
      count += 1
    end
  end
  return count

end
n, = read_ints
res = 0
while n != 0
  nums = read_ints
  ones = find_ones(nums)
  if ones >= 2
    res += 1
  end
  n -= 1
end

print res