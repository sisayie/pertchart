'''
Tests to Run on TRAVIS CI
'''
import sys, os
from graphviz import Digraph, nohtml
import ast
import json

if __name__=="__main__":
	input_data = os.getcwd()
	for f in os.listdir(input_data):
		print(f)
