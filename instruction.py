import re

OP = "\s*(?P<op>[a-zA-Z]+)\s*"
RD = "\s*\$(?P<rd>[0-9a-zA-Z]+)\s*"
RS = "\s*\$(?P<rs>[0-9a-zA-Z]+)\s*"
RT = "\s*\$(?P<rt>[0-9a-zA-Z]+)\s*"
IMM = "\s*(?P<imm>-?[0-9][x0-9a-fA-F]*)\s*"
LABEL = "\s*(?P<label>[a-zA-Z_][_0-9a-zA-Z]?)\s*"
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
ins_type = [
    r_type_ins_1, r_type_ins_2, r_type_ins_3,
    i_type_ins_1, i_type_ins_2, i_type_ins_3, i_type_ins_4,
    j_type_ins,
]
ins_oprand = ["rd", "rs", "rt", "imm", "label"]

class Instruction():
    def __init__(self, op, d):
        self.op = op
        self.rd = d["rd"] if "rd" in d else None
        self.rs = d["rs"] if "rs" in d else None
        self.rt = d["rt"] if "rt" in d else None
        self.imm = d["imm"] if "imm" in d else None
        self.label = d["label"] if "label" in d else None

    def to_binary(self, _type):
        binary = 0
        if _type == "R":
            pass
        elif _type == "I":
            pass
        elif _type == "J":
            pass
        return binary

    def __str__(self):
        return ' '.join([str(self.op), str(self.rd), str(self.rs), str(self.rd), str(self.imm), str(self.label)])

def parse_ins(line):
    m = re.match("(?P<op>[a-zA-Z]+)(?P<oprand>.*)", line)
    op = m.group("op").upper()
    oprand = m.group("oprand")
    for _type in ins_type:
        if op in _type:
            print oprand
            _m = _type["regex"].match(oprand)
            print _m.groupdict()
            return Instruction(op, _m.groupdict())

