data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count += 1 就是count = count + 1
		if count % 1000 == 0: # %是求餘數的意思
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

wc = {} #word_count
for d in data: #for loop裡還有for loop:Nested For Loop(巢狀迴圈)
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] >= 100:	
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('感謝使用此系統')

		break
	if word in wc:
		print(word, '出現過的字數是: ', wc[word])
	else:
		print('這個字沒出現過')












sum_len = 0 # 總長度
for d in data:
	x = len(d)
	sum_len = sum_len + x
print('留言平均長度為:', sum_len/1000000)
new = []
for d in data:
	if len(d) > 100:
		new.append(d)
print('一共有', len(new), '筆留言長度超過100')
print(new[0])
print(new[1])
good = []
for d in data:
	if 'good' in d:
		good.append(d)# 這裡的d更換的話28行的d也要更換，也就是說要把什麼裝進good的意思(也可以裝別的東西)
print('一共有', len(good), '筆留言提到good')
#以下為22~25的快寫法
good = [d for d in data if 'good' in d]
 for d in date:把data裡的資料拿出來叫d
if 'good' in d:如果d這個裡面有'good'的話就丟一個d(22[裡最前面那個東西)到good裡