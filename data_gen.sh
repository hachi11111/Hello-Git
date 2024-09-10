#!/bin/bash

# 生成 name.txt 文件，包含 10000 个不重复的名字
for i in {1..10000}; do
  echo "Name$i" >> name.txt
done

# 从 name.txt 中随机选取 9990 个名字，生成 names_attend.txt 文件
shuf -n 9990 name.txt > names_attend.txt
