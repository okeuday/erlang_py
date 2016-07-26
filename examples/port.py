#!/usr/bin/env python
# This is free and unencumbered software released into the public domain.

import erlang, struct, sys, traceback

# Ensure compatibility with Python 2.x and 3.x both:
if sys.version_info >= (3, 0):
  sys.stdin  = sys.stdin.buffer
  sys.stdout = sys.stdout.buffer

def send(term, stream=sys.stdout):
  """Write an Erlang term to an output stream."""
  payload = erlang.term_to_binary(term)
  header = struct.pack('!I', len(payload))
  stream.write(header)
  stream.write(payload)

def recv(stream=sys.stdin):
  """Read an Erlang term from an input stream."""
  header = stream.read(4)
  if len(header) != 4:
    return None # EOF
  (length,) = struct.unpack('!I', header)
  payload = stream.read(length)
  if len(payload) != length:
    return None
  term = erlang.binary_to_term(payload)
  return term

def recv_loop(stream=sys.stdin):
  """Yield Erlang terms from an input stream."""
  message = recv(stream=stream)
  while message:
    yield message
    message = recv(stream=stream)

if __name__ == '__main__':
  try:
    for message in recv_loop():
      send(message)
  except:
    send(traceback.format_exc())
