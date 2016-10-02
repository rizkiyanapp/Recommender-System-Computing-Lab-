import math

# KAMUS DATA
data = [[0 for user in range(6)] for item in range(6)]
itemUserF = []

# fungsi untuk memasukkan nilai rating item kedalam tabel
# I.S : array data kosong
# F.S : array terisi rating item setiap usernya
def createMatrix() :
	data[0][0] = 2
	data[0][3] = 4
	data[0][4] = 5
	data[1][0] = 5
	data[1][2] = 4
	data[1][5] = 1
	data[2][2] = 5
	data[2][4] = 2
	data[3][1] = 1
	data[3][3] = 5
	data[3][5] = 4
	data[4][2] = 4
	data[4][5] = 2
	data[5][0] = 4
	data[5][1] = 5
	data[5][3] = 1

# fungsi untuk menampilkan isi tabel
def showMatrix() :
	for x in range(6) :
		print data[x]

# fungsi untuk menunjukkan user tsb me-rate item apa saja
# I.S : arrItem kosong
# F.S : arrItem berisi item yang di rate user tsb
def userItem(user, arrItem) :
	for i in range(6) :
		if data[user][i] != 0 :
			arrItem.append(data[user].index(data[user][i]))

# fungsi untuk menunjukkan item tsb di rate user siapa saja
# I.S : arrUser kosong
# F.S : arrUser berisi user yang me-rate item tsb
def itemUser(item, arrUser) :
	for i in range(6) :
		if data[i][item] != 0 :
			arrUser.append(i)

# fungsi untuk menunjukkan user tsb bertetanggaan dengan user siapa saja
# I.S : arrUser kosong
# F.S : arrUser berisi user yang bertetanggaan dengan user yg dicari
def userNeighbor(user, arrUser) :
	arrUserFind = []
	arrUserItemFound = []
	userItem(user, arrUserFind)
	for i in range(6) :
		arrUserItemFound = []
		if i != user :
			userItem(i, arrUserItemFound)
			ketemu = False
			j = len(arrUserFind)
			while (ketemu == False and j > 0) :
				if arrUserFind[-j] in arrUserItemFound :	# untuk mengecek apakah item di user A di rate oleh user B
					ketemu = True							# jika ya maka user tsb akan ditampung ke dalam array arrUser
					arrUser.append(i)
				else :
					j -= 1

# fungsi untuk menghitung rata - rata rating item user tsb
# I.S : result kosong
# F.s : result berisi hasil rata - rata nilai rating semua item pada user tsb
def averageUser(user) :
	total = 0.0
	count = 0.0
	for i in range(len(data[user])) :
		if data[user][i] != 0 :
			total += data[user][i]
			count += 1
	result = total / count
	return result

# fungsi untuk menghitung nilai similaritas antar user A dan user B
# I.S : result kosong
# F.S : result berisi hasil perhitungan dari rumus Similarity userA dengan userB
def similarity(userA, userB) :
	arrUserItemA = []
	arrUserItemB = []
	arrItem = []
	up = 0.0
	down = 0.0
	temp = 0.0
	avgUserA = averageUser(userA)
	avgUserB = averageUser(userB)
	userItem(userA, arrUserItemA)
	userItem(userB, arrUserItemB)
	arrItem = list(set(arrUserItemA) & set(arrUserItemB))
	for i in range(len(arrItem)) :
		up += (data[userA][arrItem[i]] - averageUser(userA)) * (data[userB][arrItem[i]] - averageUser(userB))
		down += (data[userA][arrItem[i]] - averageUser(userA)) ** 2
		temp += (data[userB][arrItem[i]] - averageUser(userB)) ** 2
	down *= temp
	result = up / math.sqrt(down)
	return result

# fungsi untuk menghitung nilai predicted rating item pada user tsb
# I.S : result kosong
# F.S : result berisi hasil perhitungan dari rumus Predicted Rating user terhadap item tsb
def predictedRating(user, item) :
	arrUserNeighbor = []
	arrUserNeighborItem = []
	up = 0.0
	down = 0.0
	userNeighbor(user, arrUserNeighbor)
	for i in range(len(arrUserNeighbor)) :
		if data[arrUserNeighbor[i]][item] != 0 :
			arrUserNeighborItem.append(arrUserNeighbor[i])
	for j in range(len(arrUserNeighborItem)) :
		up += similarity(user, arrUserNeighborItem[j]) * (data[arrUserNeighborItem[j]][item] - averageUser(arrUserNeighborItem[j]))
	for k in range(len(arrUserNeighbor)) :
		if (similarity(user, arrUserNeighbor[k]) < 0) :
			temp = - (similarity(user, arrUserNeighbor[k]))
			down += temp
		else :
			down += similarity(user, arrUserNeighbor[k])
	result = averageUser(user) + (up / down)
	return result



createMatrix()

# memasukkan rating user 5 ke dalam array itemUserF
for value in data[5] :
	itemUserF.append(value)

itemUserF[2] = predictedRating(5,2)
itemUserF[4] = predictedRating(5,4)
itemUserF[5] = predictedRating(5,5)

print "Predicted Rating User F :"
print itemUserF # after predicted rating assigned for user 5