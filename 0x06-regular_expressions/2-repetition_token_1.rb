#!/usr/bin/env ruby

patt = /hb{0,1}tn/
arg = ARGV[0]

match = arg.scan(patt)

match.each do |mat|
	print mat
	end
puts
