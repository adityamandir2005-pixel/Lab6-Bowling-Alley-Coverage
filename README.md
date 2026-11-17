# Lab 6 - Bowling Alley Coverage

This repository contains the Lab 6 Bowling Alley application and its coverage tests.

## Files

- `bowling_alley.py` - application module under test
- `CodeCoverageTest_bowling_alley.py` - tests for code/statement coverage
- `BranchCoverageTest_bowling_alley.py` - tests for branch coverage
- `CodeCoverage_Report.txt` and `BranchCoverage_Report.txt` - saved run output
- `CodeCoverage_Output_Capture.png` and `BranchCoverage_Output_Capture.png` - formatted captures rendered from saved output

## Run the checks

Install Python 3, pytest, and coverage, then run from the repository root:

```bash
python -m coverage run -m pytest CodeCoverageTest_bowling_alley.py
python -m coverage report -m bowling_alley.py

python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_bowling_alley.py
python -m coverage report -m bowling_alley.py
```

## Results

Both suites pass 22 tests. The saved reports show 100% code coverage and 100% branch coverage (26 of 26 branches).

## Evidence note

The PNGs are formatted from saved logs, not direct desktop screenshots. The handout specifically asks for terminal screenshots after each coverage target is met; capture those directly in a terminal before final submission.
