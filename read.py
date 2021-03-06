data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count += 1 就是count = count + 1
		if count % 1000 == 0: # %是求餘數的意思
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
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
