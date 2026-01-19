Operating System Lab Works


OVERVIEW
--------
This repository contains a suite of 20 Operating System laboratory experiments.
The projects progress from fundamental UNIX/Linux interfaces (permissions, 
file I/O, process control) to complex OS simulations (scheduling, deadlocks, 
memory management, and file systems).

These experiments are designed to meet specific deterministic output 
requirements for automated testing and grading.

--------------------------------------------------------------------------------
BUILD INSTRUCTIONS
--------------------------------------------------------------------------------
Each question corresponds to a standalone CLI tool. You can compile them 
using 'gcc' on a Linux system.

[PREREQUISITES]
- Compiler: GCC or Clang
- OS: Linux (POSIX compliant)

[COMPILATION EXAMPLES]
1. Basic Tools (Q1-Q7, Q11-Q20):
   $ gcc -o permcalc q01_permcalc.c -Wall -Wextra
   $ gcc -o schedsim1 q11_schedsim1.c -Wall -Wextra

2. IPC & Threading Tools (Q8-Q10):
   (Requires 'pthread' and 'rt' libraries)
   $ gcc -o shmcounter q08_shmcounter.c -Wall -Wextra -pthread -lrt
   $ gcc -o thrsum q09_thrsum.c -Wall -Wextra -pthread

--------------------------------------------------------------------------------
GLOBAL OUTPUT STANDARDS
--------------------------------------------------------------------------------
All tools adhere to a strict output format for automated testing.

1. SUCCESS OUTPUT
   Success messages generally start with "OK:".
   Example: OK: COMPLETED 1
   Example: OK: SUM 55

2. ERROR OUTPUT
   Errors are reported on a single line:
   ERROR: {CODE}: {MESSAGE}
   
   - The program must exit with a non-zero status code on error.
   - No additional whitespace or debug logs are allowed.

================================================================================
EXPERIMENT DETAILS
================================================================================

PART I: UNIX INTERFACES & FILE I/O
--------------------------------------------------------------------------------
Q01 | permcalc
    | Description: UNIX Permission Calculator
    | Topics: Octal modes, umask, Bitwise operations

Q02 | fdcopy
    | Description: POSIX File Copy (using open/read/write)
    | Topics: System Calls, File Descriptors, CRC32 Checksums

Q03 | dirreport
    | Description: Directory Listing & Metadata Report
    | Topics: opendir, readdir, stat struct

Q04 | greplite
    | Description: Deterministic Text Pattern Search (grep-like)
    | Topics: Buffered I/O, String Parsing

PART II: PROCESS CONTROL & SIGNALS
--------------------------------------------------------------------------------
Q05 | spawnwait
    | Description: Process Spawner & Exit Reporter
    | Topics: fork, exec, waitpid

Q06 | timeoutwrap
    | Description: Signal-Based Timeout Supervisor
    | Topics: sigaction, alarm, Signal handling

Q07 | pipechain
    | Description: Pipe-Based Filter Chain (Producer -> Filter -> Consumer)
    | Topics: pipe, dup2, IPC

PART III: IPC & SYNCHRONIZATION
--------------------------------------------------------------------------------
Q08 | shmcounter
    | Description: Shared Memory Counter IPC
    | Topics: shm_open, mmap, Named Semaphores

Q09 | thrsum
    | Description: Threaded Deterministic Reducer
    | Topics: pthreads, Mutex Locks

Q10 | pcbuf
    | Description: Bounded Buffer Producer-Consumer
    | Topics: Semaphores, Concurrency Invariants

PART IV: CPU SCHEDULING ALGORITHMS
--------------------------------------------------------------------------------
Q11 | schedsim1
    | Simulates: FCFS, SJF (Non-preemptive)

Q12 | schedsim2
    | Simulates: Round Robin (Preemptive)

Q13 | schedprio
    | Simulates: Priority Scheduling (Non-preemptive with Aging)

PART V: DEADLOCKS
--------------------------------------------------------------------------------
Q14 | banker
    | Description: Deadlock Avoidance using Banker's Algorithm
    | Topics: Safe Sequence, Resource Allocation

Q15 | wfgcheck
    | Description: Deadlock Detection via Wait-For Graph
    | Topics: Graph Theory, Cycle Detection

PART VI: MEMORY MANAGEMENT
--------------------------------------------------------------------------------
Q16 | memfit
    | Description: Contiguous Memory Allocation Simulator
    | Algorithms: First-Fit, Best-Fit, Worst-Fit

Q17 | pagetrans
    | Description: Paging Address Translation
    | Topics: Virtual-to-Physical mapping, TLB simulation

Q18 | pagerepl
    | Description: Page Replacement Simulator
    | Algorithms: FIFO, LRU, OPT (Belady's)

PART VII: STORAGE & FILE SYSTEMS
--------------------------------------------------------------------------------
Q19 | filealloc
    | Description: File Allocation Strategy Simulator
    | Algorithms: Contiguous, Linked, Indexed

Q20 | disksched
    | Description: Disk Scheduling Simulator
    | Algorithms: FCFS, SSTF, SCAN, C-SCAN

--------------------------------------------------------------------------------
REFERENCES
--------------------------------------------------------------------------------
1. Operating System Concepts (Silberschatz, Galvin, Gagne)
2. Modern Operating Systems (Tanenbaum, Bos)
3. The Linux Programming Interface (Michael Kerrisk)
4. Linux man-pages (man7.org)
OVERVIEW
--------
This repository contains a suite of 20 Operating System laboratory experiments.
The projects progress from fundamental UNIX/Linux interfaces (permissions, 
file I/O, process control) to complex OS simulations (scheduling, deadlocks, 
memory management, and file systems).

These experiments are designed to meet specific deterministic output 
requirements for automated testing and grading.

--------------------------------------------------------------------------------
BUILD INSTRUCTIONS
--------------------------------------------------------------------------------
Each question corresponds to a standalone CLI tool. You can compile them 
using 'gcc' on a Linux system.

[PREREQUISITES]
- Compiler: GCC or Clang
- OS: Linux (POSIX compliant)

[COMPILATION EXAMPLES]
1. Basic Tools (Q1-Q7, Q11-Q20):
   $ gcc -o permcalc q01_permcalc.c -Wall -Wextra
   $ gcc -o schedsim1 q11_schedsim1.c -Wall -Wextra

2. IPC & Threading Tools (Q8-Q10):
   (Requires 'pthread' and 'rt' libraries)
   $ gcc -o shmcounter q08_shmcounter.c -Wall -Wextra -pthread -lrt
   $ gcc -o thrsum q09_thrsum.c -Wall -Wextra -pthread

--------------------------------------------------------------------------------
GLOBAL OUTPUT STANDARDS
--------------------------------------------------------------------------------
All tools adhere to a strict output format for automated testing.

1. SUCCESS OUTPUT
   Success messages generally start with "OK:".
   Example: OK: COMPLETED 1
   Example: OK: SUM 55

2. ERROR OUTPUT
   Errors are reported on a single line:
   ERROR: {CODE}: {MESSAGE}
   
   - The program must exit with a non-zero status code on error.
   - No additional whitespace or debug logs are allowed.

================================================================================
EXPERIMENT DETAILS
================================================================================

PART I: UNIX INTERFACES & FILE I/O
--------------------------------------------------------------------------------
Q01 | permcalc
    | Description: UNIX Permission Calculator
    | Topics: Octal modes, umask, Bitwise operations

Q02 | fdcopy
    | Description: POSIX File Copy (using open/read/write)
    | Topics: System Calls, File Descriptors, CRC32 Checksums

Q03 | dirreport
    | Description: Directory Listing & Metadata Report
    | Topics: opendir, readdir, stat struct

Q04 | greplite
    | Description: Deterministic Text Pattern Search (grep-like)
    | Topics: Buffered I/O, String Parsing

PART II: PROCESS CONTROL & SIGNALS
--------------------------------------------------------------------------------
Q05 | spawnwait
    | Description: Process Spawner & Exit Reporter
    | Topics: fork, exec, waitpid

Q06 | timeoutwrap
    | Description: Signal-Based Timeout Supervisor
    | Topics: sigaction, alarm, Signal handling

Q07 | pipechain
    | Description: Pipe-Based Filter Chain (Producer -> Filter -> Consumer)
    | Topics: pipe, dup2, IPC

PART III: IPC & SYNCHRONIZATION
--------------------------------------------------------------------------------
Q08 | shmcounter
    | Description: Shared Memory Counter IPC
    | Topics: shm_open, mmap, Named Semaphores

Q09 | thrsum
    | Description: Threaded Deterministic Reducer
    | Topics: pthreads, Mutex Locks

Q10 | pcbuf
    | Description: Bounded Buffer Producer-Consumer
    | Topics: Semaphores, Concurrency Invariants

PART IV: CPU SCHEDULING ALGORITHMS
--------------------------------------------------------------------------------
Q11 | schedsim1
    | Simulates: FCFS, SJF (Non-preemptive)

Q12 | schedsim2
    | Simulates: Round Robin (Preemptive)

Q13 | schedprio
    | Simulates: Priority Scheduling (Non-preemptive with Aging)

PART V: DEADLOCKS
--------------------------------------------------------------------------------
Q14 | banker
    | Description: Deadlock Avoidance using Banker's Algorithm
    | Topics: Safe Sequence, Resource Allocation

Q15 | wfgcheck
    | Description: Deadlock Detection via Wait-For Graph
    | Topics: Graph Theory, Cycle Detection

PART VI: MEMORY MANAGEMENT
--------------------------------------------------------------------------------
Q16 | memfit
    | Description: Contiguous Memory Allocation Simulator
    | Algorithms: First-Fit, Best-Fit, Worst-Fit

Q17 | pagetrans
    | Description: Paging Address Translation
    | Topics: Virtual-to-Physical mapping, TLB simulation

Q18 | pagerepl
    | Description: Page Replacement Simulator
    | Algorithms: FIFO, LRU, OPT (Belady's)

PART VII: STORAGE & FILE SYSTEMS
--------------------------------------------------------------------------------
Q19 | filealloc
    | Description: File Allocation Strategy Simulator
    | Algorithms: Contiguous, Linked, Indexed

Q20 | disksched
    | Description: Disk Scheduling Simulator
    | Algorithms: FCFS, SSTF, SCAN, C-SCAN

--------------------------------------------------------------------------------
REFERENCES
--------------------------------------------------------------------------------
1. Operating System Concepts (Silberschatz, Galvin, Gagne)
2. Modern Operating Systems (Tanenbaum, Bos)
3. The Linux Programming Interface (Michael Kerrisk)
4. Linux man-pages (man7.org)
