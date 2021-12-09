parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:

def get_parking_lot(l):
  tss=0
  ass=0
  oss=0
  d=dict()
  for k in l:
    for j in k:
      if j==1:
        tss=tss+1
        oss=oss+1
      elif j==2:
        tss=tss+1
        ass=ass+1
  d["total_slots"]=tss
  d["available_slots"]=ass
  d["occupied_slots"]=oss
  return d
print(get_parking_lot(parking_state))