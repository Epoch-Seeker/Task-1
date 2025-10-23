# sample_pathway.py
import pathway as pw

# Simple Pathway program that prints a message
def main():
    # Create a debug table
    t = pw.debug.Table([("Hello from Pathway inside Docker!",)])
    t.print()

if __name__ == "__main__":
    main()
