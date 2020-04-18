n = gets.chomp.to_i

def solve(n)
  monets = [1, 5, 10, 20, 100].reverse
  count = 0
  for monet in monets
    while n - monet >= 0
      n = n - monet
      count += 1
    end
  end
  return count
end

puts solve(n)