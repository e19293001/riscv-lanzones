ORI x3,x0,0x3                   ;x3 = 0x3
ORI x4,x0,0x4                   ;x4 = 0x4
SLT x5,x3,x4                    ;x5 = 1
ORI x3,x0,0x4                   ;x3 = 0x4
ORI x4,x0,0x3                   ;x4 = 0x3
SLT x5,x3,x4                    ;x5 = 0
ORI x2,x0,0x3
SLT x4,x3,x2
