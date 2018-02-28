#!/usr/bin/env bash

for f in emagyar_out/*.xml
do
	python3 emw_transformer.py $f
done