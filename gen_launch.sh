#!/bin/bash
# 检查音频文件是否存在
audio_file="/home/hongkai/genshin_launch.mp4"
if [ ! -f "$audio_file" ]; then
  echo "音频文件不存在"
  exit 1
fi

# 使用 mpv 播放音频文件
mpv "$audio_file"

