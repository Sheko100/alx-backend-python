#!/usr/bin/env python3
"""Module defines wait_n function
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random function n times"""
    wait_list: List[float] = []

    for i in range(n):
        wait = await wait_random(max_delay)
        wait_list.append(wait)

    wait_list = asc_sort(wait_list)

    return wait_list


def asc_sort(lst: List):
    """Sorts a list to be in ascending order"""
    srtd_lst: List = lst
    ri: int = 0
    le: int = 0
    lst_len: int = len(lst)

    while ri < lst_len - 1:
        if srtd_lst[ri] > srtd_lst[ri+1]:
            tmp = srtd_lst[ri]
            srtd_lst[ri] = srtd_lst[ri+1]
            srtd_lst[ri+1] = tmp

            le = ri
            while le > 0:
                if srtd_lst[le] < srtd_lst[le-1]:
                    tmp = srtd_lst[le]
                    srtd_lst[le] = srtd_lst[le-1]
                    srtd_lst[le-1] = tmp
                else:
                    break
                le -= 1
        ri += 1

    return srtd_lst
