#!/bin/bash 
if [ 1 -ne 2 ]; 
then echo "hola tqm"
fi
variable=1
while [ $variable -lt 5 ] 
do
echo $variable 
variable=$(($variable+1)) 
done
var1='fuera'
var2='fuera'

funcion_ambito(){
var1='dentro'
local var2='dentro'
var3='dentro'
local var4='dentro'
echo $var1 $var2 $var3 $var4
}

echo $var1 $var2
funcion_ambito
echo $var1 $var2 $var3 $var4


