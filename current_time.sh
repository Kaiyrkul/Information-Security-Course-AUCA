#!/bin/bash

curr=$(date +%H:%M)
end_hour=18
current_hour=$(date +%H)
current_min=$(date +%M)

diff_h=$((end_hour - current_hour - 1))
diff_m=$((60 - current_min))

echo "Current time: $curr. Work day ends after $diff_h hours and $diff_m minutes."
