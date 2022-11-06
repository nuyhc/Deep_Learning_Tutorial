import argparse

# 기본
# 아무것도 하지 않는 간단한 예제
# parser = argparse.ArgumentParser()
# parser.parse_args()

# 위치 인자 소개
# parser = argparse.ArgumentParser()
# parser.add_argument("echo") # 프로그램이 받고 싶은 명령행 옵션을 지정 -> 프로그램 호출시 명령을 지정해야 함
# args = parser.parse_args() # 실제로 지정된 옵션으로부터 온 데이터를 돌려줌
# print(args)

# 개선
# -> echo가 위치 인자임을 볼 수 있지만, 추측하거나 소스 코드를 읽는 것 외에는 무엇을 하는지 모름 
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args =  parser.parse_args()
# print(args.echo)

# 기능 추가
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int) # 타입을 명시하지 않으면 문자열로 인식함
# args = parser.parse_args()
# print(args.square**2)

# 그럼 이건? -> 잘됨
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number") # 타입을 명시하지 않으면 문자열로 인식함
# args = parser.parse_args()
# print(int(args.square)**2)

# 옵션 인자 소개
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")
    
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true") # 옵션을 출력하는게 아니라 옵션을 그대로 저장하라는 의미
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# 짧은 옵션
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# 위치 및 옵션 인자 결합하기
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true", # 인자의 순서는 중요하지 않음
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)

# 정수 목록을 받아 합계 또는 최댓값을 출력하는 프로그램
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

https://docs.python.org/ko/3/library/argparse.html#module-argparse