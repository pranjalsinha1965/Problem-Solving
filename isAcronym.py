"""
['as', 'soon', 'as', 'possible']

'asap'
'aspa'
'asapp'
"""
class Solutions:
    def isAcronym(self, words, acronym):
        if len(acronym) != len(words):
            return False
    
