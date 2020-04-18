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


q, = read_ints

def process_subset(nums, set)
  sum = []
  for i in 0...set.length
    if set[i] == 1
      sum.push(i)
    end
  end

  count = 0
  for i in 0...nums.length
    if sum.include? i
      count += nums[i]
    end
  end
  if count % 2 == 0 and count != 0
    return sum
  end

  return []
end

def compute_subset(nums, size, so_far)
  if size == 0
    return process_subset(nums, so_far)
  else
    compute_subset(nums, size - 1, so_far + [0])
    compute_subset(nums, size - 1, so_far + [1])
  end
end


while q != 0
  n, = read_ints
  nums = read_ints
  res = compute_subset(nums, nums.length, [])
  if res == []
    puts -1
  else
    puts res.length
    print res
    puts

  end

  puts res
  q = q - 1
end
