import sys

if len(sys.argv) < 2:
    print("Usage: python helloworld.py [name1] [name2] ... [nameN]")
    sys.exit(1)

for name in sys.argv[1:]:
    print(f"Hello, {name}!")