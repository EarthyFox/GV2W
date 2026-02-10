#!/bin/bash
for file in *.DNG; do
    mv -- "$file" "${file%.DNG}.PNG"
done
