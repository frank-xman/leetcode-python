def groupAnagrams(strs):
		d={}
		for w in (strs):
				print(w)
				key=tuple(sorted(w))
				d[key]=d.get(key,[])+[w]
		return d.values()
