class Player22:
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		a = -1000000000
		b = 1000000000
		#print "###########",flag,"---------";
		return self.alphabeta(temp_board[:],temp_block[:] ,4, a , b, True,old_move,flag)
	
	def alphabeta(self,board ,block ,depth , a , b,maximizingPlayer,old_move,flag):
		if(depth == 0):
		#	print flag
			return self.heu(board,block,flag)

		if maximizingPlayer:
			v = -1000000000
			
			cells = self.get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			if(len(cells)==0):
				cells = self.get_empty_out_of(board,range(0,8),block);

			temp = cells[0];

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

			if(depth == 4):
				return temp
			else:
				return v
		else:
			v = 1000000000
			
			cells = self.get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			if(len(cells)==0):
				cells = self.get_empty_out_of(board,range(0,8),block);
			temp = cells[0];

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
#				print a, b, old_move
				if(b <= a):
				#print vtemp, temp_block, i, depth, -1
					break
			return v

	def heu(self,board,block,flag):
		if(flag == 'x'):
			flag1 = 'o'
		else:
			flag1 = 'x'
		r = {(flag,flag,flag):100000,(flag1,flag1,flag1):-100000,(flag,flag,'-'):10000,(flag,'-',flag):10000,('-',flag,flag):10000,
		(flag1,flag1,'-'):-10000,(flag1,'-',flag1):-10000,('-',flag1,flag1):-10000,('-',flag,'-'):1000,('-','-',flag):1000,(flag,'-','-'):1000,
		(flag1,'-','-'):-1000,('-',flag1,'-'):-1000,('-','-',flag1):-1000}
		
		ans = 0
		for i in [0,3,6]:
			p = (block[i],block[i+1],block[i+2])
			if p in r.keys():
				ans += r[p]

		for i in [0,1,2]:
			p = (block[i],block[i+3],block[i+6])
			if p in r.keys():
				ans += r[p]

		p = (block[0],block[4],block[8])
		if p in r.keys():
			ans += r[p]
		p = (block[2],block[4],block[6])
		if p in r.keys():
			ans += r[p]

		for i in range(0,9):
			row = i/3
			col = i%3
			m = []
			for a in xrange(row*3,row*3+3):
				for b in xrange(col*3,col*3+3):
					m.append(board[a][b])
			for i in [0,3,6]:
				p = (m[i],m[i+1],m[i+2])
				if p in r.keys():
					ans += r[p]/1000

			for i in [0,1,2]:
				p = (m[i],m[i+3],m[i+6])
				if p in r.keys():
					ans += r[p]/1000

			p = (m[0],m[4],m[8])
			if p in r.keys():
				ans += r[p]/1000
			p = (m[2],m[4],m[6])
			if p in r.keys():
				ans += r[p]/1000					
		return ans
				

	def block_hue(num,board):
		a = []
		for i in range(3):
			row = ['-']*3
			board.append(row)
		
		row = (num/3)*3
		column = (num%3)*3
		for i in range(0,3):
			for j in range(0,3):
				a[i][j] = board[row+i][column+j]

		for i in range(0,3):
			count1 = 0
			count2 = 0
			if(a[i][0]=='X'):
				count1 += 1
						
			if(a[i][1]=='X'):
				count1 += 1
			else:
				count2 += 1
			if(a[i][2]=='X'):
				count1 += 1
	
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
