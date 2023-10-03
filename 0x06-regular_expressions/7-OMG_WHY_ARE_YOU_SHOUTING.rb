#!/usr/bin/env ruby

patt = /[A-Z]/
arg = ARGV[0]

match = arg.scan(patt)

match.each do |mat|
	print mat
	end
puts
