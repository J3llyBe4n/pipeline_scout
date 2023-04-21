## Pythonic하게 코드를 작성해보자잇 ##

---
Pythonic한 변수 명명법 by. 깡통좌
1. 변수 이름은 소문자로 작성하며, 단어와 단어 사이는 언더스코어로 구분합니다.
2. 변수 이름은 가능한 간결하고 명확하게 지어야 합니다. 변수가 어떤 값을 담고 있는지 쉽게 이해할 수 있어야 합니다.
3. 변수 이름은 예약어와 키워드(예: if, for, while 등)를 사용해서는 안 됩니다.
4. 클래스 이름과 함수 이름을 제외하고, 보통 변수 이름은 명사로 작성합니다.
5. 상수는 대문자로 작성하며, 단어와 단어 사이를 언더스코어로 구분합니다. 예를 들어 MAX_ITERATIONS와 같이 사용합니다.
6. 변수의 이름은 가능한 의미를 내포하도록 작성합니다. 변수의 용도나 목적이 드러나도록 하는 것이 좋습니다.

예시

    count = 0  
    total_sum = 0
    max_value = 100
    user_name = 'John Doe'
---
Pythonic한 함수 명명법 by.깡통좌
1. 함수 이름은 소문자로 작성하며, 단어와 단어 사이는 언더스코어로 구분합니다.
2. 함수 이름은 가능한 간결하고 명확하게 지어야 합니다. 함수가 어떤 작업을 수행하는지 쉽게 이해할 수 있어야 합니다.
3. 함수 이름은 동사로 시작하며, 함수가 수행하는 작업을 나타내도록 작성합니다.
4. 함수의 인자는 가능한 간결하고 명확하게 지어야 합니다. 인자의 역할이 명확하게 드러나도록 하는 것이 좋습니다.
5. 함수의 이름은 가능한 의미를 내포하도록 작성합니다. 함수의 용도나 목적이 드러나도록 하는 것이 좋습니다.
6. 함수의 이름에는 예약어나 키워드(예: if, for, while 등)를 사용해서는 안 됩니다.

예시

    def calculate_sum(numbers_list):
        total_sum = 0
        for num in numbers_list:
            total_sum += num
        return total_sum

    def get_user_info(user_id):
        # user_id를 기반으로 데이터베이스에서 유저 정보를 가져온다
---
Pythonic한 클래스 명명법 by.깡통좌
1. 클래스 이름은 대문자로 시작합니다.
2. 클래스 이름은 가능한 간결하고 명확하게 지어야 합니다. 클래스가 어떤 역할을 수행하는지 쉽게 이해할 수 있어야 합니다.
3. 클래스의 이름은 명사로 작성합니다.
4. 클래스 이름은 CamelCase를 사용해서 작성합니다. 단어와 단어 사이를 대문자로 구분합니다.
5. 클래스의 이름에는 예약어나 키워드(예: if, for, while 등)를 사용해서는 안 됩니다.
6. 클래스의 이름은 가능한 의미를 내포하도록 작성합니다. 클래스의 용도나 목적이 드러나도록 하는 것이 좋습니다.

예시

    class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    class User:
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
---