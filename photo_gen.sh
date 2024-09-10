#!/bin/bash

# 生成 10000 个照片文件，命名格式为“编号+名字.jpg”
for i in {1..10000}; do
  touch "$i-Name$i.jpg"
done
