#!/usr/bin/env ruby

patt = /hbt{2,5}n/
arg = ARGV[0]

match = arg.scan(patt)

match.each do |mat|
	print mat
	end
puts
