#!/bin/bash

# First puzzle ----------

awk 'BEGIN {FS="-|,"} 
{ if ( ($3 >= $1 &&  $4 <= $2) || ($1 >= $3 && $2 <= $4)) res++ }
END { print res }' inputs/04.txt

# Second puzzle ----------

awk 'BEGIN {FS="-|,"} 
{ if ( ($1 <= $3 &&  $3 <= $2) || ($1 >= $3 && $1 <= $4)) res++ }
END { print res }' inputs/04.txt
