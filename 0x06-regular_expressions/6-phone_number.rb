#!/usr/bin/env ruby
# A regular expression, matches 10 numbers from 0-9
puts ARGV[0].scan(/^[0-9]{10}$/).join
