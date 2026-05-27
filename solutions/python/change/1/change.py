"""
Finds the fewest coins
"""
from typing import List

def find_fewest_coins(coins: List[int], target: int) -> List[int]:
    """
    Given available types of coins, return a list of coins that matches the target number

    :param list[int] coins: List of coin types
    :param int target: The target number
    :return list[int]: The list of coins that matches the number
    """
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    # min_coins_needed[i] = fewest coins required to make amount i
    min_coins_needed: List[float] = [float('inf')] * (target + 1)

    # last_coin_used[i] = last coin used to make amount i
    last_coin_used: List[int] = [-1] * (target + 1)

    min_coins_needed[0] = 0

    for current_total in range(1, target + 1):
        for coin_value in coins:
            if coin_value <= current_total:
                coins_if_using_this: float = min_coins_needed[current_total - coin_value] + 1

                if coins_if_using_this < min_coins_needed[current_total]:
                    min_coins_needed[current_total] = coins_if_using_this
                    last_coin_used[current_total] = coin_value

    if min_coins_needed[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    result: List[int] = []
    current: int = target

    while current > 0:
        coin: int = last_coin_used[current]
        result.append(coin)
        current -= coin

    return sorted(result)

    
    