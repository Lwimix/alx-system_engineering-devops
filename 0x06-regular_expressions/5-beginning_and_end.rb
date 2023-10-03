#!/usr/bin/env ruby

patt = /h[\w]n/
arg = ARGV[0]

match = arg.scan(patt)

match.each do |mat|
	print mat
	end
puts
