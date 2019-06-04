#!/bin/bash

set -euo pipefail

GIT_MAIL="paulfantom@gmail.com"
GIT_USER="paulfantom"

if [ -z "${GITHUB_TOKEN}" ]; then
    echo -e "\e[31mGitHub token (GITHUB_TOKEN) not set. Terminating.\e[0m"
    exit 128
fi

# Get new version
VERSION="$(curl --retry 5 --silent -u "${GIT_USER}:${GITHUB_TOKEN}" "https://api.github.com/repos/google/jsonnet/releases/latest" | jq '.tag_name' | tr -d '"v')"
echo -e "\e[32mLatest google/jsonnet version is: ${VERSION}\e[0m"

if grep "Version:  ${VERSION}" jsonnet.spec >/dev/null; then 
	echo -e "\e[33mLatest version is already packaged\e[0m"
	exit 0
fi

TODAY="$(date +"%a %b %d %Y")"
sed -i "s/Version:.*$/Version:  ${VERSION}/g" jsonnet.spec
sed -i "s/Release:.*$/Release:  1/g" jsonnet.spec
sed -i "s|^%changelog$|%changelog\n* ${TODAY} Pawel Krupa <pawel@krupa.net.pl> - ${VERSION}-1\n- Automated release of jsonnet version ${VERSION}\n|" jsonnet.spec

git config user.email "${GIT_MAIL}"
git config user.name "${GIT_USER}"
git checkout master
git add jsonnet.spec
git commit -m ":tada: automated upstream release update to version ${VERSION}"
git tag "v${VERSION}-1"
echo -e "\e[32mPushing to master branch\e[0m"
git push "https://${GITHUB_TOKEN}:@github.com/paulfantom/jsonnet-rpm" || exit 0
git push "https://${GITHUB_TOKEN}:@github.com/paulfantom/jsonnet-rpm" --tags || exit 0
