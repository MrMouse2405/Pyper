<img align="left" width="80" height="80" src="Logo.png" alt="Pyper Logo">

# Pyper

<br>

Pyper: **Py**thon for **Per**formance.

Pyper is:
1. Compatible with cpython ecosystem.
2. Powered by LuaJIT (🚀 BLAZING FAST JIT VM)

Pyper aims to:
1. Be a drop-in replacement for cpython interpreter.
2. Yield significant performance gain.

Caveats:
1. Performance: No gains, if python script just calls c-modules.
2. Numbers: Pyper ints are just regular 64-bit floating point numbers. However, we do offer INT behaviour.
3. Parallelism / Concurrency: Pyper is still in-development, this feature is not implemented yet.

