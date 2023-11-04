'''
    ChatRoom - develop by D1nn3rb0ne, is able to open a private server chat software
    Copyright (C) 2023  d1nn3rb0ne (D1nn3rb0ne)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.    
    The Auther's email: tomma_2022@outlook.com

'''

# use array library
# use Chinese (zh-cn)

import array
import math
import timeit
import sys

def allocate_memory(size_mb):
    # 计算需要填充的元素数量
    num_elements = size_mb * 1024 * 1024 // array.array('d').itemsize
    num_elements = math.floor(float(num_elements/1.1250000610351562))
    
    # 创建指定大小的数组
    memory_array = array.array('d', [0.0] * num_elements)

    return memory_array

size = float(input("请输入要提交的内存大小（单位：MB）: "))

# 开始计时
start_time = timeit.default_timer()

# 计算占用的内存大小并
memory_array = allocate_memory(size)

# 结束计时
end_time = timeit.default_timer()
run_time = end_time - start_time
run_time_sec = format(run_time, ".3f")
run_time_ms = format(run_time * 1000, ".3f")

# 输出
mem_size_bytes = sys.getsizeof(memory_array) + memory_array.buffer_info()[1]
mem_size_mb = float(mem_size_bytes / (1024 * 1024))


print(f"Successful! 成功提交了:\t{mem_size_mb:.3f} MB 的内存")
print(f"Runtime: 程序运行时间为： \t{run_time_sec} 秒(s)\t{run_time_ms} 毫秒(ms)")
input("Press any key to quit 按任意键退出...")
