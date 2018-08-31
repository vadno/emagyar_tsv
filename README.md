# emagyar_tsv

**emagyar_tsv** converts the XML output of [e-magyar](https://e-magyar.hu/en) Hungarian text processing toolchain with the xml.etree.ElementTree Python package. The script can be run by this command: python3 deptex.py arg1 arg2

## arg1: input

XML output of e-magyar.

## arg2: output

TSV file in which one line corresponds to one token and sentences are separated by an empty line. The file contains seven columns:
1. ID
1. StartNode
1. EndNode
1. string
1. anas
1. lemma
1. pos
1. hfstana
1. feature
1. depTarget
1. depType

## Dependencies

Python3
