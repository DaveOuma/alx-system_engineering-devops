#!/usr/bin/env ruby
# A regex expression accepting  one argument and passing it to a regular expression matching method

puts ARGV[0].scan(/School/).join
