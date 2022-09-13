class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        eighth_bit = 1 << 7
        seventh_bit = 1 << 6
        sixth_bit = 1 << 5
        fifth_bit = 1 << 4
        fourth_bit = 1 << 3
        
        trailing_byte_count = 0
        for byte in data:
            if trailing_byte_count > 0:
                if (byte & eighth_bit) and not (byte & seventh_bit):
                    trailing_byte_count -= 1
                    if trailing_byte_count < 0:
                        return False
                    continue
                else:
                    return False
            else:
                if not (byte & eighth_bit):
                    continue
                else: # 1xxx_xxxx
                    if not (byte & seventh_bit):
                        return False
                    # 11xx_xxxx
                    if not (byte & sixth_bit):
                        trailing_byte_count = 1
                        continue
                    # 111x_xxxx
                    if not (byte & fifth_bit):
                        trailing_byte_count = 2
                        continue
                    # 1111_xxxx
                    if not (byte & fourth_bit): 
                        trailing_byte_count = 3
                        continue
                    return False
        if trailing_byte_count != 0:
            return False
        return True