import ctypes

# Get memory address 0, your kernel shouldn't allow this:
ctypes.string_at(0)
