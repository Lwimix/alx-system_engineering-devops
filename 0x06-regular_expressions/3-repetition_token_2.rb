#!/usr/bin/env ruby

patt = /hbt+n/
arg = ARGV[0]

match = arg.scan(patt)

match.each do |mat|
	print mat
	end
puts
