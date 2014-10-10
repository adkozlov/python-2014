s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def translate(c):
	oc = ord(c) - 97

	return chr(97 + (oc + 2) % 26 if oc in range(0, 26) else ord(c))

print(''.join([translate(c) for c in list("map")]))