#!/usr/bin/env bash
# This script sends a POST request with an email and subject variable
curl -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
