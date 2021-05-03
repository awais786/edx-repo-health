import os

from repo_health.check_dependencies import get_dependencies


def get_repo_path(repo_name):
    tests_directory = os.path.dirname(__file__)
    return f"{tests_directory}/{repo_name}"


def test_python_js_repo_dependency_check():
    repo_path = get_repo_path('fake_repos/python_js_repo')
    dependencies = get_dependencies(repo_path)

    assert 'fs==2.0.18' in dependencies.get("pypi").get("list")
    assert "react-redux" in dependencies.get("js").get("list")
    assert dependencies.get("count") == 275
    assert dependencies.get("pypi").get("count") == 225
    assert dependencies.get("github").get("count") == 13
    assert dependencies.get("js").get("count") == 26


def test_js_repo_dependency_check():
    repo_path = get_repo_path('fake_repos/js_repo')
    dependencies = get_dependencies(repo_path)

    assert 'core-js' in dependencies.get("js").get("list")
    assert 'jest' in dependencies.get("js.dev").get("list")

    assert dependencies.get("count") == 37
    assert dependencies.get("js").get("count") == 26
    assert dependencies.get("js.dev").get("count") == 11
    assert dependencies.get("pypi").get("count") == 0


def test_python_repo_dependency_check():
    repo_path = get_repo_path('fake_repos/python_repo')
    dependencies = get_dependencies(repo_path)

    assert 'django==2.2.20' in dependencies.get("pypi").get("list")
    assert 'git+https://github.com/edx/credentials-themes.git@0.1.62#egg=edx_credentials_themes==0.1.62' \
           in dependencies.get("github").get("list")
    assert dependencies.get("pypi").get("count") == 8
    assert dependencies.get("github").get("count") == 1
    assert dependencies.get("js").get("count") == 0