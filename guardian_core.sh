#!/bin/bash
while true; do
  ./check_stability.sh
  if [ $(($(date +%s) % 3600)) -eq 0 ]; then
    ./clean_garbage.sh
  fi
  sleep 60
done
