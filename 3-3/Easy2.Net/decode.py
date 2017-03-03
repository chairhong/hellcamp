# Easy2.net decode.py

month = 10
day = 26
hour = 23
minute = 44
year = 299

chick = "144 207 93 170 111 25 130 144 21 152 172 "
chick += "-3 113 164 -24 94 117 -25 173 106 77 169 "
chick += "119 15 135 127 9 111 123 -12 109 218 61 "
chick += "155 98 50 199 131 -2 168 205 75 169 164 "
chick += "24 139 116 95 127 113 71 102 141 -18 "
chick += "152 153 28 111 131 74 207 201 -21 174 "
chick += "155 74 138 164 -7 179 215 94 187 142 "
chick += "55 147 99 64 176 117 25 193 177 47 135 111 -5 108 137 -8 132 120"

egg = "210 209 22 126 188 29 212 101 24 125 145 -22 180 134 -30 162 107 18 "
egg += "142 210 8 185 95 -23 221 123 54 183 180 39 103 145 57 141 181 56 141 138 -25 124 133"

decode_key = "9pMaVs5DxiOPGe8JETXYmg3lbudro6Qk1WLKwyhfnS4Iv0ABtjUCc7RZz2NFHq"
decode_key += "KfeROdEILJs5W6D1m4XFtH7YbwgrUConPuqQBcSxT092zljv8yMAGhpZN3akVi"
decode_key += "8vxekVPpYlsXDAujWoJEingTGf3mCh59LROt6cdUNMb41zH7Kr0yS2BIFZqawQ"
decode_key += "Hv8VzYa5b1FMGNODW4kwX9L3hK6SqsTtyxoE0Z7fPJIgrCAQiljBuenRcp2dUm"
decode_key += "fgnCw4HPJRdXKIq31YNDZMS82OjA7eUxpozasVmykiQrTFLW6htGb9B0lEcvu5"
decode_key += "jxLaZdWYngAfKGNhzTcXQU7Jy9sFbp0eRI1ECrv23PSw846oH5MBVtlDiOqumk"
decode_key += "U0tnl9bVK4iB2LzZXy7PaCHcAI5pOsSfjgqkr1vuRTFEo8Dxmhw3QGdeJM6WYN"
decode_key += "gWYN9w4LuPjxJl1MhOkniQy8CBUXr6THaKDctEdb0Imp32VfFZGvAS5ezqsR7o"
decode_key += "wj3J9fL8QY2kArXKgOEzmSdqHpcMsn1ahGWxCe7yPIlTuDRb6F40oZtiUBvV5N"

def stage1(string, range):
	num = int(string)
	num2 = range % 3
	num3 = 2

	if num2 == 0:
		num -= (day*num3) + (minute*num3) - (hour*2)

	elif num2 == 1:
		num -= (month*3) + (minute*2) - (hour*num2)

	elif num2 == 2:
		num -= year - (month*(num2*5)) - (minute*num2) - (hour*(num3+4)) - (num2*num3)

	return num;

def stage2(string):
	num = month
	array = string.split(' ')
	result = ''
	count = 0

	for i in array:
		if i == "":
			break;
		array_num = int(i)
		result += chr(array_num ^ ord(decode_key[count+num]))
		count += 1

	return result

print "[*] chick key decode"
chick_array = chick.split(' ')
chick_len = len(chick_array)
chick_stg1 = ''

for i in range(0, chick_len-1):
	chick_stg1 += str(stage1(chick_array[i], i)) + ' '

print "stage 1 : " + chick_stg1

chick_stg2 = stage2(chick_stg1)
print "result : " + chick_stg2[::-1]

print "\n[*] egg key decode"
egg_array = egg.split(' ')
egg_len = len(egg_array)
egg_stg1 = ''

for i in range(0, egg_len-1):
	egg_stg1 += str(stage1(egg_array[i], i)) + ' '
print "stage 1 : " + egg_stg1

egg_stg2 = stage2(egg_stg1)
print "result : " + egg_stg2[::-1]