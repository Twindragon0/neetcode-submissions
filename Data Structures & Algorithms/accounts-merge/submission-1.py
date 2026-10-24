class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToCC = defaultdict(set)
        for account in accounts:
            name = account[0]
            currSet = set()
            for email in account[1:]:
                currSet.update(emailToCC[(name, email)])
                currSet.add(email)
            for email in account[1:]:
                emailToCC[(name, email)] = currSet
            for email in currSet:
                emailToCC[(name, email)] = currSet
        ansSet = set()
        for key, emails in emailToCC.items():
            ansSet.add((key[0], *emails))
        return list(ansSet)
        
            
