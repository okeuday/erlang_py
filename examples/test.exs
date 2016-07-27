#!/usr/bin/env elixir
# This is free and unencumbered software released into the public domain.

port = Port.open({:spawn_executable, "/usr/bin/env"},
  [:binary, {:packet, 4}, {:args, ["python", "-u", "port.py"]}, :nouse_stdio])

defmodule Python do
  def call(port, request) do
    Port.command(port, :erlang.term_to_binary(request))
    receive do
      {^port, {:data, response}} -> :erlang.binary_to_term(response)
    end
  end
end

IO.inspect Python.call(port, {:ping})

Port.close(port)
