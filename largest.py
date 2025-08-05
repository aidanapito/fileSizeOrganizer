import os
import heapq

# Head count
TOP_N = 20

def find_largest_files(root_path):
    heap = []  #min-heap of (size, path)
    for dirpath, dirnames, filenames in os.walk(root_path):
        for fname in filenames:
            full_path = os.path.join(dirpath, fname)
            try:
                size = os.path.getsize(full_path)
            except (OSError, PermissionError):
                continue
            if len(heap) < TOP_N:
                heapq.heappush(heap, (size, full_path))
            else:
                heapq.heappushpop(heap, (size, full_path))
    return sorted(heap, reverse=True)

if __name__ == "__main__":
    # / to any directory
    results = find_largest_files("/")
    for size, path in results:
        print(f"{size/1024**2:9.2f} MB   {path}")
