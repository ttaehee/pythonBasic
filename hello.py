print("__name__ = ", __name__)

def say_hello():
    print("Hello")
    
# 모듈로 사용되는 경우에는 테스트코드 실행 안되게
if __name__ == '__main__':
    say_hello()  # 테스트코드
