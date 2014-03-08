def count_words(arr)
	hash = Hash.new(0)
	for word in arr
		hash[word] += 1
	end
	print_hash(hash)
	return hash
end

def print_hash(hash)
	for key in hash.keys
		puts key + " : " + hash[key].to_s
	end
end

count_words(ARGV)