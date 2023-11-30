#!/usr/bin/env bash
# This script sends a request to a URL and prints its size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
