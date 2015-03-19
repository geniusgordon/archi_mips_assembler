import re

OP = "(?P<op>[a-zA-Z]+)\s*"
RD = "\$(?P<rd>[0-9a-zA-Z]+)\s*"
RS = "\$(?P<rs>[0-9a-zA-Z]+)\s*"
RT = "\$(?P<rt>[0-9a-zA-Z]+)\s*"
IMM = "(?P<imm>-?[0-9][x0-9a-fA-F]*)\s*"
LABEL = "(?P<label>[a-zA-Z_][_0-9a-zA-Z]?)\s*"
COMMA = "\s*,\s*"

r_type_re_1 = re.compile(RD + COMMA + RS + COMMA + RT)
r_type_ins_1 = [
    ("ADD", 0x20),
    ("SUB", 0x22),
    ("AND", 0x24),
    ("OR", 0x25),
    ("XOR", 0x26),
    ("NOR", 0x27),
    ("NADD", 0x28),
    ("SLT", 0x2A),
]
r_type_re_2 = re.compile(RD + COMMA + RS + COMMA + IMM)
r_type_ins_2 = [
    ("SLL", 0x00),
    ("SRL", 0x02),
    ("SRA", 0x03),
]
r_type_re_3 = re.compile(RS)
r_type_ins_3 = [
    ("JR", 0x08),
]
i_type_re_1 = re.compile(RT + COMMA + RS + COMMA + IMM)
i_type_ins_1 = [
    ("ADDI", 0x08),
    ("ANDI", 0x0c),
    ("ORI", 0x0d),
    ("NORI", 0x0e),
    ("SLTI", 0x0a),
]
i_type_re_2 = re.compile(RT + COMMA + IMM + "\(" + RS + "\)")
i_type_ins_2 = [
    ("LW", 0x23),
    ("LH", 0x21),
    ("LHU", 0x25),
    ("LB", 0x20),
    ("LBU", 0x24),
    ("SW", 0x2b),
    ("SH", 0x29),
    ("SB", 0x28),
]
i_type_re_3 = re.compile(RS + COMMA + RT + COMMA + IMM)
i_type_ins_3 = [
    ("BEQ", 0x04),
    ("BNE", 0x05),
]
i_type_re_4 = re.compile(RT + COMMA + IMM)
i_type_ins_4 = [
    ("LUI", 0x0f),
]
j_type_ins = re.compile(IMM)
j_type_ins = [
    ("J", 0x02),
    ("JAL", 0x03),
]

