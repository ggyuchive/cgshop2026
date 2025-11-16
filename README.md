# CG:SHOP SoCG Competition 2026
## Competition Info
- [Description](https://cgshop.ibr.cs.tu-bs.de/competition/cg-shop-2026/#problem-description)
- [CG-SHOP/pyutils26](https://github.com/CG-SHOP/pyutils26)

## Directory Structure

- `/solution`: My solution codes
- `/test` : Validate solution & score
- `/visualization`: For visualizing data
- `/input` : .zip Input data(instances) given by CG:SHOP
- `/output` : .zip Output data which has answer after running solution

## How to run (Mac)

1) Enable independent python environment
```shell
cd ~/cgshop2026
python3 -m venv cgshop-env
source cgshop-env/bin/activate
```

2) brew install prerequisite
```shell
brew update
brew install cmake boost llvm conan gmp mpfr
```

3) clone pyutils26
```shell
git clone https://github.com/CG-SHOP/pyutils26
```

4) Install in pip
```shell
cd pyutils26
pip install --upgrade pip setuptools wheel
pip install numpy matplotlib pydantic networkx pytest pybind11 scikit-build-core skbuild-conan
pip install --verbose -e .
```

5) Add `pyutils26/pytest.ini`
```
# pytest.ini
[pytest]
norecursedirs = _skbuild
```

6) Check test
```shell
pytest -q
```
