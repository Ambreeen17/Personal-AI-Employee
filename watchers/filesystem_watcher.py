import time
from pathlib import Path
import shutil

VAULT_PATH = Path("../AI_Employee_Vault")
DROP_FOLDER = Path("../Drop_Folder")
NEEDS_ACTION = VAULT_PATH / "Needs_Action"

DROP_FOLDER.mkdir(exist_ok=True)
NEEDS_ACTION.mkdir(exist_ok=True)

print("Filesystem watcher started...")

processed = set()

while True:
    for file in DROP_FOLDER.iterdir():
        if file.is_file() and file.name not in processed:
            dest = NEEDS_ACTION / f"FILE_{file.name}"
            shutil.copy(file, dest)

            meta = dest.with_suffix(".md")
            meta.write_text(f"""---
type: file_drop
original_name: {file.name}
status: pending
---

New file dropped for processing.
""")

            processed.add(file.name)
            print(f"New task created: {file.name}")

    time.sleep(5)

