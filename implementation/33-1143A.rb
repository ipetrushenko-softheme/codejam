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


n, = read_ints
doors = read_ints

def find_occ(arr, num)
  count = 0
  for el in arr
    if el == num
      count += 1
    end
  end
  return count
end

def solve(doors)
  k = 0
  zeros = find_occ(doors, 0)
  ones = find_occ(doors, 1)
  for i in 0...doors.length
    if zeros == 0 or ones == 0
      return k
    end
    if doors[i] == 0
      zeros -= 1
    elsif doors[i] == 1
      ones -= 1
    end
    k += 1
  end
  return k
end

print solve(doors)