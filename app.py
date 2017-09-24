from fakemail.fakemail import EmailAddress
from fakemail.fakemail import EmailSubject
from fakemail.fakemail import UidGen
from fakemail.dat_tools import DatWriter
from random import sample, randint
import time

tm = time.time()

e = EmailAddress(15)
s = EmailSubject(100)

fields = ["FROM", "TO", "SUBJECT"]
d = DatWriter("test.DAT")
d.write_headers(fields)
field_bates = UidGen(prefix="BATES")

for entry in range(1000):

    field_from = e.sample_emails(1)[0]
    field_to   = ";".join(e.sample_emails(randint(1, 3)))
    field_subj = s.sample_subjects(1)[0]
    d.write_entry([next(field_bates), field_from, field_to, field_subj])



d.close()

print(time.time() - tm)
    
    
