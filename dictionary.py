#1
print('\n1.')
word = {'che':'car','chen':'dust','cheng':'weight','chi':'eat'}
print(word)


#2
print('\n2.')
key = ['che', 'chen', 'cheng', 'chi']
value = ['car', 'dust', 'weight', 'eat']
zip1 = zip(key,value)
print(zip1)
word = dict(zip1)
print(word)


#3
print('\n3.')
name = ['qimeng', 'lengyiyi', 'xiangning', 'dailan']
sign = ['Aquarius', 'Sagittarius', 'Pisces', 'Gemini']
dictionary = dict(zip(name,sign))
print(dictionary)


#4
print('\n4.')
name = ('qimeng', 'lengyiyi', 'xiangning', 'dailan')
sign = ['Aquarius', 'Sagittarius', 'Pisces', 'Gemini']
dictionary = {name:sign}
print(dictionary)


#5
print('\n5.')
dictionary = dict(qimeng = 'Aquarius', lengyiyi = 'Sagittarius', xiangning = 'Pisces', dailan = 'Gemini')
print(dictionary)


#6
print('\n6.')
name = ['qimeng', 'lengyiyi', 'xiangning', 'dailan']
dictionary_name = dict.fromkeys(name)
print(dictionary_name)


#7
print('\n7.')
#del dictionary
print(dictionary)


#8
print('\n8.')
#dictionary.clear()
print(dictionary)


#9
print('\n9.')
print(dictionary['lengyi'] if 'lengyi' in dictionary else 'He/She is not in this dictionary.')


#10
print('\n10.')
print(dictionary.get('lengyiyi'))
print(dictionary.get('lengyi'))
print(dictionary.get('lengyi', 'Not in this dictionary'))


#11
print('\n11.')
sign_all = ['1', '2', 'Gemini', '4', '5', '6', '7', '8', 'Sagittarius', '10', 'Aquarius', 'Pisces']
nature = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
sign_dict = dict(zip(sign_all,nature))
print('xiangning sign', dictionary.get('xiangning'))
print('\nHer sign character is:\n\n', sign_dict.get(dictionary.get('xiangning')))


#12
print('\n12.')
print(dictionary.items())

print('')
for item in dictionary.items():
	print(item)

print('')
for key, value in dictionary.items():
	print('The sign of ', key, 'is ', value)

print('')
for key in dictionary.keys():
	print(key)

print('')
for value in dictionary.values():
	print(value)


#13
print('\n13.')
sign = dictionary
sign['biqi'] = 'Cancer'
print(sign)

print('')
sign['biqi'] = 'Virgo'
print(sign)

print('')
del sign['biqi']
print(sign)

if 'biqi' in sign:
	del sign['biqi']
else:
	print('None')


#14
print('\n14.')
import random
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print(randomdict)


#15
print('\n15.')
name = ['qimeng', 'lengyiyi', 'xiangning', 'dailan']
sign = ['Aquarius', 'Sagittarius', 'Pisces', 'Gemini']
dic1 = {i:j for i,j in zip(name, sign)}
print(dic1)


#16
print('\n16.')

































