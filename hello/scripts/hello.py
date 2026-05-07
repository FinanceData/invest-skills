import sys

def hello(name: str) -> str:
    """
    주어진 이름에게 인사를 건넵니다.
    
    Args:
        name: 인사할 대상의 이름
    """
    print(f"Hello, {name}! (안녕 {name}!)")
    return f"Hello, {name}! (안녕 {name}!)"

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "홍길동"
    hello(name)
