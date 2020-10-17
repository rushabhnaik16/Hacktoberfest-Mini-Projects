#! /bin/bash

<<comment
  Author: Vivek Alhat
  Script: Organize files w.r.t file types
  Version: 1.0
comment

declare -a fmt=("txt" "mp3" "mp4" "jpg" "png" "jpeg")

echo "> Enter Directory (e.g: Documents, Pictures etc.): "
read -r path

# fmt=jpg # Test 1

for file in $(ls $HOME/$path/)
do
  # printf "$file\n"
  if [[ "${file##*.}" == "${fmt[0]}" ]]; then
    printf "> Processing $file\n"
    if [[ -d $HOME/$path/TextFiles/ ]]; then
      mv $HOME/$path/$file $HOME/$path/TextFiles
      printf "> Moved $file to $HOME/$path/TextFiles\n"
    else
      printf "No directory found. Creating a new directory ..\n"
      mkdir -p $HOME/$path/TextFiles && mv $HOME/$path/$file $HOME/$path/TextFiles
      printf "> Moved $file to $HOME/$path/TextFiles\n"
    fi
  elif [[ "${file##*.}" == "${fmt[1]}" ]]; then
    printf "> Processing $file\n"
    mv $HOME/$path/$file $HOME/Music
    printf "> Moved $file to $HOME/Music\n"
  elif [[ "${file##*.}" == "${fmt[2]}" ]]; then
    printf "> Processing $file\n"
    mv $HOME/$path/$file $HOME/Videos
    printf "> Moved $file to $HOME/Videos\n"
  elif [[ "${file##*.}" == "${fmt[3]}" ]] || [[ "${file##*.}" == "${fmt[4]}" ]] || [[ "${file##*.}" == "${fmt[5]}" ]]; then
    printf "> Processing $file\n"
    mv $HOME/$path/$file $HOME/Pictures
    printf "> Moved $file to $HOME/Pictures\n"
  fi
done

echo "Finished!"
