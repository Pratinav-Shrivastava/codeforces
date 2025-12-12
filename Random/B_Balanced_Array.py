import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        k = n // 2        
        if k & 1:
            out_lines.append("NO")
            continue
        
        evens = [str(2 * i) for i in range(1, k + 1)]
        odds  = [str(2 * i - 1) for i in range(1, k)]
        last  = str(3 * k - 1)
        out_lines.append("YES")
        out_lines.append(" ".join(evens + odds + [last]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
