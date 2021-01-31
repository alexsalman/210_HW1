#!/usr/bin/env bash

check() {
    run sh -c "echo '$1' | ./arith"
    echo "$1 = $2, your code outputs $output"
    [ "$output" = "$2" ]
}
