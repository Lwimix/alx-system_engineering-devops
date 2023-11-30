#!/usr/bin/env bash
# This script sends a GET request to a URL along with a header variable
curl "$1" -H "X-School-User-Id: 98"
