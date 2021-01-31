load harness

@test "mytest-1" {
  check '2 - 3 * 4' '-10'
}

@test "mytest-2" {
  check '-2 - 3 * -4 - 6 * 2 * 0' '10'
}

@test "mytest-3" {
  check '3 * 8 - 9 * 10' '-66'
}

@test "mytest-4" {
  check '5 * 6 - 9' '21'
}

@test "mytest-5" {
  check '5 * 8 - 6 * 4 - -2' '18'
}

@test "mytest-6" {
  check '-10 / 4 + 3 / 6 + 8' '6.0'
}

@test "mytest-7" {
  check '100 + -100 / 2' '50.0'
}

@test "mytest-8" {
  check '1000 / 50 + -0' '20.0'
}

@test "mytest-9" {
  check '2 * 4 / -2 + 3 * 8' '20.0'
}

@test "mytest-10" {
  check '-1 + -20 / 8' '-3.5'
}
