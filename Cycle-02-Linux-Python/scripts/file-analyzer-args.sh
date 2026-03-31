#!/usr/bin/bash

if ! [ -d $1 ] || [ "$1" == "" ]
then 
    echo "Expected argument Directory path example : ../abc , ./bxd etc." 
    exit 1
fi

directory_location=$(echo $1)


cd $directory_location

echo "The files in the directory $directory_location are : " 
count=0
for i in *
do
    if [ -f $i ]
    then
        count=$((count+1))
        echo -e "$count \t $(du -b $i)"
    fi
    # echo -e "\n" 
 
done

echo -e "\nTotal number of files in the Directory $directory_location are : $count" 
echo -e "\nDirectory size (bytes) : $(du -b $directory_location)" 
largest_file = $(ls -S $directory_location | head -1)
echo -e "\nLargest file in the directory is : $largest_file \nSize (bytes) : $(du -b $largest_file)"


