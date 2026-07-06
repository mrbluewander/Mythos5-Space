#!/bin/bash
# Mythos 5 Auto-Sync Script
git add .
git commit -m "Mythos 5 Auto-Sync: $1"
git push origin main
echo "[STATUS] Mythos 5 Core Physical Sync Completed."
