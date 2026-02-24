# GitHub Classroom: IFC Building Code Compliance Assignment
## Complete Setup Summary

This assignment teaches students to parse IFC (Industry Foundation Classes) files and validate building designs against real building codes. Perfect for architecture/engineering students learning to code, or CS students learning domain applications.

---

## 📦 What's Included

### Student-Facing Files

1. **ifc-exercises.ipynb** (Main Notebook)
   - ✓ Introduction to IFC and resources
   - ✓ Setup and exploration guide
   - ✓ Working example: Extract all spaces
   - ✓ Exercise 1: Building code compliance checker
   - ✓ Exercise 2: Window compliance analysis
   - ✓ Bonus: Fire safety evacuation routes
   - ✓ Reference section with common IFC queries

2. **README.md** (Student Instructions)
   - Assignment overview and objectives
   - Getting started guide
   - Detailed description of each exercise
   - Hints for solving problems
   - Resources and references
   - Debugging tips

3. **IFC_QUICK_REFERENCE.md** (Cheat Sheet)
   - How to load IFC files
   - Common entity types and queries
   - Property and quantity access
   - Debugging patterns
   - Real-world code examples
   - Performance tips

4. **assets/duplex.ifc** (Sample Data)
   - Pre-loaded sample building model
   - Duplex apartment with spaces, windows, doors
   - Ready to analyze out of the box

---

## 🎯 Assignment Structure

### Exercise Progression

| # | Exercise | Focus | Skills | Est. Time |
|---|----------|-------|--------|-----------|
| Ex | Example | File I/O | Loading IFC, basic queries | 15 min |
| 1 | Building Code | Data Extraction | Classification, validation, reporting | 45 min |
| 2 | Windows | Spatial Analysis | Relationships, calculations, compliance | 60 min |
| Bonus | Fire Safety | Algorithms | Graphs, pathfinding, optimization | 90+ min |

### Learning Outcomes

Students will be able to:
- ✓ Understand IFC format and structure
- ✓ Parse IFC files programmatically with IfcOpenShell
- ✓ Extract and analyze spatial building data
- ✓ Apply real building code requirements in code
- ✓ Validate designs against standards
- ✓ Build spatial analysis algorithms
- ✓ Document code professionally

---

## 📋 Key Features

### Real-World Relevance
- Uses actual Catalan Building Code standards
- Teaches BIM (Building Information Modeling) concepts
- Applies to professional AEC workflows
- Links to industrial standards (BuildingSmart)

### Scaffolded Learning
- Starts simple (extract data)
- Progressively increases complexity
- Provides templates and hints
- Bonus offers challenge for advanced students

### Comprehensive Resources
- Multiple reference documents
- Code examples and patterns
- Debugging guides
- Links to official documentation

### Instructor Support
- Detailed grading rubrics
- Expected solution approaches
- Common mistake patterns
- Sample test cases
- Customization suggestions

---

## 🚀 Quick Start for Instructors

### 1. Import to GitHub Classroom
```bash
# Use this repository as template
# Students get individual forks
# They work in their private repos
```

### 2. Distribute to Students
- Point them to README.md for getting started
- Let them work through notebook at their own pace
- They implement functions in Exercise cells

### 3. Grade Using Rubric
- Check each exercise function for correctness
- Use SOLUTION_GUIDE.md for assessment criteria
- Assign partial credit for reasonable approaches
- Bonus is extra credit (10%)

### 4. Provide Feedback
- Comment on code quality and clarity
- Suggest better approaches if needed
- Highlight edge cases they missed
- Point to IFC_QUICK_REFERENCE.md for help

---

## 🔧 Technical Details

### Dependencies
- Python 3.8+
- Jupyter Notebook
- IfcOpenShell (auto-installed)
- Standard libraries (pathlib, collections, json)

### File Paths (Relative to Notebook)
```
assets/duplex.ifc      # Loaded as: Path("assets/duplex.ifc")
```

### Compatibility
- Linux ✓
- macOS ✓
- Windows ✓
- Cloud Jupyter ✓ (if file path adjusted)

---

## 📚 Learning Resources Included

### IFC Education
- **Knowledge Base**: https://notebooklm.google.com/notebook/0925c2a1-519b-40a8-aca4-1e832d219f3c
- **Official Standard**: https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
- **Python Library**: https://docs.ifcopenshell.org/ifcopenshell-python.html

### Building Codes
- **Catalan Code**: https://notebooklm.google.com/notebook/216b245f-0fc1-4063-bdfd-d23b41360b0e (used in exercises)

### Quick Reference
- Built-in cheat sheet in `IFC_QUICK_REFERENCE.md`
- Common patterns section in notebook
- Debugging tips throughout

---

## ✅ What's Ready to Use

### Immediate Usage
1. ✓ Notebook with full content and code templates
2. ✓ Sample IFC file (duplex apartment)
3. ✓ Student-friendly documentation
4. ✓ Instructor grading guides
5. ✓ Quick reference materials

### No Additional Setup Required
- ✓ All resources linked directly
- ✓ Dependencies auto-install
- ✓ File paths work out of the box
- ✓ Example code runs end-to-end

---

## 🎓 Integration Scenarios

### Computer Science Course
- Focus: Data parsing, APIs, validation logic
- Difficulty: Medium (good introduction to domain-specific programming)
- Prerequisites: Basic Python

### Architecture/Engineering Course
- Focus: BIM concepts, building codes, compliance
- Difficulty: Low-Medium (scaffolded learning)
- Prerequisites: None (engineering background helpful but not required)

### Data Science Course
- Focus: Spatial data analysis, graph algorithms (bonus)
- Difficulty: Medium-High
- Prerequisites: Python, basic graph theory

### AEC/BIM Professional Training
- Focus: Practical IFC workflows, automation
- Difficulty: Low (hands-on tool learning)
- Prerequisites: Building domain knowledge

---

## 📖 Document Guide

### For Students: Start Here →
1. **README.md** - Read assignment overview and instructions
2. **ifc-exercises.ipynb** - Complete notebook with content
3. **IFC_QUICK_REFERENCE.md** - Use while coding

### For Instructors: Grade Using →
1. **SOLUTION_GUIDE.md** - Assessment criteria and rubrics
2. **ASSIGNMENT_OVERVIEW.md** - Context and integration notes
3. **README.md** (student version) - Understand requirements

### For Customization →
- **ASSIGNMENT_OVERVIEW.md** - Section "Customization Guide"
- Adjust exercises in **ifc-exercises.ipynb**
- Modify rubrics in **SOLUTION_GUIDE.md**

---

## 🔍 Quality Checklist

- ✓ Notebook tested and structured properly
- ✓ Example code works without external setup
- ✓ Resources properly linked and accessible
- ✓ Exercises are achievable with hints
- ✓ Grading rubrics are clear and fair
- ✓ Documentation is concise (no buzzwords)
- ✓ Multiple difficulty levels provided
- ✓ Error handling suggestions included
- ✓ Professional yet approachable tone
- ✓ Real-world application demonstrated

---

## 💬 Teaching Notes

### Facilitating Learning
- Encourage students to explore entity attributes with `print(dir(entity))`
- Remind them that IFC is complex; partial solutions are valuable
- Point to SOLUTION_GUIDE.md for common mistakes they might encounter
- Emphasize that different approaches can work

### Common Student Questions
1. "How do I find what properties are available?"
   → See IFC_QUICK_REFERENCE.md - Debugging section

2. "Why can't I find windows in spaces?"
   → IFC relationships are complex. Use coordinate-based fallbacks.

3. "Is my solution acceptable even if not perfect?"
   → Yes! See SOLUTION_GUIDE.md - Partial credit opportunities

### Time Management
- Full assignment: ~3-4 hours
- Without bonus: ~2-2.5 hours
- Example + Exercise 1 only: ~1 hour (intro version)

---

## 🚀 Extending This Assignment

### Easier Version
- Remove Exercise 2 (Windows)
- Skip Bonus
- Provide helper functions
- Use pre-extracted data

### Harder Version
- Add visualization requirements
- Include multiple IFC files
- Require database storage
- Implement real optimization algorithms
- Different building codes

### Real-World Project
- Import actual project IFC
- Target actual building codes
- Generate formal compliance reports
- Add BIM visualization component

---

## 📞 Troubleshooting

### Notebook Won't Run
→ Check Python 3.8+, run first cell to install IfcOpenShell

### "File not found" Error
→ Ensure working directory is repository root, assets/duplex.ifc exists

### IfcOpenShell Installation Fails
→ Try: `pip install --upgrade pip` then retry
→ May need OS-specific dependencies

### IFC File Structure Confusing
→ Print attributes: `print([attr for attr in dir(entity) if not attr.startswith('_')])`

---

## 📝 Assignment Files Summary

```
📦 edu.ifc-parsing (Your Repository)
├── 📄 README.md                    # START HERE for students
├── 📄 ASSIGNMENT_OVERVIEW.md       # For instructors/context
├── 📄 SOLUTION_GUIDE.md            # For grading
├── 📄 IFC_QUICK_REFERENCE.md       # Cheat sheet for all
├── 📓 ifc-exercises.ipynb          # Main notebook
└── 📁 assets/
    └── duplex.ifc                  # Sample building model
```

---

## ✨ Best Practices

### For Students
1. Work through examples before exercises
2. Print entity attributes when stuck
3. Start with simple implementations
4. Test with small data first
5. Document your approach
6. Commit work regularly to git

### For Instructors
1. Run notebook yourself once before assigning
2. Clarify time expectations with students
3. Allow different valid approaches
4. Provide code review feedback
5. Adjust difficulty based on student background
6. Share solutions after grading deadline

---

## 📊 Success Metrics

A successful submission should:
- ✓ Load IFC file without errors
- ✓ Extract spaces correctly
- ✓ Implement meaningful compliance checking
- ✓ Handle edge cases gracefully
- ✓ Have clear, readable code
- ✓ Show learning progression
- ✓ Document assumptions

---

**Ready to assign!** Start by pointing students to [README.md](README.md).

Questions? Issues? Refer to:
- Student help: [IFC_QUICK_REFERENCE.md](IFC_QUICK_REFERENCE.md)
- Instructor help: [SOLUTION_GUIDE.md](SOLUTION_GUIDE.md)
- Context: [ASSIGNMENT_OVERVIEW.md](ASSIGNMENT_OVERVIEW.md)
