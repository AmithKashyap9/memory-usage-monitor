#!/bin/bash

DURATION=60 # Duration in seconds
INTERVAL=2 # Interval in seconds between probes
OUTPUT_FILE="memory_usage.log"

while getopts "d:i:o:" opt; do
  case ${opt} in
    d )
      DURATION=$OPTARG
      ;;
    i )
      INTERVAL=$OPTARG
      ;;
    o )
      OUTPUT_FILE=$OPTARG
      ;;
    \? )
      echo "Usage: $0 [-d duration_in_seconds] [-i interval_in_seconds] [-o output_file]"
      exit 1
      ;;
  esac
done

get_memory_usage() {
  local used_memory=$(vmstat -s | grep "used memory" | awk '{print $1}')
  echo "$used_memory"
}

echo "Starting memory usage monitoring..."
echo "Duration: $DURATION seconds"
echo "Interval: $INTERVAL seconds"
echo "Output file: $OUTPUT_FILE"
echo "Timestamp,Used Memory (KB)" > "$OUTPUT_FILE"

END_TIME=$((SECONDS + DURATION))

while [ $SECONDS -lt $END_TIME ]; do
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  MEMORY_USAGE=$(get_memory_usage)
  echo "$TIMESTAMP,$MEMORY_USAGE" >> "$OUTPUT_FILE"
  sleep $INTERVAL 
done

echo "Monitoring complete. Data written to $OUTPUT_FILE"