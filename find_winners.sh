#!/bin/bash

# 创建 winners_pic 文件夹
mkdir -p winners_pic

# 读取 name.txt 文件，获取获奖选手的名字
winners=$(cat name.txt | shuf -n 1000)

# 遍历所有照片文件
for photo in *.jpg; do
  # 获取照片文件名（不包含扩展名）
  photo_name=$(basename "$photo" .jpg)

  # 检查照片文件名是否在获奖选手名单中
  if echo "$winners" | grep -q "$photo_name"; then
    # 如果存在，将照片复制到 winners_pic 文件夹中
    cp "$photo" winners_pic/
  fi
done
