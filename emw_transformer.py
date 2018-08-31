#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author: Vadász Noémi
# created: 2018/02/28

import xml.etree.ElementTree as ElmTr
import sys


class Token:

    def __init__(self):
        self.Id = ''
        self.StartNode = ''
        self.EndNode = ''
        self.string = ''
        self.anas = ''
        self.lemma = ''
        self.pos = ''
        self.hfstana = ''
        self.feature = ''
        self.depTarget = ''
        self.depType = ''

    def print_ana(self, ofile):
        print(self.Id, self.StartNode, self.EndNode, self.string, self.anas, self.lemma, self.pos, self.hfstana, self.feature, self.depTarget, self.depType, sep='\t', end='\n', file=ofile)


def xml_parse(ifile):

    tsv_annot = []

    tree = ElmTr.parse(ifile)
    root = tree.getroot()

    for annots in root.findall('AnnotationSet'):

        for annot in annots.findall('Annotation'):
            typ = annot.get('Type')
            if typ == 'Token':

                token_ana = Token()
                token_ana.Id = annot.get('Id')
                token_ana.StartNode = annot.get('StartNode')
                token_ana.EndNode = annot.get('EndNode')
                for feature in annot:
                    if feature[0].text == 'string':
                        token_ana.string = feature[1].text
                    elif feature[0].text == 'anas':
                        token_ana.anas = feature[1].text
                    elif feature[0].text == 'lemma':
                        token_ana.lemma = feature[1].text
                    elif feature[0].text == 'pos':
                        token_ana.pos = feature[1].text
                    elif feature[0].text == 'feature':
                        token_ana.feature = feature[1].text
                    elif feature[0].text == 'hfstana':
                        token_ana.hfstana = feature[1].text
                    elif feature[0].text == 'depTarget':
                        token_ana.depTarget = feature[1].text
                    elif feature[0].text == 'depType':
                        token_ana.depType = feature[1].text
                tsv_annot.append(token_ana)

            # üres sor (7 üres mező tabbal)
            elif typ == 'Sentence':
                counter = 0
                space_ana = Token()
                tsv_annot.append(space_ana)

    return tsv_annot


def print_tsv(tsv_annot, ofile):

    with open(ofile, 'w') as of:
        for line in tsv_annot:
            line.print_ana(of)


def main():

    ifile = 'maistanultam_1_emw_emdep.xml'
    ofile = 'maistanultam_1_emw_emdep.tsv'
    tsv_annot = xml_parse(ifile)
    print_tsv(tsv_annot, ofile)


if __name__ == "__main__":
    main()
