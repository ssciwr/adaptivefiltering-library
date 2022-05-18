# Contribution guide

Thanks for considering to contribute to this project.
The guidelines provided here only apply to `afwizard-library` which contains the library of community-contributed filter pipelines for AFWizard.
If your contribution targets AFWizard itself, please open an issue [on the main repository]](https://github.com/ssciwr/afwizard).

## How to contribute a filter pipeline

We are assuming that you have used AFWizard and generated a JSON file that describes a filter pipeline configuration (e.g. by using `save_filter`). Having this file, the following steps will stage your pipeline for inclusion into the public library.
Some degree of familiarity with `git` and GitHub is useful in the process, you could e.g. follow [GitHubs introductory course](https://lab.github.com/).

* Fork the repository at https://github.com/ssciwr/afwizard-library
* Create a clone of your personal fork
* Copy the JSON file with your pipeline into the `afwizard_library` subdirectory of your clone.
* Add your name to the copyright file `COPYING.md`
* Create a commit and push it to your fork
* Open a Pull Request on GitHub
* Go through the checklist shown in the Pull Request description

Once your submission is ready, it will be merged into the library repository and be available for all users of AFWizard.

## Copyright + Licensing

As a contributor to this project, you do keep the copyright to your contributions.
By default, it is published under the permissive MIT license.
If this choice of license is holding you off from contributing, please considering opening an issue to discuss alternative licensing options.
