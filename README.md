# Operating System Lab — Experiments 

This repository contains a curated suite of **20 Operating System lab experiments** designed for deterministic, testable, and pedagogically clear outcomes. The labs progressively explore UNIX/POSIX interfaces, classical OS algorithms, scheduling, deadlocks, memory, and file systems.

---

## 📂 Overview

Each experiment provides:

* A clearly defined objective
* Required system interfaces and APIs
* Deterministic behavior suitable for automatic evaluation
* CLI-based user interaction
* Well-structured code modules

The goal of the lab suite is to expose students to **real system calls**, **process/thread concurrency**, and **core OS resource management algorithms**.

---

## 🧪 Experiment List

1. **UNIX Permission and umask Calculator** — Mode/umask arithmetic and decoding
2. **POSIX File Copy** — Using `open/read/write`
3. **Directory Listing & Metadata** — `ls` + `stat` subset
4. **grep-lite** — Simple deterministic text search
5. **Process Spawner & Exit Reporter** — `fork/exec/wait`
6. **Signal-Based Timeout Supervisor** — `sigaction`, `alarm`, `kill`
7. **Pipe-Based Filter Chain** — `pipe` + `dup2`
8. **Shared Memory Counter IPC** — `shm_open`, `mmap`, `sem_open`
9. **Threaded Deterministic Reducer** — `pthreads` + mutex
10. **Bounded Buffer Producer–Consumer** — Semaphore controlled
11. **CPU Scheduling Simulator I** — FCFS & Non-preemptive SJF
12. **CPU Scheduling Simulator II** — Round Robin
13. **Priority Scheduling Simulator** — Aging + Non-preemptive
14. **Deadlock Avoidance** — Banker's Algorithm
15. **Deadlock Detection** — Wait-for graph cycle
16. **Contiguous Memory Allocation** — First/Best/Worst fit
17. **Paging Address Translation** — Optional TLB simulation
18. **Page Replacement Simulator** — FIFO, LRU, OPT
19. **File Allocation Simulator** — Contiguous, Linked, Indexed
20. **Disk Scheduling Simulator** — FCFS, SSTF, SCAN, C‑SCAN

---

## 🛠️ Build Instructions

These experiments run as standalone CLI tools implemented in **Python 3.x** on a POSIX environment.

Run example:

```
$ python3 exp12_round_robin.py
```

Requirements:

* **Compiler:** GCC or Clang
* **OS:** Linux (POSIX compliant)
* **Headers:** `pthread.h`, `semaphore.h`, `sys/mman.h`, `fcntl.h`, etc.

---

## 📤 Input / Output Format

All tools are designed for:

* Deterministic input format
* Deterministic output format
* Scriptable behavior for CI auto-grading

Example (Round Robin Scheduling):

```
Input:
P1 0 7
P2 2 4
P3 4 1
Quantum 2

Output:
Gantt: P1 P2 P1 P3 P1 P2
Average Waiting Time: 4.33
Average Turnaround Time: 9.00
```

---

## 🧩 Determinism Requirement

Many lab variants intentionally avoid:

* Randomization
* OS‑dependent runtime fluctuations

This ensures reproducibility for both **grading** and **research replication**.

---

## 📁 Repository Layout (Suggested)

```
/exp01_perm_umask/
/exp02_posix_copy/
...
/exp20_disk_sched/
common/
README.md
Makefile
```

---

## 📚 Learning Outcomes

Upon completion, students gain proficiency in:

* UNIX/POSIX systems programming
* OS scheduling & memory/resource management
* IPC (pipes, shared memory, semaphores)
* Concurrency primitives (threads, mutexes)
* Deadlocks & avoidance strategies
* Virtual memory & FS allocation strategies

---

## 🧑‍🏫 Recommended Environment

| Component   | Recommendation                  |
| ----------- | ------------------------------- |
| OS          | Ubuntu / Debian / Arch / Fedora |
| Compiler    | GCC ≥ 10 or Clang ≥ 12          |
| Kernel APIs | POSIX compliant                 |

---

## 📜 License

[MIT License] or instructor-selected license.

---

## 👨‍💻 Author / Maintainer

**Author:** Anik Kirtania
**Department:** Computer Science and Engineering
**University:** University of Chittagong, Chittagong-4331

**Instructor:** Muhammad Anwarul Azim
Professor, Computer Science & Engineering,
University of Chittagong, Chittagong-4331

Operating Systems Lab 512
---

If you need a **Makefile**, **sample input**, **test harness**, or **CI scripts**, ask and I will generate them.
