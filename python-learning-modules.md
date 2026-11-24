# Portfolio Project Data — Python Learning Modules

- **Category:** `code-learning` (`Code Learning`)
- **Accent Color:** `orange`
- **Target Assets Folder:** `public/images/projects/python_learning_modules/`
- **Required Local Images:** `banner.webp` ONLY

## TypeScript Data (`ProjectCaseStudy`)

```typescript
{
  "id": "python-learning-modules",
  "code": "PRO-46 // CL-02",
  "title": "Python Learning Modules",
  "category": "code-learning",
  "categoryLabel": "Code Learning",
  "year": "2025",
  "status": "Completed",
  "accentColor": "orange",
  "repoUrl": "https://github.com/weztcy/Python-Learning-Modules",
  "license": "MIT License",
  "banner": "/images/projects/python_learning_modules/banner.webp",
  "summary": "Structured 18-module Python curriculum spanning 300 executable lessons, standard library mastery, algorithms, ecosystem tools, and 20 mini-projects.",
  "codeLearningDescription": "A progressive 18-module Python programming curriculum comprising 300 standalone executable scripts, 18 module study guides, and 300 verified execution logs. Learners advance from syntax fundamentals and OOP to algorithms, modern typing, ecosystem libraries, testing, and 20 practical projects.",
  "architectureSummary": "Progressive 18-module directory hierarchy pairing Indonesian module study guides with 300 standalone Python scripts and captured terminal execution logs.",
  "techStack": [
    "Python",
    "Python Standard Library",
    "NumPy",
    "pandas",
    "Matplotlib",
    "Requests",
    "BeautifulSoup",
    "OpenPyXL",
    "Flask",
    "FastAPI",
    "Pydantic",
    "SQLAlchemy",
    "pytest",
    "SQLite"
  ],
  "telemetryMatrix": {
    "projectType": "Modular Python Programming Curriculum",
    "targetPlatform": "Cross-Platform Python CLI & Ecosystem",
    "primaryDomain": "Software Engineering & CS Education",
    "architecturePipeline": "18 Modules -> 300 Scripts -> Log Captures",
    "testingAndAudit": "Verified",
    "projectStatus": "Completed",
    "projectYear": "2025"
  },
  "codeLearningProjectInfo": {
    "learningCategory": "Python Fundamentals, Algorithms & Ecosystem Curriculum",
    "difficultyLevel": "Beginner to Advanced",
    "programmingLanguages": "Python"
  },
  "codeLearningObjectives": [
    {
      "title": "Core Syntax & Control Flow Fluency",
      "description": "Write clean Python scripts using variables, built-in types, operators, conditional branching, structural pattern matching, and iterative loops.",
      "competencyCode": "COMP_01"
    },
    {
      "title": "Built-in Collections & Functional Abstractions",
      "description": "Manipulate lists, tuples, sets, dictionaries, and Unicode strings alongside comprehensions, iterators, generators, closures, and decorators.",
      "competencyCode": "COMP_02"
    },
    {
      "title": "Object-Oriented & Modular Architecture",
      "description": "Model reusable classes using encapsulation, inheritance, composition, dunder protocols, dataclasses, exceptions, file I/O, and custom packages.",
      "competencyCode": "COMP_03"
    },
    {
      "title": "Algorithmic Problem Solving & Complexity",
      "description": "Implement searching, sorting, stacks, queues, linked lists, trees, heaps, hash tables, graphs, backtracking, dynamic programming, and Big O analysis.",
      "competencyCode": "COMP_04"
    },
    {
      "title": "Modern Typing, Ecosystem Libraries & Testing",
      "description": "Apply type hints, context managers, NumPy, pandas, Matplotlib, FastAPI, SQLAlchemy, unittest, pytest, mocking, and profiling in local prototypes.",
      "competencyCode": "COMP_05"
    }
  ],
  "codeLearningPrerequisites": [
    {
      "category": "Prior Knowledge",
      "items": [
        "Basic familiarity with operating a command-line terminal and navigating directories",
        "No prior Python programming experience required for Module 01"
      ],
      "description": "The curriculum starts from introductory script execution and print output before scaling into computer science algorithms and ecosystem frameworks."
    },
    {
      "category": "Tooling Setup",
      "items": [
        "Python 3.10 or newer interpreter (required for match-case and modern typing syntax)",
        "Virtual environment with packages installed from requirements.txt for Modules 16–18"
      ],
      "description": "Modules 01 through 15 run exclusively on the Python Standard Library, while Modules 16 through 18 require third-party ecosystem packages."
    }
  ],
  "codeLearningCurriculumStructure": {
    "summary": "The curriculum progresses across four structured phases covering 18 modules and 300 executable Python scripts. Learners build foundational syntax and control flow first, advance through built-in collections, functional patterns, OOP, and algorithms, and finish with modern typing, data/API libraries, testing, and 20 practical capstone projects.",
    "totalEstimatedHours": "150 Hours",
    "phases": [
      {
        "phaseNumber": "01",
        "phaseTitle": "Python Foundations & Control Flow",
        "difficulty": "Beginner",
        "moduleRange": "Modules 01 - 05",
        "topics": [
          "Script Structure & CLI I/O",
          "Variables, Types & Mutability",
          "Operators & F-Strings",
          "Branching & Pattern Matching",
          "Loops & Iterative Patterns"
        ]
      },
      {
        "phaseNumber": "02",
        "phaseTitle": "Functions, Collections & Text Processing",
        "difficulty": "Beginner",
        "moduleRange": "Modules 06 - 08",
        "topics": [
          "Functions, Scope & Recursion",
          "Lists, Tuples, Sets & Dictionaries",
          "String Slicing, Methods & Unicode"
        ]
      },
      {
        "phaseNumber": "03",
        "phaseTitle": "Functional Python, OOP, Files & Standard Library",
        "difficulty": "Intermediate",
        "moduleRange": "Modules 09 - 13",
        "topics": [
          "Comprehensions, Iterators & Generators",
          "Lambdas, Closures & Decorators",
          "Classes, Inheritance, Dataclasses & Metaclasses",
          "Exceptions, JSON/CSV/Pickle & Packages",
          "Standard Library & SQLite"
        ]
      },
      {
        "phaseNumber": "04",
        "phaseTitle": "Algorithms, Modern Python, Ecosystem & Capstones",
        "difficulty": "Advanced",
        "moduleRange": "Modules 14 - 18",
        "topics": [
          "Search, Sort, Trees, Graphs & DP",
          "Typing, Context Managers & Memory",
          "NumPy, pandas, FastAPI & SQLAlchemy",
          "pytest, Mocking, Profiling & Packaging",
          "20 Practical Python Mini-Projects"
        ]
      }
    ]
  },
  "codeLearningModules": [
    {
      "id": "mod-01",
      "moduleNumber": "01",
      "title": "Introduction to Python & Program Structure",
      "description": "Covers script execution, docstrings, comments, print formatting, escape sequences, indentation rules, syntax error inspection, and interpreter discovery.",
      "submoduleCount": 10,
      "difficulty": "Beginner",
      "keyTopics": ["Hello World", "Program Structure", "print() Formatting", "Indentation", "Syntax Errors", "Interpreter Paths"],
      "sourceFilesCount": 10,
      "estimatedHours": "4 Hours"
    },
    {
      "id": "mod-02",
      "moduleNumber": "02",
      "title": "Variables & Data Types",
      "description": "Introduces variable binding, numeric primitives, strings, booleans, None, type inspection, implicit/explicit conversion, constants, and mutability.",
      "submoduleCount": 14,
      "difficulty": "Beginner",
      "keyTopics": ["int, float & complex", "str & bool", "NoneType", "Type Casting", "Multiple Assignment", "Mutable vs Immutable"],
      "sourceFilesCount": 14,
      "estimatedHours": "5 Hours"
    },
    {
      "id": "mod-03",
      "moduleNumber": "03",
      "title": "Input, Output & Operators",
      "description": "Teaches terminal input parsing and validation alongside arithmetic, assignment, comparison, logical, identity, membership, bitwise operators, and f-strings.",
      "submoduleCount": 14,
      "difficulty": "Beginner",
      "keyTopics": ["input() & Validation", "Arithmetic & Bitwise", "Logical & Identity", "Operator Precedence", "F-Strings", "Number Formatting"],
      "sourceFilesCount": 14,
      "estimatedHours": "6 Hours"
    },
    {
      "id": "mod-04",
      "moduleNumber": "04",
      "title": "Branching & Decision Making",
      "description": "Explores conditional control flow via if, if-else, elif, nested conditions, compound logic, ternary expressions, match-case, and applied rule checks.",
      "submoduleCount": 10,
      "difficulty": "Beginner",
      "keyTopics": ["if / elif / else", "Nested Conditions", "Ternary Expressions", "match-case", "Grade & Leap Year Logic"],
      "sourceFilesCount": 10,
      "estimatedHours": "5 Hours"
    },
    {
      "id": "mod-05",
      "moduleNumber": "05",
      "title": "Loops & Iteration Control",
      "description": "Covers for and while loops, range sequences, nested iteration, break/continue/else clauses, accumulators, pattern generation, and prime checks.",
      "submoduleCount": 15,
      "difficulty": "Beginner",
      "keyTopics": ["for & while Loops", "range()", "Nested Loops", "break & continue", "Loop else", "Star & Number Patterns"],
      "sourceFilesCount": 15,
      "estimatedHours": "7 Hours"
    },
    {
      "id": "mod-06",
      "moduleNumber": "06",
      "title": "Functions & Scope",
      "description": "Introduces reusable function definitions, parameter passing, return values, default/keyword/*args/**kwargs arguments, LEGB scope, recursion, and docstrings.",
      "submoduleCount": 15,
      "difficulty": "Beginner",
      "keyTopics": ["Parameters & Return", "*args & **kwargs", "global & nonlocal", "Recursion", "Docstrings", "Function Type Hints"],
      "sourceFilesCount": 15,
      "estimatedHours": "7 Hours"
    },
    {
      "id": "mod-07",
      "moduleNumber": "07",
      "title": "Built-in Data Structures",
      "description": "Compares lists, tuples, sets, and dictionaries across indexing, slicing, sorting, set algebra, nesting, shallow copying, and collection conversion.",
      "submoduleCount": 20,
      "difficulty": "Beginner",
      "keyTopics": ["Lists & Slicing", "Tuples & Unpacking", "Sets & Set Operations", "Dictionaries", "Nested Collections", "Collection Conversion"],
      "sourceFilesCount": 20,
      "estimatedHours": "9 Hours"
    },
    {
      "id": "mod-08",
      "moduleNumber": "08",
      "title": "String Manipulation",
      "description": "Covers immutable character indexing, slicing, built-in string methods, searching, replacing, splitting/joining, validation, text cleaning, and Unicode.",
      "submoduleCount": 14,
      "difficulty": "Beginner",
      "keyTopics": ["Indexing & Slicing", "String Methods", "split() & join()", "Validation & Cleaning", "Unicode Strings", "Palindrome Checks"],
      "sourceFilesCount": 14,
      "estimatedHours": "6 Hours"
    },
    {
      "id": "mod-09",
      "moduleNumber": "09",
      "title": "Comprehensions, Iterators & Generators",
      "description": "Explains concise collection building and lazy evaluation using list/dict/set comprehensions, iter()/next(), custom iterators, yield, and generator pipelines.",
      "submoduleCount": 16,
      "difficulty": "Intermediate",
      "keyTopics": ["List/Dict/Set Comprehensions", "Generator Expressions", "Iterator Protocol", "yield & yield from", "Lazy Evaluation", "enumerate & zip"],
      "sourceFilesCount": 16,
      "estimatedHours": "8 Hours"
    },
    {
      "id": "mod-10",
      "moduleNumber": "10",
      "title": "Advanced Functions",
      "description": "Treats functions as first-class objects through lambdas, map/filter/reduce, custom sorting keys, closures, parameterized decorators, partial, and callables.",
      "submoduleCount": 15,
      "difficulty": "Intermediate",
      "keyTopics": ["Lambda Expressions", "Higher-Order Functions", "map / filter / reduce", "Closures", "Decorators", "Partial & Callables"],
      "sourceFilesCount": 15,
      "estimatedHours": "8 Hours"
    },
    {
      "id": "mod-11",
      "moduleNumber": "11",
      "title": "Object-Oriented Programming",
      "description": "Deep-dives into classes, instance/class/static methods, encapsulation, properties, inheritance, composition, dunder protocols, dataclasses, slots, descriptors, and metaclasses.",
      "submoduleCount": 24,
      "difficulty": "Intermediate",
      "keyTopics": ["Classes & Properties", "Inheritance & MRO", "Polymorphism & ABCs", "Dunder Methods", "Dataclasses & Enums", "Descriptors & Metaclasses"],
      "sourceFilesCount": 24,
      "estimatedHours": "12 Hours"
    },
    {
      "id": "mod-12",
      "moduleNumber": "12",
      "title": "Exceptions, File Handling & Modules",
      "description": "Covers structured exception handling, custom exceptions, context managers, pathlib, text/JSON/CSV/Pickle file I/O, custom modules, packages, and relative imports.",
      "submoduleCount": 20,
      "difficulty": "Intermediate",
      "keyTopics": ["try / except / finally", "Custom Exceptions", "pathlib & File I/O", "JSON, CSV & Pickle", "Modules & Packages", "Main Guard"],
      "sourceFilesCount": 21,
      "estimatedHours": "10 Hours"
    },
    {
      "id": "mod-13",
      "moduleNumber": "13",
      "title": "Python Standard Library",
      "description": "Demonstrates built-in modules for math, statistics, CSPRNG secrets, datetime, OS/sys, collections, itertools, functools, regex, logging, argparse, subprocess, hashlib, and sqlite3.",
      "submoduleCount": 20,
      "difficulty": "Intermediate",
      "keyTopics": ["math & secrets", "datetime & logging", "collections & itertools", "Regular Expressions", "argparse & subprocess", "hashlib & sqlite3"],
      "sourceFilesCount": 20,
      "estimatedHours": "10 Hours"
    },
    {
      "id": "mod-14",
      "moduleNumber": "14",
      "title": "Algorithms & Data Structures",
      "description": "Implements search and sorting algorithms, stacks, queues, linked lists, binary trees, BSTs, heaps, hash tables, BFS/DFS graph traversal, backtracking, DP, greedy, and Big O.",
      "submoduleCount": 23,
      "difficulty": "Advanced",
      "keyTopics": ["Binary Search & Sorting", "Stacks, Queues & Linked Lists", "Trees, Heaps & Hash Tables", "Graph BFS & DFS", "Backtracking & DP", "Big O Analysis"],
      "sourceFilesCount": 23,
      "estimatedHours": "14 Hours"
    },
    {
      "id": "mod-15",
      "moduleNumber": "15",
      "title": "Modern Python & Advanced Features",
      "description": "Explores static typing (Union, Generic, Protocol, cast), structural pattern matching, custom context managers, weakref, GC, memory profiling, walrus operator, and lru_cache.",
      "submoduleCount": 17,
      "difficulty": "Advanced",
      "keyTopics": ["Generics & Protocols", "Pattern Matching", "contextlib & weakref", "Memory Profiling", "Walrus & Unpacking", "lru_cache & Introspection"],
      "sourceFilesCount": 17,
      "estimatedHours": "9 Hours"
    },
    {
      "id": "mod-16",
      "moduleNumber": "16",
      "title": "Data, APIs, Automation & Ecosystem",
      "description": "Introduces NumPy arrays, pandas DataFrames, Matplotlib plots, HTTP requests, BeautifulSoup scraping, OpenPyXL Excel automation, Flask, FastAPI, SQLAlchemy, and Pydantic.",
      "submoduleCount": 17,
      "difficulty": "Advanced",
      "keyTopics": ["NumPy & pandas", "Matplotlib Plots", "Requests & BeautifulSoup", "OpenPyXL Automation", "Flask & FastAPI", "SQLAlchemy & Validation"],
      "sourceFilesCount": 17,
      "estimatedHours": "10 Hours"
    },
    {
      "id": "mod-17",
      "moduleNumber": "17",
      "title": "Testing, Debugging & Project Management",
      "description": "Covers debugging logs, assertions, unittest, pytest, mocking, edge cases, cProfile, virtualenvs, pip, packaging, AST linting, formatting, static type inspection, and env vars.",
      "submoduleCount": 16,
      "difficulty": "Advanced",
      "keyTopics": ["unittest & pytest", "Mocking & Edge Cases", "cProfile Profiling", "venv & Packaging", "AST Linting", "Static Type Inspection"],
      "sourceFilesCount": 16,
      "estimatedHours": "8 Hours"
    },
    {
      "id": "mod-18",
      "moduleNumber": "18",
      "title": "Practical Python Projects",
      "description": "Consolidates core language mechanics, SQLite, file organization, CSV/Excel reporting, mocked HTTP clients, scraping, FastAPI endpoints, and pandas/Matplotlib summaries across 20 projects.",
      "submoduleCount": 20,
      "difficulty": "Advanced",
      "keyTopics": ["CLI & Business Logic", "In-Memory SQLite", "CSV & Excel Reporting", "Mocked API & Scraping", "FastAPI REST Endpoints", "Data Dashboard Prototype"],
      "sourceFilesCount": 20,
      "estimatedHours": "12 Hours"
    }
  ],
  "codeLearningPracticalProjects": [
    {
      "title": "In-Memory REST API Service (298_rest_api_project.py)",
      "description": "Builds a task creation and retrieval REST API using FastAPI and Pydantic schemas, verified locally via FastAPI TestClient with HTTP 404 error handling.",
      "highlights": [
        "Defines typed Pydantic request/response models for task resources",
        "Exercises POST and GET endpoints end-to-end without external server deployment"
      ],
      "coreScope": "FastAPI routing, schema validation, and automated TestClient verification",
      "trackTag": "Web API Prototype",
      "tier": "Advanced",
      "difficulty": "Advanced",
      "estimatedTime": "1.5 Hours",
      "architecturalConstraints": [
        "In-memory state storage only with deterministic HTTP 404 handling for missing IDs",
        "Offline execution via TestClient without binding external network ports"
      ]
    },
    {
      "title": "Data Analysis & Visualization Prototype (299_data_dashboard_project.py)",
      "description": "Aggregates categorical metrics using pandas groupby and renders an in-memory bar chart via Matplotlib without requiring browser hosting.",
      "highlights": [
        "Computes deterministic category totals using pandas DataFrame grouping",
        "Renders chart output headlessly in memory using Matplotlib"
      ],
      "coreScope": "DataFrame aggregation and programmatic visualization pipeline",
      "trackTag": "Data Analytics Prototype",
      "tier": "Advanced",
      "difficulty": "Advanced",
      "estimatedTime": "1.5 Hours",
      "architecturalConstraints": [
        "Headless in-memory chart rendering without GUI window dependencies",
        "Self-contained sample dataset for reproducible CLI execution"
      ]
    },
    {
      "title": "Excel Automated Reporting Tool (295_excel_report_project.py)",
      "description": "Generates structured .xlsx student grade workbooks inside temporary directories using OpenPyXL, writing tabular rows alongside dynamic AVERAGE spreadsheet formulas.",
      "highlights": [
        "Automates workbook creation and cell formatting with OpenPyXL",
        "Embeds Excel AVERAGE formulas and verifies saved workbook structure"
      ],
      "coreScope": "Programmatic spreadsheet authoring and formula generation",
      "trackTag": "Office Automation",
      "tier": "Intermediate",
      "difficulty": "Intermediate",
      "estimatedTime": "1 Hour",
      "architecturalConstraints": [
        "Writes strictly to TemporaryDirectory to avoid polluting workspace files",
        "Stores formula expressions cleanly for spreadsheet engine evaluation"
      ]
    },
    {
      "title": "Parameterized SQLite Student Database (285_student_database_project.py)",
      "description": "Creates and queries an in-memory SQLite student schema using parameterized SQL statements to prevent injection while keeping runs stateless.",
      "highlights": [
        "Executes DDL table creation and parameterized INSERT/SELECT queries",
        "Uses sqlite3 :memory: backend for clean, repeatable terminal runs"
      ],
      "coreScope": "Relational schema setup and safe SQL query execution",
      "trackTag": "Database Fundamentals",
      "tier": "Intermediate",
      "difficulty": "Intermediate",
      "estimatedTime": "1 Hour",
      "architecturalConstraints": [
        "Parameterized query placeholders required for all data insertion",
        "Ephemeral :memory: storage lifecycle scoped to script execution"
      ]
    },
    {
      "title": "Mocked Weather API & Local HTML Scraper (296–297)",
      "description": "Combines mocked HTTP JSON temperature parsing (Requests + unittest.mock) with local HTML article title extraction via BeautifulSoup CSS selectors.",
      "highlights": [
        "Separates HTTP client parsing logic from live network availability via Mock",
        "Extracts structured DOM headings using BeautifulSoup article h2 selectors"
      ],
      "coreScope": "API response validation and deterministic HTML parsing",
      "trackTag": "Integration & Parsing",
      "tier": "Advanced",
      "difficulty": "Advanced",
      "estimatedTime": "1.5 Hours",
      "architecturalConstraints": [
        "Zero external live network calls during verification runs",
        "Explicit HTTP status verification and structured JSON/DOM extraction"
      ]
    },
    {
      "title": "Core CLI & Business Logic Suite (281–294, 300)",
      "description": "Fifteen focused prototypes spanning a CLI calculator, quiz grader, inventory/cashier/library managers, CSPRNG password generator, file organizer, CSV analyzer, and task tracker.",
      "highlights": [
        "Applies input validation, set state transitions, secrets.choice, and pathlib automation",
        "Covers console arithmetic, expense tracking, contact lookup, and CSV aggregation"
      ],
      "coreScope": "Core Python data structures, OOP, file handling, and validation",
      "trackTag": "Core Python Capstones",
      "tier": "Core",
      "difficulty": "Intermediate",
      "estimatedTime": "6 Hours",
      "architecturalConstraints": [
        "Standard Library execution across all 15 core CLI prototypes",
        "Explicit exception raising or validation guards for invalid user inputs"
      ]
    }
  ],
  "codeLearningOutcomes": [
    {
      "pillar": "Core Python & Language Mechanics",
      "skills": [
        {
          "title": "Procedural & Functional Fluency",
          "description": "Write idiomatic scripts using built-in collections, comprehensions, generators, closures, decorators, and recursive patterns."
        },
        {
          "title": "Object-Oriented & File System Engineering",
          "description": "Architect reusable classes, custom exceptions, context managers, JSON/CSV/SQLite persistence, and modular packages."
        }
      ]
    },
    {
      "pillar": "Algorithms, Testing & Ecosystem Delivery",
      "skills": [
        {
          "title": "Algorithmic & Complexity Reasoning",
          "description": "Implement linear/non-linear data structures, graph traversals, sorting, backtracking, and dynamic programming with Big O awareness."
        },
        {
          "title": "Ecosystem Prototyping & Verification",
          "description": "Build and test local data pipelines, Excel automations, scrapers, and FastAPI services backed by unittest, pytest, mocking, and profiling."
        }
      ]
    }
  ],
  "codeLearningCurriculumSpecs": {
    "curriculumTrack": "Python Core to Ecosystem",
    "primaryLanguage": "Python",
    "executionRuntime": "CPython Interpreter & Virtualenv",
    "testVerification": "pytest, unittest & Logs"
  },
  "codeLearningSupplementaryResources": [
    {
      "title": "Module Study Guides & Captured Execution Logs",
      "description": "Every module directory pairs an Indonesian instructional Markdown guide with per-script terminal execution log screenshots.",
      "resources": [
        {
          "name": "Module Study Guides (module-01 through module-18 README.md)",
          "type": "Reference Guide",
          "format": "MD"
        },
        {
          "name": "Captured Execution Log Screenshots (output/*.png across 300 scripts)",
          "type": "Execution Log",
          "format": "PNG"
        }
      ]
    },
    {
      "title": "Environment Manifest & Reusable Module Helpers",
      "description": "Supporting dependency configuration and local helper modules referenced during package and ecosystem lessons.",
      "resources": [
        {
          "name": "requirements.txt (Ecosystem & Testing Dependencies)",
          "type": "Dependency Manifest",
          "format": "TXT"
        },
        {
          "name": "pembantu_belajar.py & paket_belajar/ (Module 12 Import Helpers)",
          "type": "Helper Package",
          "format": "PY"
        }
      ]
    }
  ]
}
```
