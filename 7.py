letters = ['73', '6d', '61', '72', '74', '20', '67', '75', '79', '2c', '20', '79', '6f', '75', '20', 
            '6d', '61', '64', '65', '20', '69', '74', '2e', '20', '74', '68', '65', '20', '6e', '65', '78', '74', '20', 
            '6c', '65', '76', '65', '6c', '20', '69', '73', '20', '5b', '31', '30', '35', '2c', '20', '31', '31', '30', 
            '2c', '20', '31', '31', '36', '2c', '20', '31', '30', '31', '2c', '20', '31', '30', '33', '2c', '20', '31',
            '31', '34', '2c', '20', '31', '30', '35', '2c', '20', '31', '31', '36', '2c', '20', '31', '32', '31', '5d',
            ]

message = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print(''.join(chr(int(x, 16)) for x in letters))
print(''.join(chr(x) for x in message))