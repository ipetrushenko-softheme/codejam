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


n = gets.chomp.to_i
s = gets.chomp.to_s
dict = {}
s.each_char { |el|
  if dict.key?(el)
    dict[el] += 1
  else
    dict[el] = 1
  end
}

zeros = dict["z"]
ones = dict["n"]
if ones != nil
  while ones > 0
    print "1 "
    ones -= 1
  end
end

if zeros != nil
  while zeros > 0
    print "0 "
    zeros -= 1
  end
end
