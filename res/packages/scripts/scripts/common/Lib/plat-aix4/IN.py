# 2017.08.29 21:58:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/plat-aix4/IN.py
LITTLE_ENDIAN = 1234
BIG_ENDIAN = 4321
PDP_ENDIAN = 3412
BYTE_ORDER = BIG_ENDIAN
DEFAULT_GPR = 3735928559L
MSR_EE = 32768
MSR_PR = 16384
MSR_FP = 8192
MSR_ME = 4096
MSR_FE = 2048
MSR_FE0 = 2048
MSR_SE = 1024
MSR_BE = 512
MSR_IE = 256
MSR_FE1 = 256
MSR_AL = 128
MSR_IP = 64
MSR_IR = 32
MSR_DR = 16
MSR_PM = 4
DEFAULT_MSR = MSR_EE | MSR_ME | MSR_AL | MSR_IR | MSR_DR
DEFAULT_USER_MSR = DEFAULT_MSR | MSR_PR
CR_LT = 2147483648L
CR_GT = 1073741824
CR_EQ = 536870912
CR_SO = 268435456
CR_FX = 134217728
CR_FEX = 67108864
CR_VX = 33554432
CR_OX = 16777216
XER_SO = 2147483648L
XER_OV = 1073741824
XER_CA = 536870912

def XER_COMP_BYTE(xer):
    return xer >> 8 & 255


def XER_LENGTH(xer):
    return xer & 127


DSISR_IO = 2147483648L
DSISR_PFT = 1073741824
DSISR_LOCK = 536870912
DSISR_FPIO = 268435456
DSISR_PROT = 134217728
DSISR_LOOP = 67108864
DSISR_DRST = 67108864
DSISR_ST = 33554432
DSISR_SEGB = 16777216
DSISR_DABR = 4194304
DSISR_EAR = 1048576
SRR_IS_PFT = 1073741824
SRR_IS_ISPEC = 536870912
SRR_IS_IIO = 268435456
SRR_IS_GUARD = 268435456
SRR_IS_PROT = 134217728
SRR_IS_LOOP = 67108864
SRR_PR_FPEN = 1048576
SRR_PR_INVAL = 524288
SRR_PR_PRIV = 262144
SRR_PR_TRAP = 131072
SRR_PR_IMPRE = 65536

def BUID_7F_SRVAL(raddr):
    return 2280652800L | uint(raddr) >> 28


BT_256M = 8188
BT_128M = 4092
BT_64M = 2044
BT_32M = 1020
BT_16M = 508
BT_8M = 252
BT_4M = 124
BT_2M = 60
BT_1M = 28
BT_512K = 12
BT_256K = 4
BT_128K = 0
BT_NOACCESS = 0
BT_RDONLY = 1
BT_WRITE = 2
BT_VS = 2
BT_VP = 1

def BAT_ESEG(dbatu):
    return uint(dbatu) >> 28


MIN_BAT_SIZE = 131072
MAX_BAT_SIZE = 268435456

def ntohl(x):
    return x


def ntohs(x):
    return x


def htonl(x):
    return x


def htons(x):
    return x


IPPROTO_IP = 0
IPPROTO_ICMP = 1
IPPROTO_IGMP = 2
IPPROTO_GGP = 3
IPPROTO_TCP = 6
IPPROTO_EGP = 8
IPPROTO_PUP = 12
IPPROTO_UDP = 17
IPPROTO_IDP = 22
IPPROTO_TP = 29
IPPROTO_LOCAL = 63
IPPROTO_EON = 80
IPPROTO_BIP = 83
IPPROTO_RAW = 255
IPPROTO_MAX = 256
IPPORT_RESERVED = 1024
IPPORT_USERRESERVED = 5000
IPPORT_TIMESERVER = 37

def IN_CLASSA(i):
    return long(i) & 2147483648L == 0


IN_CLASSA_NET = 4278190080L
IN_CLASSA_NSHIFT = 24
IN_CLASSA_HOST = 16777215
IN_CLASSA_MAX = 128

def IN_CLASSB(i):
    return long(i) & 3221225472L == 2147483648L


IN_CLASSB_NET = 4294901760L
IN_CLASSB_NSHIFT = 16
IN_CLASSB_HOST = 65535
IN_CLASSB_MAX = 65536

def IN_CLASSC(i):
    return long(i) & 3758096384L == 3221225472L


IN_CLASSC_NET = 4294967040L
IN_CLASSC_NSHIFT = 8
IN_CLASSC_HOST = 255

def IN_CLASSD(i):
    return long(i) & 4026531840L == 3758096384L


def IN_MULTICAST(i):
    return IN_CLASSD(i)


IN_CLASSD_NET = 4026531840L
IN_CLASSD_NSHIFT = 28
IN_CLASSD_HOST = 268435455
INADDR_UNSPEC_GROUP = 3758096384L
INADDR_ALLHOSTS_GROUP = 3758096385L
INADDR_MAX_LOCAL_GROUP = 3758096639L

def IN_EXPERIMENTAL(i):
    return long(i) & 3758096384L == 3758096384L


def IN_BADCLASS(i):
    return long(i) & 4026531840L == 4026531840L


INADDR_ANY = 0
INADDR_BROADCAST = 4294967295L
INADDR_LOOPBACK = 2130706433
INADDR_NONE = 4294967295L
IN_LOOPBACKNET = 127
IP_OPTIONS = 1
IP_HDRINCL = 2
IP_TOS = 3
IP_TTL = 4
IP_RECVOPTS = 5
IP_RECVRETOPTS = 6
IP_RECVDSTADDR = 7
IP_RETOPTS = 8
IP_MULTICAST_IF = 9
IP_MULTICAST_TTL = 10
IP_MULTICAST_LOOP = 11
IP_ADD_MEMBERSHIP = 12
IP_DROP_MEMBERSHIP = 13
IP_DEFAULT_MULTICAST_TTL = 1
IP_DEFAULT_MULTICAST_LOOP = 1
IP_MAX_MEMBERSHIPS = 20
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\plat-aix4\IN.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:58:13 St�edn� Evropa (letn� �as)
