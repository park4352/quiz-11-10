import random

def generate_lotto_numbers():
    lotto_numbers = []

    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)

        # 중복된 숫자가 없을 때만 리스트에 추가
        if number not in lotto_numbers:
            lotto_numbers.append(number)

    lotto_numbers.sort()  # 숫자를 오름차순으로 정렬
    lotto_numbers_str = ', '.join(map(str, lotto_numbers))  # 숫자를 문자열로 변환하여 출력을 위해 준비

    return lotto_numbers, f"생성된 로또 번호는 {lotto_numbers_str} 입니다."

# 로또 번호 생성 및 출력
numbers, message = generate_lotto_numbers()
print(message)
