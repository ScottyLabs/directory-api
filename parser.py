import search
from bs4.element import Tag

result = search.basic("gael")

for idx, val in enumerate(result.contents):
    print(idx, " ", val)



class Parser :
    data : Tag
    single : bool
    results : list[dict] or dict

    def __init__(self, data : Tag):
        self.data = data
        self.single = 'class' not in data.attrs

    def parseSingle(self):
        if not self.single:
            raise TypeError("Cannot parse multiple results")
        self.results = {'listing': self.data.h1.text}
        for entry in self.data.find_all("b"):
            if entry.text == "Display Name:":
                self.results['name'] = entry.next_sibling[1:]
            if entry.text == "Email:":
                self.results['email'] = entry.next_sibling[1:]
            if entry.text == "Andrew UserID:":
                self.results['andrew_id'] = entry.next_sibling[1:]
            if entry.text == "Advisor:":
                self.results['advisor'] = entry.findNext().text
            if entry.text == "Phone:":
                self.results['phone'] = entry.next_sibling[1:]
            if entry.text == "Job Title According to HR:":
                self.results['job'] = entry.next_sibling.next_sibling.text
            if entry.text == "Student Class Level:":
                self.results['class_level'] = entry.next_sibling.next_sibling.text
            if entry.text == "Student Class Level:":
                self.results['class_level'] = entry.next_sibling.next_sibling.text
            if entry.text == "Department with which this person is affiliated:":
                dep = []
                for i in entry.nextSiblingGenerator():
                    if i.name != 'br' and i.name is not None:
                        break
                    elif i.name is None:
                        dep.append(i.text)
                self.results['department'] = dep


p = Parser(search.basic("gael"))
p.parseSingle()

print(p.results)
