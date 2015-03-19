import re
from register import *

OP = "\s*(?P<op>[a-zA-Z]+)\s*"
RD = "\s*\$(?P<rd>[0-9a-zA-Z]+)\s*"
RS = "\s*\$(?P<rs>[0-9a-zA-Z]+)\s*"
RT = "\s*\$(?P<rt>[0-9a-zA-Z]+)\s*"
IMM = "\s*(?P<imm>-?[0-9][x0-9a-fA-F]*)\s*"
LABEL = "\s*(?P<label>[a-zA-Z_][_0-9a-zA-Z]*)\s*"
COMMA = "\s*,\s*"

r_type_ins_1 = {
    "ADD": 0x20,
    "SUB": 0x22,
    "AND": 0x24,
    "OR": 0x25,
    "XOR": 0x26,
    "NOR": 0x27,
    "NADD": 0x28,
    "SLT": 0x2A,
    "type": "R",
    "regex": re.compile(RD + COMMA + RS + COMMA + RT)
}
r_type_ins_2 = {
    "SLL": 0x00,
    "SRL": 0x02,
    "SRA": 0x03,
    "type": "R",
    "regex": re.compile(RD + COMMA + RS + COMMA + IMM)
}
r_type_ins_3 = {
    "JR": 0x08,
    "type": "R",
    "regex": re.compile(RS)
}
i_type_ins_1 = {
    "ADDI": 0x08,
    "ANDI": 0x0c,
    "ORI": 0x0d,
    "NORI": 0x0e,
    "SLTI": 0x0a,
    "type": "I",
    "regex": re.compile(RT + COMMA + RS + COMMA + IMM)
}
i_type_ins_2 = {
    "LW": 0x23,
    "LH": 0x21,
    "LHU": 0x25,
    "LB": 0x20,
    "LBU": 0x24,
    "SW": 0x2b,
    "SH": 0x29,
    "SB": 0x28,
    "type": "I",
    "regex": re.compile(RT + COMMA + IMM + "\(" + RS + "\)")
}
i_type_ins_3 = {
    "BEQ": 0x04,
    "BNE": 0x05,
    "type": "I",
    "regex": re.compile(RS + COMMA + RT + COMMA + IMM)
}
i_type_ins_4 = {
    "LUI": 0x0f,
    "type": "I",
    "regex": re.compile(RT + COMMA + IMM)
}
j_type_ins = {
    "J": 0x02,
    "JAL": 0x03,
    "type": "J",
    "regex": re.compile(LABEL)
}
halt_ins = {
    "HALT": 0x3f,
    "type": "H",
    "regex": re.compile("\s*")
}
ins_type = [
    r_type_ins_1, r_type_ins_2, r_type_ins_3,
    i_type_ins_1, i_type_ins_2, i_type_ins_3, i_type_ins_4,
    j_type_ins, halt_ins,
]
ins_oprand = ["rd", "rs", "rt", "imm", "label"]

class Instruction():
    def __init__(self, op, addr, _type, d):
        self.op = op
        self._type = _type
        self.addr = addr
        self.rd = get_reg_num(d["rd"]) if "rd" in d else 0
        self.rs = get_reg_num(d["rs"]) if "rs" in d else 0
        self.rt = get_reg_num(d["rt"]) if "rt" in d else 0
        self.imm = int(d["imm"]) if "imm" in d else 0
        self.label = d["label"] if "label" in d else 0

    def to_binary(self):
        binary = 0
        if self._type == "R":
            binary |= (self.rs & 0x1f) << 21
            binary |= (self.rt & 0x1f) << 16
            binary |= (self.rd & 0x1f) << 11
            binary |= (self.imm & 0x1f) << 6
            binary |= self.op & 0x3f
        elif self._type == "I":
            binary |= (self.op & 0x3f) << 26
            binary |= (self.rs & 0x1f) << 21
            binary |= (self.rt & 0x1f) << 16
            binary |= self.imm & 0xffff
        elif self._type == "J":
            binary |= (self.op & 0x3f) << 26
            binary |= self.label & 0x3ffffff
        elif self._type == "H":
            binary = 0xffffffff
        return binary

    def __str__(self):
        return ' '.join([str(self.op), str(self.rd), str(self.rs), str(self.rd), str(self.imm), str(self.label)])
