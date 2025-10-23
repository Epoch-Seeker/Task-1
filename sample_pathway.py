# sample_pathway.py
import pathway as pw

# Example: Create a simple table and print
def main():
    table = pw.debug.table([("Hello from Pathway inside Docker!",)])
    table.print()

if __name__ == "__main__":
    main()
