import numpy as np

# ["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"]

d = np.arange()

d = array(["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"])

# 2차원 배열로 만들어줌

d = array([
    ["A", "A", "A", "A", "C", "X"],
    ["A", "A", "A", "A", "C", "X"],
    ["A", "A", "A", "A", "C", "X"],
    ["Z", "Z", "Z", "Z", "Z", "X"],
    ["A", "T", "T", "T", "T", "X"],
    ["X", "U", "U", "U", "U", "U"]
])

# cut_rows	cut_columns
# [1, 2, 4]	[2, 3]

print(d[0:1, 0:2])

# 각각으로 자른뒤에
# 총 12개의 배열
# 중복을 제거
# 전체중 len이 가장 높은 값을 result로 반환
