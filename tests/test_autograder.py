"""
Autograder tests for IFC Building Code Compliance Assignment

Tests check that student implementations meet baseline requirements.
This file runs on GitHub Classroom's autograding container.
"""

import pytest
import sys
from pathlib import Path

# Add the notebook directory to path for imports
REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT))

import ifcopenshell
from nbconvert import exporters
import json


class TestNotebookExecution:
    """Test that notebook runs without critical errors"""
    
    def test_notebook_exists(self):
        """Check that the notebook file exists"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        assert notebook_path.exists(), "ifc-exercises.ipynb not found"
    
    def test_ifc_file_exists(self):
        """Check that the sample IFC file exists"""
        ifc_path = REPO_ROOT / "assets" / "duplex.ifc"
        assert ifc_path.exists(), "assets/duplex.ifc not found"
    
    def test_ifc_file_loads(self):
        """Check that IFC file can be loaded"""
        ifc_path = REPO_ROOT / "assets" / "duplex.ifc"
        ifc = ifcopenshell.open(str(ifc_path))
        assert ifc is not None
        
        # Check basic structure
        assert len(list(ifc)) > 0, "IFC file is empty"
        
        # Check for spaces (should have at least one)
        spaces = ifc.by_type("IfcSpace")
        assert len(spaces) > 0, "No spaces found in model"


class TestExercise1:
    """Test Exercise 1: Building Code Compliance Checker"""
    
    def test_function_exists(self):
        """Test that check_space_compliance function is defined"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        # Find the cell with Exercise 1
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                cell_content = ''.join(cell['source'])
                if 'check_space_compliance' in cell_content:
                    code_text = cell_content
                    break
        
        assert 'def check_space_compliance' in code_text, \
            "Function check_space_compliance not defined"
    
    def test_function_returns_dict(self):
        """Test that function returns enriched data with analysis"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        # Extract and execute the function
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if 'def check_space_compliance' in source and 'TODO' not in source:
                    code_text = source
                    break
        
        if not code_text:
            pytest.skip("Student has not implemented check_space_compliance yet")
        
        # Execute function
        namespace = {}
        try:
            exec(code_text, namespace)
        except Exception as e:
            pytest.fail(f"Function definition has syntax error: {e}")
        
        # Load test data
        ifc_path = REPO_ROOT / "assets" / "duplex.ifc"
        ifc = ifcopenshell.open(str(ifc_path))
        spaces = ifc.by_type("IfcSpace")
        
        # Call the function with test data
        try:
            result = namespace['check_space_compliance'](spaces)
        except Exception as e:
            pytest.fail(f"Function crashed when called: {e}")
        
        # Verify it returns proper structure
        assert isinstance(result, dict), "Should return a dictionary"
        assert len(result) > 0, "Result should not be empty"
        assert any(k in result for k in ['passed', 'failed', 'compliance']), \
            "Should have compliance analysis in result"
    
    def test_function_checks_requirements(self):
        """Test that function validates actual requirements"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        # Extract the function
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if 'def check_space_compliance' in source and 'TODO' not in source:
                    code_text = source
                    break
        
        if not code_text:
            pytest.skip("Student has not implemented function yet")
        
        namespace = {}
        try:
            exec(code_text, namespace)
        except:
            pytest.skip("Function not ready for testing")
        
        ifc_path = REPO_ROOT / "assets" / "duplex.ifc"
        ifc = ifcopenshell.open(str(ifc_path))
        spaces = ifc.by_type("IfcSpace")
        
        # Call function and verify it actually analyzed something
        try:
            result = namespace['check_space_compliance'](spaces)
        except:
            pytest.fail("Function crashes when called with real data")
        
        # Check that something was analyzed
        total_analyzed = 0
        if isinstance(result, list):
            total_analyzed = len(result)
        elif isinstance(result, dict):
            for key in ['passed', 'failed']:
                if key in result:
                    if isinstance(result[key], (list, dict)):
                        total_analyzed += len(result[key])
        
        assert total_analyzed > 0, \
            "Function should analyze at least some spaces (got empty result)"


class TestExercise2:
    """Test Exercise 2: Window Compliance Analysis"""
    
    def test_function_exists(self):
        """Test that analyze_window_compliance function is defined"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                cell_content = ''.join(cell['source'])
                if 'def analyze_window_compliance' in cell_content:
                    code_text = cell_content
                    break
        
        assert 'def analyze_window_compliance' in code_text, \
            "Function analyze_window_compliance not defined"
    
    def test_function_returns_dict(self):
        """Test that function analyzes windows and returns valid data"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        # Extract function
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if 'def analyze_window_compliance' in source and 'TODO' not in source:
                    code_text = source
                    break
        
        if not code_text:
            pytest.skip("Student has not implemented analyze_window_compliance yet")
        
        # Try to execute
        namespace = {}
        try:
            exec(code_text, namespace)
        except Exception as e:
            pytest.fail(f"Function definition has error: {e}")
        
        # Load test data
        ifc_path = REPO_ROOT / "assets" / "duplex.ifc"
        ifc = ifcopenshell.open(str(ifc_path))
        spaces = ifc.by_type("IfcSpace")
        
        # Call with test data
        try:
            result = namespace['analyze_window_compliance'](ifc, spaces)
        except Exception as e:
            pytest.fail(f"Function crashed when called: {e}")
        
        # Verify output structure
        assert isinstance(result, dict), "Should return a dictionary"
        assert len(result) > 0, "Result should not be empty"
        
        # Should have window-related data
        has_window_data = any(k in result for k in [
            'total_windows', 'windows', 'window_count', 'compliance'
        ])
        assert has_window_data, \
            f"Result should contain window analysis. Got keys: {list(result.keys())}"


class TestBonus:
    """Test Bonus Exercise: Fire Safety Routes (optional)"""
    
    def test_bonus_function_exists(self):
        """Test that analyze_evacuation_routes function is defined"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        code_text = ""
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                cell_content = ''.join(cell['source'])
                if 'def analyze_evacuation_routes' in cell_content:
                    code_text = cell_content
                    break
        
        # Bonus is optional, so we only issue a warning if not found
        if 'def analyze_evacuation_routes' not in code_text:
            pytest.skip("Bonus exercise not attempted (this is optional)")


class TestCodeQuality:
    """Test code quality and documentation"""
    
    def test_functions_have_docstrings(self):
        """Check that main functions have docstrings"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            notebook_json = json.load(f)
        
        # Find docstrings in code cells
        docstring_count = 0
        for cell in notebook_json['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if '"""' in source or "'''" in source:
                    docstring_count += 1
        
        assert docstring_count > 0, \
            "At least one function should have a docstring"
    
    def test_notebook_is_valid_json(self):
        """Check that notebook is valid JSON"""
        notebook_path = REPO_ROOT / "ifc-exercises.ipynb"
        
        with open(notebook_path) as f:
            try:
                json.load(f)
            except json.JSONDecodeError:
                pytest.fail("Notebook is not valid JSON")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
