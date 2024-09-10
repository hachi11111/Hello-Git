#!/bin/bash

# 定义备份目录和文件名
BACKUP_DIR="/home/hongkai/.ssh/Hello-Git/backup"
LOG_FILE="log.log"
BACKUP_FILE="$BACKUP_DIR/log_$(date +%Y%m%d%H%M%S).log"

# 检查备份目录是否存在，如果不存在则创建
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p "$BACKUP_DIR"
fi

# 检查 log.log 文件是否存在，如果不存在则创建一个空的 log.log 文件
if [ ! -f "$LOG_FILE" ]; then
  touch "$LOG_FILE"
fi

# 获取当前文件的 MD5 值
CURRENT_MD5=$(md5sum "$LOG_FILE" | awk '{ print $1 }')

# 获取上次备份文件的 MD5 值
LAST_BACKUP_FILE=$(ls -t "$BACKUP_DIR"/log_*.log | head -n 1)
if [ -f "$LAST_BACKUP_FILE" ]; then
  LAST_MD5=$(md5sum "$LAST_BACKUP_FILE" | awk '{ print $1 }')
else
  LAST_MD5=""
fi

# 比较当前文件和上次备份文件的 MD5 值
if [ "$CURRENT_MD5" != "$LAST_MD5" ]; then
  # 如果 MD5 值不同，则进行备份
  cp "$LOG_FILE" "$BACKUP_FILE"
  echo "备份文件: $BACKUP_FILE"
else
  echo "文件内容未变化，不进行备份"
fi
