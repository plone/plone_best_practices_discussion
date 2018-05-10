#!/usr/bin/env python

from github3 import repository
from pkg_resources import parse_version
from pkg_resources.extern.packaging.version import Version
from subprocess import check_output

# Read infos from pyenv
result = check_output(['pyenv', 'versions'])
pyenv_versions = {}
for line in result.splitlines():
    if line.startswith(b'* '):
        line = line[2:]
    if not line.startswith(b'system ('):
        version = parse_version(line.strip().decode('utf-8'))
        if isinstance(version, Version):
            master_version = '{major}.{minor}'.format(
                major=version._version.release[0],
                minor=version._version.release[1],
            )

            if master_version in pyenv_versions:
                if pyenv_versions[master_version] < version:
                    pyenv_versions[master_version] = version
            else:
                pyenv_versions[master_version] = version

print('PyENV Versions:')
for major, version in pyenv_versions.items():
    print(version.public)

# Check for Python Releases via github Tags
python = repository('python', 'cpython')
python_releases = [version for version in python.tags()]
releases = {}
for release in python_releases:
    version = parse_version(release.name)
    if isinstance(version, Version):
        master_version = '{major}.{minor}'.format(
            major=version._version.release[0],
            minor=version._version.release[1],
        )

        if master_version in releases:
            if releases[master_version] < version:
                releases[master_version] = version
        else:
            releases[master_version] = version

print('Current highest Python releases')
for major, version in releases.items():
    print(version.public)

print('Upgrade PyENV Versions:')
for version in pyenv_versions.keys():
    if pyenv_versions[version] < releases[version]:
        print('please update pyenv version to: {version}'.format(
            version=releases[version],
        ))
