class Conversion:
    def convert_kgs(weight):
        final_weight = round((int(weight) * 0.454), 0)
        return final_weight
    
    def convert_inch(height):
        cm = int(height) * 2.54
        m = round(int(cm), 0) / 100
        m2 = (m * m)
        final_height = round(m2, 2)
        return final_height
    
    def convert_cm(height):
        m = round(int(height), 0) / 100
        m2 = (m * m)
        final_height = round(m2, 2)
        return final_height
    
    def convert_mtr(height):
        m2 = int(height) * int(height)
        final_height = round(m2, 2)
        return final_height