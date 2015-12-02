class Player3:
	cnt = 0
	dep = 4
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		a = -100000000
		b = 100000000
		return self.alphabeta(temp_board[:],temp_block[:] ,self.dep , a , b, True,old_move,flag)
	
	def alphabeta(self,board ,block ,depth , a , b,maximizingPlayer,old_move,flag):
		if(depth == 0):
			#print flag
			return self.heu(board,block,flag)

		if maximizingPlayer:
			v = -100000
			cells = self.get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			#list of possible moves
			#print cells
			if(len(cells)==0):
				cells = get_empty_out_of(board,range(0,8),block);

			temp = cells[0];

			random.shuffle(cells)
			for i in cells:
				
				temp_block = ['-']*9
				for j  in range(0,len(block)):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)

				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				
				update_lists(temp_board,temp_block,i,flag)
				vtemp = self.alphabeta(temp_board,temp_block,depth - 1, a , b , False,i,flag)				
				#print vtemp, i, depth, old_move , 0 , a , b
				if(vtemp > v):
					v = vtemp
					temp = i
				
				a = max(a,v)
				if(b <= a):
					#print vtemp, temp_block, i, depth, 0
					break

			if(depth == self.dep):
				return temp
			else:
				return v
		else:
			v = 100000
			cells = get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			if(len(cells)==0):
				cells = get_empty_out_of(board,range(0,8),block);
			temp = cells[0];
			random.shuffle(cells)
	
			for i in cells:
		
				temp_block = ['-']*9
				for j in range(0,9):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)
				
				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				
				flag1 = ''
				if flag == 'x':
					flag1 = 'o'
				elif flag == 'o':
					flag1 = 'x'
				
				update_lists(temp_board , temp_block , i ,flag1 )
				vtemp = self.alphabeta(temp_board,temp_block,depth - 1, a , b , True,i,flag)
				#print vtemp, i, depth , old_move , a, b  , -1
			
				if(vtemp < v):
					v = vtemp
					temp = i

				b = min(b,v)
				#print a, b, old_move
				if(b <= a):
					#print vtemp, temp_block, i, depth, -1
					break
			return v

	def check(self,i,board,flag):
		row = (i / 3) * 3
		col = (i % 3) * 3
		block = ['-']* 9
		cnt = 0
		for i in range(row,row+3):
			for j in range(col, col + 3):
				block[cnt] = board[i][j]
				cnt += 1
		
		count1 = 0
		count2 = 0
		value = 0

		for i in range(0,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 0

			elif(count1==1):
				value += 2.5

			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(3,6):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 0
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(6,9):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(0,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(1,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(2,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(0,9,4):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 10;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		count1 = 0
		count2 = 0
		for i in range(2,7,2):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 2.5;

			if(count2==2):
				value -= 5;

			if(count2==3):
				return -10;

		elif(count2==0):
			if(count1==0):
				value += 1
			elif(count1==1):
				value += 2.5
			elif(count1==2):
				value += 5
			else:
				return 1;

		else:
			if(count1 < count2):
				value += 2
			elif(count1 == count2):
				value += 1
			else:
				value -= 1

		return value;


	def heu(self,board,block,flag):
		count1 = 0
		count2 = 0
		value = 0

		for i in range(0,9):
			if i in [0,2,6,8]:
				value +=  3 * self.check(i,board,flag)
			elif i == 4:
				value += 4 * self.check(i,board,flag)
			else:
				value += 2 * self.check(i,board,flag)			


		for i in range(0,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 0

			elif(count1==1):
				value += 25

			elif(count1==2):
				for i in range(0,3):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(3,6):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 0
			elif(count1==1):
				value += 25
			elif(count1==2):
				for i in range(3,6):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(6,9):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 25
			elif(count1==2):
				for i in range(6,9):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(0,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 25
			elif(count1==2):
				for i in range(0,9,3):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		
		count1 = 0
		count2 = 0
		for i in range(1,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 25
			elif(count1==2):
				for i in range(1,9,3):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(2,9,3):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 25;

			if(count2==2):
				value -= 50;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 25
			elif(count1==2):
				for i in range(2,9,3):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(0,9,4):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 35;

			if(count2==2):
				value -= 60;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 35
			elif(count1==2):
				for i in range(0,9,4):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
			value -= 10

		count1 = 0
		count2 = 0
		for i in range(2,7,2):
			if(block[i]==flag):
				count1 += 1
			elif(block[i]!='-'):
				count2 += 1

		if(count1==0):
			if(count2==1):
				value -= 35;

			if(count2==2):
				value -= 60;

			if(count2==3):
				return -1000;

		elif(count2==0):
			if(count1==0):
				value += 10
			elif(count1==1):
				value += 35
			elif(count1==2):
				for i in range(2,7,2):
					if(block[i]=='-'):
						temp_cond = self.check(i,board,flag)
						if(temp_cond < 0):
							value -= 50
						else:
							value += 60
			else:
				return 1000;

		else:
				value -= 10

		return value;

	def get_empty_out_of(self, gameb, blal, block_stat):
		cells = []  # it will be list of tuples
		#Iterate over possible blocks and get empty cells
		for idb in blal:
			id1 = idb/3
			id2 = idb%3
			for i in xrange(id1*3, id1*3+3):
				for j in xrange(id2*3, id2*3+3):
					if gameb[i][j] == '-':
						cells.append((i,j))

		# If all the possible blocks are full, you can move anywhere
		if cells == []:
			for i in xrange(9):
				for j in xrange(9):
					no = (i/3)*3 + (j/3)
					if block_stat[no] == '-' and gameb[i][j] == '-':
						cells.append((i,j))
		return cells

	
	def blocks_allowed(self,old_move,block_stat):
		for_corner = [0,2,3,5,6,8]
		blocks_allowed  = []
		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0,1,3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2,5,8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5,8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]

			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)

		else:
			#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]

			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
			
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]

			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

		for i in reversed(blocks_allowed):
			if block_stat[i] != '-':
				blocks_allowed.remove(i)

        	return blocks_allowed
