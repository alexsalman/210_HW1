load harness

@test "medium-1" {
  check '2 + 3 * 4' '14'
}

@test "medium-2" {
  check '-2 + 3 * -4 + 6 * 2 * 0' '-14'
}

@test "medium-3" {
  check '3 * 8 + 9 * 10' '114'
}

@test "medium-4" {
  check '5 * 6 + 9' '39'
}

@test "medium-5" {
  check '5 * 8 + 6 * 4 + -2' '62'
}

@test "medium-6" {
  check '-10 * 4 + 3 * 6 + 8' '-14'
}

@test "medium-7" {
  check '100 + -100 * 0' '100'
}

@test "medium-8" {
  check '0 * 0 + 0 + -0' '0'
}

@test "medium-9" {
  check '2 * 4 * -2 + 3 * 8' '8'
}

@test "medium-10" {
  check '-1 + -0 * 8' '-1'
}