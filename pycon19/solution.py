import itertools
from typing import Optional, Iterable, Generator, List


class Solution:
    size = 0

    def right_to_left(self, right: int, left: int) -> Generator[Iterable[int], None, None]:
        if right < 0:
            right += self.size

        for i in range(right, left - 1, -1):
            yield range(i, right + 1)

    def left_to_right(self, left: Optional[int], right: int) -> Generator[Iterable[Optional[int]], None, None]:
        if left is None:
            yield []
            left = 0

        if left < 0:
            left += self.size

        for i in range(left + 1, right + 1):
            yield range(left, i)

    def solve(self, orders: List[int]) -> bool:
        """Return True if orders can divided for 2 person with equal price"""
        self.size = len(orders)

        def sum_of_(index_iter):
            return sum((orders[i] for i in index_iter))

        orders.sort()
        all_indexes = frozenset(range(self.size))
        for right_range in self.right_to_left(-1, 1):
            right_list = list(right_range)
            for left_range in self.left_to_right(None, right_list[0] - 1):
                tim = frozenset(itertools.chain(right_list, left_range))
                guido = all_indexes - tim

                sum_of_tim, sum_of_guido = sum_of_(tim), sum_of_(guido)

                diff = sum_of_tim - sum_of_guido
                if diff == 0:
                    return True
                if 0 < diff:
                    break

        return False
