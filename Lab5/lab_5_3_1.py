import time
import concurrent.futures

N = 1000
arr_i = [i for i in range(1, N + 1)]
arr_j = [i for i in range(1, N + 1)]

matrix = []


def f(i, j: int) -> (int, int, float):
    return i, j, (abs(j - i)) ** 1 / 2


def case_1() -> float:
    start_time = time.time()
    for i in arr_i:
        line_res = []
        for j in arr_j:
            _, _, res = f(i, j)
            line_res.append(res)

        matrix.append(line_res)

    end_time = time.time()
    res_duration = end_time - start_time

    return res_duration


print(case_1())

squares = [[0 for _ in range(N)] for _ in range(N)]
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(5) as executor:
    res = [executor.submit(f, i, j) for i in range(N) for j in range(N)]
    for _, r in enumerate(concurrent.futures.as_completed(res)):
        i, j, val = r.result()
        squares[i][j] = val
end_time = time.time()

print(end_time-start_time)
