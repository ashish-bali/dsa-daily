# dsa-daily

Daily data-structures & algorithms practice, organized by pattern.

Each problem lives in its own folder: `NNN-problem-slug/` containing a
`solution.py` (annotated, tested) and a `README.md` (problem statement,
approach, and complexity).

## Patterns

| Folder | Focus |
| --- | --- |
| [arrays-hashing](./arrays-hashing) | Hash maps, frequency counting, set membership |
| [two-pointers](./two-pointers) | Opposite / same-direction pointers on sorted data |
| [sliding-window](./sliding-window) | Contiguous subarray / substring windows |
| [binary-search](./binary-search) | Search on sorted arrays and answer spaces |
| [graphs-bfs-dfs](./graphs-bfs-dfs) | Traversal, connected components, shortest path |
| [stacks-queues](./stacks-queues) | LIFO/FIFO, monotonic stacks, deques |

## Progress

| # | Problem | Pattern | Difficulty |
| --- | --- | --- | --- |
| 001 | [Two Sum](./arrays-hashing/001-two-sum) | Arrays & Hashing | Easy |

## Conventions

- **Naming:** `NNN-kebab-case-title` (e.g. `001-two-sum`).
- **Solution:** each `solution.py` exposes a named function and runs a small
  set of assertions when executed directly (`python solution.py`).
- **README:** states the problem, the chosen approach, and time/space
  complexity.
