# -*- coding:utf-8 -*-
import argparse

#命令行模块argparse
parser=argparse.ArgumentParser()
parser.add_argument("square",help="hello weiwei",type=int)
args=parser.parse_args()
print args.square**2