# 항해를 떠날 배를 선택하는 함수 
def chooseBoat() :
  print("1)매우 단단한 배 2)많은 대포가 달려있는 배 3)매우 빠른 배 ")
  boat = input("어떤 배로 항해를 시작하시겠습니까?\n")
  if boat == "1":
    print("매우 단단한 배를 타고 항해를 시작합니다.")
    return boat
  elif boat == "2":
    print("많은 대포가 달려있는 배를 타고 항해를 시작합니다.")
    return boat
  elif boat == "3":
    print("매우 빠른 배를 타고 항해를 시작합니다.")
    return boat
  else :
    print("존재하지 않는 배입니다. 배를 다시 선택해주세요.")
    return chooseBoat()

# 해적을 만나는 함수 
def meetPirate() :
  print("해적이 나타났습니다!")
  if boat == "3" :
    print("앗! 배가 너무 빨라서 해적선을 그냥 지나쳤습니다!")
    return 1
  else :
    print("해적과 맞서 싸울지, 항복할지 선택하세요.")
    fight = input("1)맞서 싸운다. 2)항복한다.\n")
    if fight == "1" :
      print("해적이 내는 문제를 맞추고 해적을 물리치세요!")
      print("치과의사가 좋아하는 아파트는?")
      if boat == "2" :
        print("대포에 겁먹은 해적이 보기를 줬습니다!")
        answer = input("1)이편한세상 2)자이아파트 3)롯데캐슬\n")
        if answer == "1":
          print("정답입니다! 해적을 물리쳤습니다.")
          return 1
        else :
          print("정답이 아닙니다! 해적에게 배를 빼앗겨 항구로 돌아갑니다.")
          return 0
      else :
        answer = input("정답을 띄어쓰기 없이 한글로 입력해주세요.\n")
        if answer == "이편한세상" :
          print("정답입니다! 해적을 물리쳤습니다.")
          return 1
        else :
          print("정답이 아닙니다! 해적에게 배를 빼앗겨 항구로 돌아갑니다.")
          return 0
    else :
      print("해적에게서 항복하고 항구로 돌아갑니다.")
      return 0

#빙하를 만나는 함수 
def meetGlacier():
  print("보물섬으로 가는 길목에는 세 개의 커다란 빙하가 있습니다.")
  print("하지만 비가 내리고 안개가 뒤덮혀 앞을 볼 수 없습니다.")
  print("왼쪽과 오른쪽을 선택하여 세 개의 빙하를 피해보세요!")
  ways = ["1","2","2"]
  i = 0
  boatNumber1 = 0
  goNext = 0
  for i in range(0,3):
    print(f"{i+1}번째 빙하를 피하기 위해서 어느 방향을 선택하시겠습니까?")
    chooseWay = input("1)왼쪽 2)오른쪽\n")
    if chooseWay == ways[i]:
      print(f"{i+1}번째 빙하를 무사히 통과하였습니다.")
    else :
      print("빙하와 부딪혔습니다.")
      if boat == "1" and boatNumber1 == 0 :
        print("배가 튼튼해서 빙하를 한 번 버텼습니다!")
        print("항해를 계속합니다")
        boatNumber1 = boatNumber1 + 1
      else :
        print("배가 빙하를 버티지 못하고 부셔졌습니다.")
        print("항구로 돌아갑니다.")
        goNext = 1
        break
  if goNext == 0:
    return 1
  else :
    return 0

#보물섬을 선택하는 함수 
def findIsland():
  print("이제 보물섬이 코 앞까지 다가왔습니다.")
  print("앞에 보이는 네 개의 섬 중 어느 섬이 보물섬일까요?")
  island = input("1)고양이 모양 섬 2)강아지 모양 섬 3)호랑이 모양 섬 4)코끼리 모양 섬\n")
  if island == '4':
    print("축하합니다! 보물섬을 찾고 어마어마한 보물을 얻게 되었습니다.")
    return 1
  else :
    print("아쉽지만 보물섬이 아니었습니다.")
    print("섬에 있던 악어가 배를 파괴해 버렸습니다!")
    print("항구로 돌아갑니다.")
    return 0
    

#항구로 돌아와 재시작하는 함수 
def backToHarbor():
  print("모험을 다시 시작하시겠습니까?")
  restart = input("1)모험을 다시 시작한다. 2)모험을 종료한다.\n")
  if restart == "1":
    print("모험을 다시 시작합니다.")
    return 1
  else :
    print("모험을 종료합니다.")
    return 0

#항해 시작 
print("당신은 배를 타고 보물섬을 찾기 위한 항해를 떠나려고 합니다.")
print("배가 부서지지 않게 조심하면서 보물섬을 찾아보세요!")
print("(모든 객관식 선택지는 숫자를 이용하여 입력해주세요)")
print("항구에는 세 가지 배가 있습니다.")
start = 1
while start == 1:
  boat = chooseBoat()
  meetpirate = meetPirate()
  if meetpirate == 1 :
    meetglacier = meetGlacier()
    if meetglacier == 1:
      findisland = findIsland()
      if findisland == 1:
        start = 0
      else :
        start = backToHarbor()
    else : 
      start = backToHarbor()
  else :
    start = backToHarbor()