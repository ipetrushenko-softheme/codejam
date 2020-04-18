n = gets.chomp.to_i

def solve(n)
  count = 0
  (1..n/2).each { |i|
    diff = n - i
    if diff % i == 0
      count += 1
    end
  }

  return count
end


print solve(n)