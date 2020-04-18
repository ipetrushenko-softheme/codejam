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


n, m, k = read_ints

if n <= m and n <= k
  print "Yes"
else
  print "No"
end
