#!/usr/bin/env ruby
# A regular expression, matches a string that starts with h ends with n and has a single character in between
puts ARGV[0].scan(/^[0-9]{10}$/).join
