from practice_sets.repo_analyzer import RepoAnalyzer

def test_analyze_repo():
    rep1 = []
    rep2 = [
    {"name": "alpha",   "stargazers_count": 12},
    {"name": "bravo",   "stargazers_count": 45},
    {"name": "charlie", "stargazers_count": 45},  # tie with bravo
    {"name": "delta",   "stargazers_count": 7},]

    assert RepoAnalyzer.analyze_repo(rep1) is None
    assert RepoAnalyzer.analyze_repo(rep2) == {"name": "bravo", "stargazers_count": 45}