Check if order bills can be splitted for Guido and Tim
------------------------------------------------------

다음은 요기요를 통해 주문한 주문 금액의 목록입니다.
이 주문들을 Guido와 Tim이 비용을 같은 금액으로 나누어 지불할 수 있는지 확인하세요.

NOTE: 입력의 숫자는 하나의 주문 당 가격이며,
하나의 주문은 한 사람이 비용을 지불합니다. (한 주문의 비용을 나누어 지불하는 것 불가.)

```
input type: list[int(order's payment)]
return type: bool


example.

[
    15000,
    20000,
    9000,
    4000,
]
=> True

[
    8000,
    12000,
    20000,
    16000,
    12000,
    8000,
    4000,
]
=> True


[
    23000,
    12000,
    13500,
]
=> False

```
