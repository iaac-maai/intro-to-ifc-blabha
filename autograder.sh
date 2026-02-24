#!/bin/bash
# GitHub Classroom autograder script
# Runs tests and generates feedback

echo "🏗️  IFC Assignment Autograder"
echo "=============================="
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -q ifcopenshell pytest pytest-json-report nbconvert 2>/dev/null

# Run tests
echo "🧪 Running tests..."
cd /autograder/source

# Run pytest with JSON output for grading feedback
python -m pytest tests/test_autograder.py -v --tb=short --json-report --json-report-file=/tmp/report.json

# Capture exit code
TEST_EXIT=$?

echo ""
echo "=============================="
if [ $TEST_EXIT -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "⚠️  Some tests failed. Review the output above."
fi

exit $TEST_EXIT
