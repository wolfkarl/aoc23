from aocd import puzzle
import math

# lines = puzzle.examples[0].input_data
lines = puzzle.input_data

(rule_input, pages_input) = lines.split("\n\n")

class Rule:
    def __init__(self, rule_str) -> None:
        (self.before, self.after) = [int(s) for s in rule_str.split("|")]

    def __repr__(self) -> str:
        return f"{self.before}|{self.after}"

class RuleBook:
    def __init__(self, rules_str):
        self.rules = [Rule(s) for s in rules_str.split("\n")]

    def get_afters_for(self, before):
        return [r.after for r in self.rules if r.before == before]
    
    def get_befores_for(self, after):
        return [r.before for r in self.rules if r.after == after]
    
class Update:
    def __init__(self, update_str, rb: RuleBook) -> None:
        self.rb = rb
        self.pages = [int(s) for s  in update_str.split(",")]

    def middle_page(self):
        m =  math.ceil(len(self.pages)/2) -1
        return self.pages[m]
    
    def is_correct(self):

        for i in range(len(self.pages)):
            page = self.pages[i]
            
            afters = self.rb.get_afters_for(page)
            for after in afters:
                if after in self.pages[:i]:
                    return False
        
            befores = self.rb.get_befores_for(page)
            for before in befores:
                if before in self.pages[(i+1):]:
                    return False
                
        return True
    
    def make_correct(self):

        tries = 0
        MAX = 10_000

        while tries <= MAX:
            tries += 1
            corrected = False
            # print(self.pages)

            for i, page in enumerate(self.pages):

                
                afters = self.rb.get_afters_for(page)
                for after in afters:
                    if after in self.pages[:i]:
                        # print(after)
                        aix = self.pages.index(after)
                        (self.pages[i], self.pages[aix]) = (self.pages[aix], self.pages[i])
                        corrected = True
                        break
                
                if corrected:
                    break
            
                befores = rb.get_befores_for(page)
                for before in befores:
                    if before in self.pages[(i+1):]:
                        # print(before)
                        aix = self.pages.index(before)
                        (self.pages[i], self.pages[aix]) = (self.pages[aix], self.pages[i])
                        corrected = True
                        break

                if corrected:
                    break
        

            if corrected:
                continue
            else:
                break
                
        return tries < MAX

            
        
rb = RuleBook(rule_input)

updates = [Update(pi, rb) for pi in pages_input.split("\n")]
middle_pages = [update.middle_page() for update in updates if update.is_correct()]

print(sum(middle_pages))

incorrect = [update for update in updates if not update.is_correct()]
corrected = [update.make_correct() for update in incorrect]
corrected_middle = [update.middle_page() for update in incorrect]

print(sum(corrected_middle))



