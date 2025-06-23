class RepoAnalyzer:
    @staticmethod
    def analyze_repo(repo):
        lst = sorted(repo , key = lambda x: (x["stargazers_count"]), reverse=True)
        if len(lst) == 0:
            return None
        else:
            return lst[0]

repos = [
    {"name": "alpha",   "stargazers_count": 12},
    {"name": "bravo",   "stargazers_count": 45},
    {"name": "charlie", "stargazers_count": 45},  # tie with bravo
    {"name": "delta",   "stargazers_count": 7},
]
print(RepoAnalyzer.analyze_repo(repos))