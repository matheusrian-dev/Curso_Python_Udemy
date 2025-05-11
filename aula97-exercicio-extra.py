"""
Exercicio extra - Hacker Rank
- Find Runner-up
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given 'n' scores.
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers
each separated by a space.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


def find_runner_up(arr):
    # necessário converter map em list ou tuple para
    # iterar mais de uma vez.
    arr = list(arr)
    valor_max = max(arr)
    # float('-inf') para casos onde não há valor mínimo
    # definido.
    runner_up = float('-inf')
    for score in arr:
        if score < valor_max and score > runner_up:
            runner_up = score
    return runner_up


print(find_runner_up(arr))
