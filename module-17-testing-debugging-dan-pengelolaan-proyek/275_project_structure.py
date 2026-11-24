from pathlib import Path

# Path dari file ini tetap benar meskipun terminal dibuka di direktori lain.
akar = Path(__file__).resolve().parent.parent
print("Ada kurikulum:", (akar / "Python_learning_modules.md").is_file())
print("Ada README root:", (akar / "README.md").is_file())