print "type in fibonacci number : "
value = gets.chomp
ary = Array.new
ary[0] = ary[1] = 1
puts ary[0]
puts ary[0]
for i in ( 2...Integer( value ) )
  ary << ary[i-1] + ary[i-2]
  puts ary[i]
end
