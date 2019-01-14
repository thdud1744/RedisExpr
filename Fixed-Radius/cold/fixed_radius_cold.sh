declare -a results

for i in $(seq 1 100)
do
        echo 3 | sudo tee /proc/sys/vm/drop_caches
        foo=$(python fixed_radius_cold.py)
        results+=($foo)
        echo $i
done

echo ${results[@]}

echo ${#results[@]} #array length

echo "${results[@]/%/+}0" | bc # you should devide result by 100