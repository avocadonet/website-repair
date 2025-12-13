#!/bin/bash

echo "[STEP 1/2] Running Backend Setup (start_backend.sh)..."
bash start_backend.sh

echo "[STEP 2/2] Running Frontend Server in the background..."
bash start_frontend.sh
