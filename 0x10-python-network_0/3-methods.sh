#!/bin/bash
# Display de HTTP methods
curl -sI Allow "$1" | grep -i Allow | perl -lane 'print "@F[1..$#F]"'
