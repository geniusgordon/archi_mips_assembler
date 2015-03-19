import re
import sys
from instruction import *

class Assembler():
	def __init__(self):
		self.line = []
		self.ins = []
		self.sym = {}

	def read_file(self, file_name):
		with open(file_name, "r") as f:
			self.line = list(f)

	def output_file(self, file_name, addr):
		with open(file_name, "wb") as f:
			for i in range(4)[::-1]:
				f.write(chr((addr>>(i*8))&0xff))
			for i in range(4)[::-1]:
				f.write(chr((len(self.ins)>>(i*8))&0xff))
			for _ins in self.ins:
				for i in range(4)[::-1]:
					f.write(chr((_ins.to_binary()>>(i*8))&0xff))

	def parse_ins(self, line, addr):
		m = re.match("\s*(?P<op>[a-zA-Z]+)(?P<oprand>.*)", line)
		op = m.group("op").upper()
		oprand = m.group("oprand")
		for _type in ins_type:
			if op in _type:
				_m = _type["regex"].match(oprand)
				return Instruction(_type[op], addr, 
								_type["type"], _m.groupdict())

	def parse_symbol(self, addr):
		for l in self.line:
			m = re.match("\s*("+LABEL+"\s*:\s*)?(?P<ins>.*)", l)
			if m.group("label") is not None:
				self.sym[m.group("label")] = addr
			self.ins.append(self.parse_ins(m.group("ins"), addr))
			addr += 4
	
	def assign_addr(self):
		for _ins in self.ins:
			if not isinstance(_ins.label, int):
				_ins.label = self.sym[_ins.label] / 4

	def assemble(self, fin, fout, addr):
		self.read_file(fin)
		self.parse_symbol(addr)
		self.assign_addr()
		self.output_file(fout, addr)

if __name__ == '__main__':
	p = Assembler()
	p.assemble(sys.argv[1], "iimage.bin", int(sys.argv[2]))

