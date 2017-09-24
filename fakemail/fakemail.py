import random
import string
from nltk.corpus import words
from nltk.corpus import names
from nltk.corpus import brown
from nltk import pos_tag

class EmailAddress(object):
    word_list = words.words(fileids=['en'])
    name_list = names.words(fileids=['female.txt'])
    urls = []
    emails = []

    def __init__(self, address_count):
        for n in range((address_count//3)+1):
            self.urls.append(self.gen_url())
        for n in range(address_count):
            self.emails.append("@".join([self.gen_username(),
                                    random.choice(self.urls)]))
        return

    def __str__(self):
        all_emails = "\n".join(self.emails)
        return(all_emails)
    
    def __iter__(self):
        for email in self.emails:
            yield(email)

    def sample_emails(self, count):
        return(random.sample(self.emails, count))

    def weighted_choice(self, choices):
        """simple weighted selection from 'dict[k] = v' where v is int"""
        weight_total = sum(choices.values())
        rand_val = random.uniform(0, weight_total)

        test_val = 0
        for k in choices:
            if test_val + choices[k] >= rand_val:
                return(k)
            test_val += choices[k]

    def gen_url(self):
        """generates a single, random URL with dns.tld structure"""
        return(".".join([self.gen_dns(), self.gen_tld()]))


    def gen_dns(self):
        """generates a single, random word to create a fake dns entry"""
        dns = random.choice(self.word_list).lower()
        return(dns)

    def gen_tld(self):
        # original tlds = ['com', 'org', 'net', 'int', 'edu', 'gov', 'mil']
        tlds = {'com': 5, 'net': 2, 'org': 1}
        return(self.weighted_choice(tlds))

    def gen_username(self):
        return(random.choice(self.name_list).lower())


class EmailSubject(object):
    subjects = []

    def __init__(self, subject_count):
        self.gen_word_list()
        for n in range(subject_count):
            self.subjects.append(self.gen_subject())
        return

    def __str__(self):
        return("\n".join(self.subjects))

    def __iter__(self):
        for subject in self.subjects:
            yield(subject)

    def sample_subjects(self, count):
        return(random.sample(self.subjects, count))

    def gen_word_list(self):
        brown_ids = brown.fileids()
        brown_selection = fileids=random.choice(brown_ids)
        self.word_list = brown.words(brown_selection)

    def gen_subject(self, minlen=3, maxlen=8):
        #from the collection select a random sequence as a list
        subject_len = random.randrange(minlen, maxlen)
        subject_start = random.randrange(0, len(self.word_list)-maxlen)
        subject = self.word_list[subject_start:subject_start + subject_len]

        # test for preposition as the last word, it looks weird so remove it
        if pos_tag([subject[-1]])[-1][1] == "IN":
            print("subject {0}".format(subject))
            subject = subject[:-1]
            print("subject {0}".format(subject))
            print("******")

        #merge the words into a string, make pretty
        subject = " ".join(subject)
        subject = subject.strip(string.punctuation+" ")
        subject = subject.capitalize()

        return(subject)

class EmailDate(object):
    def __init__(self):
        pass
        return

    def gen_single_date(self, earliest, latest):
        pass
        return

class UidGen:
    def __init__(self, prefix="CTRL", pad=8, first=1):
        self.prefix = prefix
        self.pad = pad
        self.first = first

    def __iter__(self):
        while 1:
            yield(next(self))

    def __next__(self):
        uid = "{0}{1}".format(self.prefix, str(self.first).zfill(self.pad))
        self.first += 1
        return(uid)

    def __str__(self):
        uid = "{0}{1}".format(self.prefix, str(self.first).zfill(self.pad))
        # print(uid)
        return(uid)








































