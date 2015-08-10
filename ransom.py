def ransom_note(note, magazine):
	m_dict = dict()
	ml= len(magazine)
	nl= len(note)
	for i in range(ml):
		if m_dict.has_key(magazine[i]):
			m_dict[magazine[i]]+=1
		else:
			m_dict[magazine[i]]=1
	for i in range(nl):
		if m_dict.has_key(note[i]) and m_dict[note[i]]>0:
			m_dict[magazine[i]]-=1
		else:
			return False
	return True
def ransom_note1(note, magazine):
	sortedmagazine = list(magazine)
	sortedmagazine.sort()
	sortednote = list(note)
	sortednote.sort()
	ml= len(magazine)
	nl= len(note)
	j=0
	for i in range(nl):
		ifound = False
		while j<ml:
			if sortednote[i]==sortedmagazine[j]:
				j+=1
				ifound = True
				break
			elif sortednote[i]>sortedmagazine[j]:
				j+=1
				continue
			else:
				return False
		if not (ifound):
			return False
	return True

print ransom_note1('qwerty', 'asdfgh')
print ransom_note1('qtwerty', 'qwerty')