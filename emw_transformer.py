#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: Vadász Noémi
# created: 2018/02/28

import xml.etree.ElementTree as ElmTr
import sys


class Token:

    def __init__(self):
        self.id = ''
        self.index = ''
        self.word = ''
        self.lemma = ''
        self.pos = ''
        self.morf = ''
        self.dep_id = ''
        self.dep_index = ''
        self.dep_type = ''

    def print_ana(self, ofile):
        print(self.index, self.word, self.lemma, self.pos, self.morf, self.dep_index, self.dep_type, sep='\t', file=ofile)


def xml_parse(ifile):

    tsv_annot = []

    tree = ElmTr.parse(ifile)
    root = tree.getroot()

    for annots in root.findall('AnnotationSet'):
        counter = 0
        for annot in annots.findall('Annotation'):
            typ = annot.get('Type')
            if typ == 'Token':
                counter += 1
                token_ana = Token()
                token_ana.id = annot.get('Id')
                token_ana.index = counter
                for feature in annot:
                    if feature[0].text == 'string':
                        token_ana.word = feature[1].text
                    elif feature[0].text == 'lemma':
                        token_ana.lemma = feature[1].text
                    elif feature[0].text == 'pos':
                        token_ana.pos = feature[1].text
                    elif feature[0].text == 'feature':
                        token_ana.morf = feature[1].text
                    elif feature[0].text == 'depTarget':
                        token_ana.dep_id = feature[1].text
                    elif feature[0].text == 'depType':
                        token_ana.dep_type = feature[1].text
                tsv_annot.append(token_ana)

            # üres sor (7 üres mező tabbal)
            elif typ == 'Sentence':
                counter = 0
                space_ana = Token()
                tsv_annot.append(space_ana)

    # az id-k helyett folytatólagos indexelést csinál (a deptex miatt kell!)
    for line in tsv_annot:
        for line2 in tsv_annot:
            if line.dep_id == line2.id:
                line.dep_index = line2.index

    return tsv_annot


def print_tsv(tsv_annot, ofile):

    with open(ofile, 'w') as of:
        for line in tsv_annot:
            line.print_ana(of)


def main():

    ifile = sys.argv[1]
    ofile = sys.argv[2]
    tsv_annot = xml_parse(ifile)
    print_tsv(tsv_annot, ofile)


if __name__ == "__main__":
    main()
