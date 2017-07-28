def traffic():
	with open("traffic.txt", "r") as f:
		traffic = [data.strip().split() for data in f]

	d = {}
	for client, roomNumber, direction, time in traffic:
		if not roomNumber in d: #only first time room number appears
			d[roomNumber] = [-int(time)]
		else:
			d[roomNumber].append(-int(time) if direction == 'I' else int(time))

	for number in d.items():
		visitor = int(len(number[1])//2)
		print("Room {0}, {1} minute average visit, {2} visitors total".format(number[0], int(sum(number[1]))//visitor, visitor))

traffic()

# def traffic():
#     with open('traffic.txt', 'r') as f:
#         traffic = [data.strip().split() for data in f]
        
    
#     d = {}
#     for client, room_number, direction, time in traffic:
#         if not room_number in d: # only first time room number appears 
#             d[room_number] = [-int(time)]
#         else:
#             d[room_number].append(-int(time) if direction == 'I' else int(time))
#     for number in d.items():
#         visitor = int(len(number[1])//2)
#         print('Room {0}, {1} minute average visit, {2} visitor(s) total' 
#             .format(number[0], int(sum(number[1]))//visitor, visitor))
        
        
            
# traffic()