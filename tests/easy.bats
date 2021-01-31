load harness

@test "easy-1" {
  check '2 + 3' '5'
}

@test "easy-2" {
  check '3 + 92' '95'
}

@test "easy-3" {
  check '100 + 0' '100'
}

@test "easy-4" {
  check '-1 + -3' '-4'
}

@test "easy-5" {
  check '10 + -3' '7'
}

@test "easy-6" {
  check '-1 + 0' '-1'
}

@test "easy-7" {
  check '99 + 3 + 12 + 2' '116'
}

@test "easy-8" {
  check '2 + 3 + 4 + -1' '8'
}

@test "easy-9" {
  check '-1 + -2 + 3' '0'
}

@test "easy-10" {
  check '-1 + -5 + -1' '-7'
}

@test "easy-11" {
  check '9 * 3' '27'
}

@test "easy-12" {
  check '-3 * 4' '-12'
}

@test "easy-13" {
  check '0 * 2' '0'
}

@test "easy-14" {
  check '20 * 5' '100'
}

@test "easy-15" {
  check '0 * 2' '0'
}

@test "easy-16" {
  check '-2 * -0' '0'
}

@test "easy-17" {
  check '2 * 3 * 4 * 1000' '24000'
}

@test "easy-18" {
  check '1 * -2 * 3 * -4' '24'
}

@test "easy-19" {
  check '9 * 2 * 99 * 999' '1780218'
}

@test "easy-20" {
  check '1 * 1 * -1 * 1' '-1'
}
