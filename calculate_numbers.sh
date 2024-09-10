#!/bin/bash
read -p "文件路径:" file_path
if [ ! -f "$file_path" ];then
	echo "文件不存在"
	exit 1
fi
sum=0
count=0
while read -r number ;do
	sum=$((sum + number))
	count=$((count + 1))
done < "$file_path"
if [ "$count" -eq 0 ]; then
  echo "文件中没有数字"
  exit 1
fi

average=$(echo "scale=2; $sum / $count" | bc)
echo "总和: $sum"
echo "平均值: $average"

json_file="output.json"
echo "{\"sum\": $sum, \"average\": $average}" > "$json_file"

echo "结果已保存到 $json_file"
