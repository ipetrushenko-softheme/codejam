n = gets.to_i
dict = {
	"Icosahedron" => 20,
	"Cube" => 6,
	"Tetrahedron" => 4,
	"Dodecahedron" => 12,
	"Octahedron" => 8
}

count = 0
while n != 0
	figure = gets.chomp.to_s
	count += dict[figure]
	n -= 1
end
puts count

