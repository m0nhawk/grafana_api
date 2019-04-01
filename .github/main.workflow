workflow "Publish" {
  resolves = ["publish-to-conda"]
  on = "release"
}

action "publish-to-conda" {
  uses = "m0nhawk/conda-package-publish-action@master"
  secrets = ["ANACONDA_USER", "ANACONDA_PASSWORD"]
}

# Filter for master branch
