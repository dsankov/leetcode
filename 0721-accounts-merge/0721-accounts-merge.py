NO_PARENT = -1

class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = defaultdict(lambda: NO_PARENT)

        def find(self, user_id):
            if self.parent[user_id] == user_id:
                return user_id

            if self.parent[user_id] == NO_PARENT:
                self.parent[user_id] = user_id
                return user_id

            root_id = self.find(self.parent[user_id])
            self.parent[user_id] = root_id
            return root_id

        def union(self, user_1, user_2):
            root_1 = self.find(user_1)
            root_2 = self.find(user_2)
            self.parent[root_2] = root_1

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = self.UnionFind()
        known_user_emails = {}
        for user_index, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in known_user_emails:
                    uf.union(known_user_emails[email], user_index)
                known_user_emails[email] = user_index
                
        emails_dict = defaultdict(list)
        for email, user in known_user_emails.items():
            emails_dict[uf.find(user)].append(email)

        result = []
        for user, emails in emails_dict.items():
            result.append([accounts[user][0]] + sorted(emails))
        return result


        
        