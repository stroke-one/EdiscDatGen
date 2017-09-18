
class DatWriter:
    def __init__(self, filepath):
        self.dat_delimiter = chr(20)
        self.dat_quotechar = chr(254)
        self.dat_newline   = chr(174)
        self.fp = open(filepath, "w", encoding='utf-8')
        

    def write_headers(self, headers=[]):
        headers = [self.dat_quotechar + h + self.dat_quotechar for h in headers]
        self.fp.write(self.dat_delimiter.join(headers))
        self.fp.write("\n")
        return
                      
        
    def write_entry(self, values=[]):
        values = [self.dat_quotechar + v + self.dat_quotechar for v in values]
        self.fp.write(self.dat_delimiter.join(values))
        self.fp.write("\n")
        return

    def close(self):
        self.fp.close()
        self.fp = None
        return

    

    


