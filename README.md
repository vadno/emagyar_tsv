# emagyar_tsv

**emagyar_tsv** converts the XML output of [e-magyar](https://e-magyar.hu/en) Hungarian text processing toolchain with the xml.etree.ElementTree Python package. The script can be run by this command: python3 deptex.py arg1 arg2

## arg1: input

XML output of e-magyar.

## arg2: output

TSV file in which one line corresponds to one token and sentences are separated by an empty line. The file contains seven columns:
1. the identifier of the word within the sentence
1. wordform
1. lemma
1. part of speech
1. morphological features
1. the identifier of the parent node
1. the dependency label

## Dependencies

Python3
