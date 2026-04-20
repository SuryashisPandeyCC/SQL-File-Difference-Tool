import sys
import difflib
from colorama import Fore, init
import os

# initialize colorama
init()

# check arguments
if len(sys.argv) < 3:
    print("Usage: python sqldiff.py old.sql new.sql [--explain]")
    sys.exit(1)

old_file = sys.argv[1]
new_file = sys.argv[2]
use_explain = "--explain" in sys.argv

# read files
def read_file(path):
    try:
        with open(path, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found -> {path}")
        sys.exit(1)

old_lines = read_file(old_file)
new_lines = read_file(new_file)

# generate diff
diff = list(difflib.unified_diff(
    old_lines,
    new_lines,
    fromfile="old.sql",
    tofile="new.sql"
))

# print colored diff
for line in diff:
    if line.startswith("+") and not line.startswith("+++"):
        print(Fore.GREEN + line, end="")
    elif line.startswith("-") and not line.startswith("---"):
        print(Fore.RED + line, end="")
    else:
        print(line, end="")

# optional Claude explanation
if use_explain:
    try:
        import anthropic

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("\n[!] Missing ANTHROPIC_API_KEY environment variable")
            sys.exit(1)

        client = anthropic.Anthropic(api_key=api_key)

        diff_text = "".join(diff)

        if len(diff_text.strip()) == 0:
            print("\nNo differences found.")
            sys.exit(0)

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[
                {
                    "role": "user",
                    "content": f"Explain this SQL difference clearly:\n\n{diff_text}"
                }
            ]
        )

        explanation = response.content[0].text

        print("\n\n--- AI Explanation ---\n")
        print(explanation)

    except ImportError:
        print("\n[!] anthropic library not installed. Run: pip install anthropic")