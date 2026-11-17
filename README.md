# Lab 6 - Bowling Alley Coverage

This repository contains the Lab 6 code and coverage tests for the Bowling Alley assignment.

## Files

- `LAB6/bowling_alley.py` - application module under test
- `LAB6/CodeCoverageTest_bowling_alley.py` - tests for statement/code coverage
- `LAB6/BranchCoverageTest_bowling_alley.py` - tests for branch coverage
- `evidence/CodeCoverage_Report.txt` - saved code coverage run output
- `evidence/BranchCoverage_Report.txt` - saved branch coverage run output

## Run the checks

Install Python 3, pytest, and coverage, then run from the repository root:

```bash
python -m coverage run -m pytest LAB6/CodeCoverageTest_bowling_alley.py
python -m coverage report -m LAB6/bowling_alley.py

python -m coverage erase
python -m coverage run --branch -m pytest LAB6/BranchCoverageTest_bowling_alley.py
python -m coverage report -m LAB6/bowling_alley.py
```

## Results

Both suites pass 22 tests. The saved reports show 100% code coverage and 100% branch coverage (26 of 26 branches).

## Evidence note

The `.txt` files preserve the command output. The image output captures, if included, are formatted from saved logs and are not direct terminal screenshots. The handout specifically asks for terminal screenshots after each coverage target is met; capture those directly in a terminal before final submission.
