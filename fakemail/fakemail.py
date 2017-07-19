import random
import string
from nltk.corpus import words
from nltk.corpus import names
from nltk.corpus import brown

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

    def gen_word_list(self):
        brown_ids = brown.fileids()
        brown_selection = fileids=random.choice(brown_ids)
        self.word_list = brown.words(brown_selection)

    def gen_subject(self, minlen=3, maxlen=8):
        subject_len = random.randrange(minlen, maxlen)
        subject_start = random.randrange(0, len(self.word_list)-maxlen)
        subject = " ".join(self.word_list[subject_start:subject_start+subject_len])
        subject = subject.strip(string.punctuation+" ")
        subject = subject.capitalize()
        return(subject)


class EmailDate(object):
    def __init__(self):
        pass
        return
