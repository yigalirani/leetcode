from collections import defaultdict

    
class Solution:
    def accountsMerge(self, accounts):
        email_to_users=defaultdict(set)
        visited_users=set()
        visited_email=set()
        marged=defaultdict(set)
        usernames={}
        def visit_email(email):
            if email in visited_email:
                return 
            visited_email.add(email)
            marged[current_user].add(email)
            for user in email_to_users[email]:
                visit_user(user)
            
        def visit_user(user):
            if user in visited_users:
                return
            visited_users.add(user)
            for email in accounts[user][1:]:
                visit_email(email)
            
            
        for user,account in enumerate(accounts):
            usernames[user]=account[0]
            for email in account[1:]:
                email_to_users[email].add(user)
        for user in range(len(accounts)):
            current_user=user
            visit_user(user)
        ans=[]
        for user,emails in marged.items():
            username=usernames[user]
            ans.append([username]+sorted(emails))
        return ans
def main():
    accounts=[["a","a1@mail.com"],["a","a1@mail.com","a2@mail.com"]]    
    ans=Solution().accountsMerge(accounts)
    print(ans)
main()