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

arr = read_ints()

def solve(arr)
  maximum = arr.max
  arr.each { |el|
    if el != maximum
      print "#{maximum - el} "
    end
  }
end

solve(arr)
