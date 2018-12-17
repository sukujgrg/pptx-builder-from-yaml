# pptx-builder-from-yaml

> CLI to generate powerpoint slides from simple yaml file[s]

* Table of contents
  * [Dependencies to run the CLI](#dependencies-to-run-the-cli)
  * [How to install?](#how-to-install)
  * [How does a yaml file look like for generating pptx?](#how-does-a-yaml-file-look-like-for-generating-pptx)
  * [How to run the CLI?](#how-to-run-the-cli)
     * [How to validate a yaml and then generate the PPTX?](#how-to-validate-a-yaml-and-then-generate-the-pptx)
  * [FAQs](#faqs)
     * [How can I add same footer to all pptx[s] built using the CLI?](#how-can-i-add-same-footer-to-all-pptxs-built-using-the-cli)
     * [How to get different backgrounds for the generated pptx files using the CLI?](#how-to-get-different-backgrounds-for-the-generated-pptx-files-using-the-cli)
  * [How to setup development environment?](#how-to-setup-development-environment)
  * [How to run tests?](#how-to-run-tests)


## Dependencies to run the CLI
- `>= python3.4`
- python modules
  - `click==7.0.0`
  - [python-pptx==0.6.16](https://python-pptx.readthedocs.io/en/latest/)
  - `PyYAML==3.13`

## How to install?
> https://pypi.org/project/pptx-builder-from-yaml/
```bash
pip install pptx-builder-from-yaml
```

## How does a yaml file look like for generating pptx?

Here is a sample yaml file - [Dummy.yml](unit_tests/scripts/yamls/Dummy.yml)

## How to run the CLI?
```bash
$ pptx-builder --help
Usage: pptx-builder [OPTIONS] YAML_PATHS...

  A powerpoint builder

  https://github.com/sukujgrg/pptx-builder-from-yaml

Options:
  -pt, --pptx-template-path PATH  [required]
  -ms, --master-slide-idx INTEGER
                                  [default: 0]
  -sl, --slide-layout-idx INTEGER
                                  [default: 6]
  -fs, --font-size INTEGER        [default: 32]
  -fn, --font-name TEXT           [default: Calibri]
  -ns, --new-slide-path DIRECTORY
                                  [default: /var/folders/jw/vrnt6ysj2v7cm85hqy
                                  n_sk0h0000gq/T]
  --validate
  --help                          Show this message and exit.
```

```bash
pptx-builder slide_yamls/ -pt pptx-templates/default.pptx
```
**Notes:**
- `slide_yamls/` is the directory that holds `yaml` files for slides. The `yaml`[s] must
follow the schema defined in the code. [Here](unit_tests/scripts/yamls/Dummy.yml) is an
example `yaml` file. `slide_yamls` are positional arguments and can accept files and
directories. If a positional argument is a directory, it will try to build individual
`pptx` with each `yaml` files in the same directory.
- `--pptx-template-path | -pt` is expecting either a directory or a pptx file. If it is a 
directory, `pptx-builder` will chose one among all the pptx files found in the same directory.
The pptx template file should be without any change to master slide index or in slide
layout index. If there are any changes to master slide index or slide layout, you need to
pass corresponding `int` type to `-ms` and `-sl` options.
A sample pptx template file can seen here [pptx-templates](unit_tests/scripts/pptx-templates).
- The default `--new-slide-path` is `tmp` directory and hence it depends on the operating
system you run the `pptx-builder` on.


### How to validate a yaml and then generate the PPTX?
```bash
pptx-builder slide_yamls/dummy.yml -dm master_slides/default.pptx --validate
```

## FAQs
### How can I add same footer to all pptx[s] built using the CLI?

Add footer to pptx template file to pass with `--pptx-template-path` option

### How to get different backgrounds for the generated pptx files using the CLI?

Create different pptx template files with different backgrounds and pass it on to
`--pptx-template-path` option. See [this](https://youtu.be/AftDaPQwhPg) video on
creating pptx template file.

## How to setup development environment?

```bash
git clone https://github.com/sukujgrg/pptx-builder-from-yaml.git

cd pptx-builder-from-yaml

pipenv install --dev

pipenv shell

pipenv graph
```

## How to run tests?
```bash
cd pptx-builder-from-yaml/

pytest
```
or
```bash
$ tox .
py36 create: /Users/suku/GitHubPublic/pptx-builder-from-yaml/.tox/py36
py36 installdeps: ., pytest
py36 installed: atomicwrites==1.2.1,attrs==18.2.0,Click==7.0,jsonschema==2.6.0,lxml==4.2.5,more-itertools==4.3.0,Pillow==5.3.0,pluggy==0.8.0,pptx-builder-from-yaml==0.0.1,py==1.7.0,pytest==4.0.1,python-pptx==0.6.16,PyYAML==3.13,six==1.12.0,XlsxWriter==1.1.2
py36 runtests: PYTHONHASHSEED='69299544'
py36 runtests: commands[0] | pytest
===================================================== test session starts ======================================================
platform darwin -- Python 3.6.4, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
rootdir: /Users/suku/GitHubPublic/pptx-builder-from-yaml, inifile:
collected 2 items

unit_tests/scripts/test_gen.py ..                                                                                        [100%]

=================================================== 2 passed in 0.29 seconds ===================================================
___________________________________________________________ summary ____________________________________________________________
  py36: commands succeeded
  congratulations :)
```