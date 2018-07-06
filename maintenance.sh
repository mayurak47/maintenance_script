/Applications/Utilities/Geekbench\ 4.app/Contents/Resources/geekbench_x86_64 > abc.txt
i=0
for item in $(cat abc.txt | grep https://); do array[$i]=$item; i=$((i+1)); done
rm abc.txt
python3 maintenance.py ${array[1]}
