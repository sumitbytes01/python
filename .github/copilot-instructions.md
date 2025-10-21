Project: learning Python examples (small scripts)

This repository is a personal learning collection of small Python example scripts grouped by topic (e.g. `comprehensions/`, `OOPS/`, `generators/`). There is no packaging, CI, or test harness — files are intended to be read and run individually.

How to be productive here
- Treat each file as a self-contained example. Typical usage is to run a script with the system Python (macOS zsh):

```bash
python3 path/to/file.py
```

- When making changes, keep examples small and focused. Avoid adding heavy dependencies or project-wide configuration unless there is a clear benefit.

Repository layout and notable examples
- `comprehensions/` — demonstrates list/set/dict comprehensions. Example: `comprehensions/set_comprehension.py` shows set comprehensions and iterating over a dictionary of ingredient lists.
- `generators/` — examples of generator functions and `send()`. Example: `generators/send_gen.py` demonstrates priming a generator with `next()` and using `send()` to pass values into the generator.
- `OOPS/` — class and instance behavior examples (e.g. `OOPS/simple_class.py`, `OOPS/named_space.py`). These files show dynamic attribute assignment and `getattr()` usage.
- `00_python/`, `functions/`, `decorators/`, `loops/`, `datatypes/` — topic examples intended for reading and experimenting.

Conventions and patterns to follow when editing or adding files
- Files are simple scripts: prefer clear, short top-level examples over large modules. If you find repeated code across files, consider adding a helper in `utils/`.
- Keep print-based examples deterministic when possible (e.g. sort sets before printing) so diffs and outputs are stable.
- Use explicit names: e.g. avoid ambiguous variable names like `coffee_menu` used as both set and list; keep types consistent to reduce confusion for learners.
- Prefer built-in types and standard library. The repo has no dependency management; adding external packages should include a short note in README and `requirements.txt` in `virtual/` if necessary.

Developer workflows (what works here)
- Run single files with `python3 <file>`.
- There is no test runner by default. Add small unit tests under a `tests/` folder if you want automated verification, and include instructions in README.
- Debug with print statements or run in an interactive REPL. Files are intentionally small — importing them from a REPL is a common workflow.

Patterns to call out for AI assistance
- When refactoring examples, keep behavior explicit: if changing a comprehension from list to set, update variable names and output text to avoid confusion.
- For generator examples, show the sequencing of `next()` and `send()` explicitly in comments, and include expected printed output where helpful.
- For OOP examples, prefer showing both class-level and instance-level attribute access in the same small snippet so learners can see differences (see `OOPS/named_space.py`).

Files and directories to reference when making changes
- `comprehensions/set_comprehension.py` — set/list comprehension examples and a potential bug: ensure there is no stray identifier at top-level.
- `generators/send_gen.py` — demonstrates `yield`/`send()` usage and priming generators.
- `OOPS/named_space.py` and `OOPS/simple_class.py` — dynamic attributes, `getattr`, and `pass` usage in empty classes.
- `README.md` — minimal repo description; update if you add project-level features (tests, packaging).

Style preferences for patches
- Small, focused edits. Preserve the didactic nature of examples (keep prints and inline comments explaining behavior).
- Make outputs deterministic where helpful (sort sets, format floats with `:.2f`).

If you add tests or CI
- Add a `tests/` folder and a simple `pytest` setup. Document `python3 -m pytest` in README.

Please review this guidance and tell me if you'd like more detail for any area (tests, packaging, or converting examples into importable modules).
