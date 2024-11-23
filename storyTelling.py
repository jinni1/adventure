print("당신은 배를 타고 보물섬을 찾기 위한 항해를 떠나려고 합니다.")
print("배가 부서지지 않게 조심하면서 보물섬을 찾아보세요!")
print("(모든 객관식 선택지는 숫자를 이용하여 입력해주세요)")

print("항구에는 세 가지 배가 있습니다.")
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

boat = chooseBoat()

def meetPirate() :
  print("해적이 나타났습니다!")
  if boat == "3" :
    print("앗! 배가 너무 빨라서 해적선을 그냥 지나쳤습니다!")
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
        else :
          print("정답이 아닙니다! 해적에게 배를 빼앗겨 항구로 돌아갑니다.")
      else :
        answer = input("정답을 띄어쓰기 없이 한글로 입력해주세요.\n")
        if answer == "이편한세상" :
          print("정답입니다! 해적을 물리쳤습니다.")
        else :
          print("정답이 아닙니다! 해적에게 배를 빼앗겨 항구로 돌아갑니다.")
        
meetPirate()