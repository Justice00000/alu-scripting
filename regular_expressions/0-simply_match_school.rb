#!/usr/bin/env ruby
## Check if the provided argument contains the word "School"

# Ensure that one argument is provided
if ARGV.length != 1
  puts "Usage: ruby regex_match.rb <input_string>"
  exit(1)
end

# Get the input string from the command-line argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /School/

# Use the match method to check for a match
if input_string.match?(pattern)
  puts "The provided argument contains the word 'School.'"
else
  puts "The provided argument does not contain the word 'School.'"
end
