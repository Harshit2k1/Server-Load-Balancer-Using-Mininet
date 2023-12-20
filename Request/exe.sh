#!/bin/bash

# Generate a random number between 1 and 100



#for i in {1..2}; do
#    curl 10.0.0.2/smallfile -o smallfile.save 1>/dev/null
#    done


# Check conditions using if, elif, and else
for i in {1..150}; do
    random_number=$((RANDOM % 4))
    if [ "$random_number" -eq 0 ]; then
#        echo $random_number
        curl 10.0.0.254/bigfile -o bigfile.save 1>/dev/null
    elif [ "$random_number" -eq 1 ]; then
#        echo $random_number
        curl 10.0.0.254/medfile -o medfile.save 1>/dev/null
    elif [ "$random_number" -eq 2 ]; then
#        echo $random_number
        curl 10.0.0.254/smallfile -o smallfile.save 1>/dev/null
    else
#        echo $random_number
        curl 10.0.0.254/vsmfile -o vsmfile.save 1>/dev/null
    fi
    done
