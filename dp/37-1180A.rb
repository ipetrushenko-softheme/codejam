n = gets.chomp.to_i

def solve(n)
  dp = [0] * (n + 1)
  dp[1] = 1
  for i in 2...n+1 do
    dp[i] = dp[i-1] + 4*(i-1)
  end
  return dp[n]
end

puts solve(n)
