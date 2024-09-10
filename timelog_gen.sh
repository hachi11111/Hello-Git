#!/bin/bash

# 定义日志文件名
LOG_FILE="log.log"

# 获取当前日期和时间
CURRENT_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# 记录信息到日志文件
echo "当前时间为：[$CURRENT_TIME] " >> "$LOG_FILE"
